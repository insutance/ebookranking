from django.contrib import admin
from .models import Kyobo, Yes24, Aladin, Naver, Ridibooks, TotalBooks

# Register your models here.
admin.site.register(Kyobo)
admin.site.register(Yes24)
admin.site.register(Aladin)
admin.site.register(Naver)
admin.site.register(Ridibooks)
admin.site.register(TotalBooks)
