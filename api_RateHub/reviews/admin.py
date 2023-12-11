from django.contrib import admin
from import_export import resources
from import_export.admin import ImportExportModelAdmin

from .models import Category, Genre, Title, Review, Comment


class CategoryResource(resources.ModelResource):
    class Meta:
        model = Category


class CategoryAdmin(ImportExportModelAdmin):
    resource_classes = [CategoryResource]


class GenreResource(resources.ModelResource):
    class Meta:
        model = Genre


class GenreAdmin(ImportExportModelAdmin):
    resource_classes = [GenreResource]


class TitleResource(resources.ModelResource):
    class Meta:
        model = Title


class TitleAdmin(ImportExportModelAdmin):
    resource_classes = [TitleResource]


class ReviewResource(resources.ModelResource):
    class Meta:
        model = Review


class ReviewAdmin(ImportExportModelAdmin):
    resource_classes = [ReviewResource]


class CommentResource(resources.ModelResource):
    class Meta:
        model = Comment


class CommentAdmin(ImportExportModelAdmin):
    resource_classes = [CommentResource]


admin.site.register(Category, CategoryAdmin)
admin.site.register(Genre, GenreAdmin)
admin.site.register(Title, TitleAdmin)
admin.site.register(Review, ReviewAdmin)
admin.site.register(Comment, CommentAdmin)
