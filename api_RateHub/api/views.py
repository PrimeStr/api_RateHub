from django.core.mail import send_mail
from django.db.models import Avg
from django_filters.rest_framework import DjangoFilterBackend
from django.shortcuts import get_object_or_404
from rest_framework import filters, viewsets, mixins
from rest_framework.decorators import action
from rest_framework.pagination import PageNumberPagination
from rest_framework.permissions import AllowAny, IsAuthenticated
from rest_framework.response import Response
from rest_framework_simplejwt.tokens import RefreshToken
from rest_framework.status import HTTP_200_OK, HTTP_400_BAD_REQUEST
from rest_framework.views import APIView
from rest_framework.viewsets import ModelViewSet

from api_RateHub.settings import EMAIL_HOST
from reviews.models import Category, Genre, Title, Review
from users.models import User

from .filters import TitleFilter
from .permissions import (IsSuperuserOrAdminOrReadOnly, IsAdminOnly,
                          SelfUserOnly, IsAuthorModeratorAdminOrReadOnly)
from .serializers import (CategorySerializer, GenreSerializer,
                          TitleCreateUpdateDestroySerializer,
                          SignUpSerializer, TokenSerializer,
                          AdminOrModeratorSerializer, UsersSerializer,
                          TitleReadOnlySerializer, ReviewSerializer,
                          CommentSerializer)


class ListCreateDestroyViewSet(mixins.ListModelMixin,
                               mixins.CreateModelMixin,
                               mixins.DestroyModelMixin,
                               viewsets.GenericViewSet):
    pass


class CategoryViewSet(ListCreateDestroyViewSet):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer
    pagination_class = PageNumberPagination
    permission_classes = (IsSuperuserOrAdminOrReadOnly,)
    filter_backends = (filters.SearchFilter,)
    search_fields = ("name",)
    lookup_field = "slug"


class GenreViewSet(ListCreateDestroyViewSet):
    queryset = Genre.objects.all()
    serializer_class = GenreSerializer
    pagination_class = PageNumberPagination
    permission_classes = (IsSuperuserOrAdminOrReadOnly,)
    filter_backends = (filters.SearchFilter,)
    search_fields = ("name",)
    lookup_field = "slug"


class TitleViewSet(viewsets.ModelViewSet):
    queryset = Title.objects.all().annotate(rating=Avg("reviews__score"))
    permission_classes = (IsSuperuserOrAdminOrReadOnly,)
    pagination_class = PageNumberPagination
    filter_backends = (DjangoFilterBackend,)
    filterset_class = TitleFilter

    def get_serializer_class(self):
        if self.action in ('list', 'retrieve'):
            return TitleReadOnlySerializer
        return TitleCreateUpdateDestroySerializer


class SignUpViewSet(APIView):
    permission_classes = (AllowAny,)

    def post(self, request):
        serializer = SignUpSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        user, _ = User.objects.get_or_create(**serializer.validated_data)
        send_mail(
            subject='Код подтверждения',
            message=(f'Ваш confirmation_code: {user.confirmation_code}'),
            from_email=EMAIL_HOST,
            recipient_list=[request.data.get('email')],
            fail_silently=False,
        )
        return Response(
            serializer.data, status=HTTP_200_OK
        )


class TokenViewSet(APIView):
    def post(self, request):
        serializer = TokenSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        user = get_object_or_404(
            User, username=request.data.get('username')
        )
        if str(user.confirmation_code) == request.data.get(
                'confirmation_code'
        ):
            refresh = RefreshToken.for_user(user)
            token = {'token': str(refresh.access_token)}
            return Response(
                token, status=HTTP_200_OK
            )
        return Response(
            {'confirmation_code': 'Неверный код подтверждения.'},
            status=HTTP_400_BAD_REQUEST
        )


class UsersViewSet(ModelViewSet):
    queryset = User.objects.all()
    serializer_class = AdminOrModeratorSerializer
    lookup_field = 'username'
    filter_backends = (filters.SearchFilter,)
    search_fields = ('username',)
    permission_classes = (IsAuthenticated, IsAdminOnly)
    http_method_names = ('get', 'post', 'patch', 'delete')

    @action(
        methods=['get', 'patch'], detail=False,
        url_path='me', permission_classes=(SelfUserOnly,)
    )
    def me_user(self, request):
        if request.method == 'GET':
            user = get_object_or_404(
                User, username=request.user
            )
            serializer = self.get_serializer(user)
            return Response(serializer.data)

        user = get_object_or_404(
            User, username=request.user
        )
        serializer = UsersSerializer(user, data=request.data, partial=True)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data, status=HTTP_200_OK)


class ReviewViewSet(ModelViewSet):
    serializer_class = ReviewSerializer
    permission_classes = (IsAuthorModeratorAdminOrReadOnly,)

    def get_queryset(self):
        title = get_object_or_404(Title, id=self.kwargs.get('title_id'))
        return title.reviews.all()

    def perform_create(self, serializer):
        title = get_object_or_404(Title, id=self.kwargs.get('title_id'))
        serializer.save(author=self.request.user, title=title)


class CommentViewSet(ModelViewSet):
    serializer_class = CommentSerializer
    permission_classes = (IsAuthorModeratorAdminOrReadOnly,)

    def get_queryset(self):
        review = get_object_or_404(Review, id=self.kwargs.get('review_id'))
        return review.comments.all().order_by('id')

    def perform_create(self, serializer):
        review = get_object_or_404(
            Review,
            title_id=self.kwargs.get('title_id'),
            pk=self.kwargs.get('review_id')
        )
        serializer.save(author=self.request.user, review=review)
