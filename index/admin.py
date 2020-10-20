from django.contrib import admin
from .models import Book, TotalBooks

class BookAdmin(admin.ModelAdmin):
    list_display = ['rank', 'title', 'price', 'bookstore', 'weight', 'date']
    list_display_links = ['title']

class TotalBookAdmin(admin.ModelAdmin):
    list_display = ['rank', 'title', 'weight', 'date']
    list_display_links = ['title']

# Register your models here.
admin.site.register(Book, BookAdmin)
admin.site.register(TotalBooks, TotalBookAdmin)

