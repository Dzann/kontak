from django.contrib import admin
from .models import DataSiswa
# Register your models here.

class statusSiswa(admin.ModelAdmin):
    list_display = ['nama','nisn','email']
admin.site.register(DataSiswa, statusSiswa)