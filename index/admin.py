from django.contrib import admin
from .models import Book, TotalBooks

class BookAdmin(admin.ModelAdmin):
    list_display = ['rank', 'title', 'price', 'bookstore', 'weight', 'date']
    list_display_links = ['title']

<<<<<<< HEAD
class TotalBooksAdmin(admin.ModelAdmin):
=======
class TotalBookAdmin(admin.ModelAdmin):
>>>>>>> 20d152de566d3db7d4adaef0cb15bd7c850ffd57
    list_display = ['rank', 'title', 'weight', 'date']
    list_display_links = ['title']

# Register your models here.
admin.site.register(Book, BookAdmin)
<<<<<<< HEAD
admin.site.register(TotalBooks, TotalBooksAdmin)
=======
admin.site.register(TotalBooks, TotalBookAdmin)
>>>>>>> 20d152de566d3db7d4adaef0cb15bd7c850ffd57

