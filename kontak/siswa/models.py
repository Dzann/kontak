from django.utils.translation import gettext_lazy as _
from django.db import models
from enum import Enum
# Create your models here.
class jenis_kelamin(models.TextChoices) :
    laki_laki = 'L', _('Laki-laki')
    perempuan = 'P', _('Perempuan')

class DataSiswa(models.Model):
    nisn = models.CharField(max_length=10)
    nama = models.CharField(max_length=50)
    email = models.CharField(max_length=50, blank=True, null=True)
    no_Telepon = models.CharField(max_length=20, blank=True, null=True)
    asal_Sekolah = models.ForeignKey('sekolah.sekolah', on_delete=models.CASCADE, null=True, blank=True)
    alamat = models.TextField(blank=True, null=True)
    jenis_kelamin = models.CharField(
        max_length=1,
        choices=jenis_kelamin.choices
        )
    tempat_lahir = models.CharField(max_length=50)
    tanggal_lahir = models.DateField()
    

    create_at = models.DateTimeField(auto_now_add=True)
    update_at = models.DateTimeField(auto_now=True)
    
    def __str__(self):
        return self.nama

    class Meta:
        db_table = 'siswa'
        ordering = ['-id']

    

