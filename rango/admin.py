from django.contrib import admin
from rango.models import Category,Page

class PageInLine (admin.TabularInline):
    model=Page
    extra = 3

class CategoryAdmin (admin.ModelAdmin):
    fields = ['name','views','likes','slug']
    inlines = [PageInLine]
    list_display = ('name','views','likes')

admin.site.register(Category,CategoryAdmin)

class PageAdmin (admin.ModelAdmin):
    fields = ['title','category','url']
    list_display = ['title','category','url']

admin.site.register(Page,PageAdmin)

