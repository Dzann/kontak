from django.contrib import admin
from .models import sekolah
# Register your models here.
class namaSekolah(admin.ModelAdmin):
    list_display = ['nama','email','web']

admin.site.register(sekolah,namaSekolah)

