from django.contrib import admin
from equipsmith_dev.models import Book, Impression


# Register your models here.
# admin.site.register(Book)
# admin.site.register(Impression)

class BookAdmin(admin.ModelAdmin):
    # ページ一覧に出したい項目の指定
    list_display = ('id', 'name', 'publisher', 'page',)
    # 修正リンクでクリックできる項目の指定
    list_display_links = ('id', 'name',)


admin.site.register(Book, BookAdmin)


class ImpressionAdmin(admin.ModelAdmin):
    list_display = ('id', 'comment',)
    list_display_links = ('id', 'comment',)
    raw_id_fields = ('book',)


admin.site.register(Impression, ImpressionAdmin)