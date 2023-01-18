from django.db import models
from django.utils.translation import gettext_lazy as _
from django.contrib.auth.models import User

class StatusSekolah(models.TextChoices):
    SWASTA = 'S', _('Swasta')
    NEGERI = 'N', _('Negeri')

class sekolah(models.Model):
    npsn = models.CharField(max_length=10, null=False, default='0')
    nama = models.CharField(max_length=50)
    status = models.CharField(
        max_length=1,
        choices=StatusSekolah.choices,
        null=False, 
        default='0',
    )
    email = models.CharField(max_length=50)
    web = models.CharField(max_length=100, blank=True, null=True)
    Telp = models.CharField(max_length=20)
    alamat = models.TextField(blank=True, null=True)
    provinsi = models.CharField(max_length=50,blank=True, null=True)
    kabupaten_atau_kota = models.CharField(max_length=50,blank=True, null=True)
    kecamatan = models.CharField(max_length=50,blank=True, null=True)

    # created_by = models.ForeignKey
    create_at = models.DateTimeField(auto_now_add=True)
    update_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.nama

    class Meta:
        db_table = 'sekolah'
        ordering = ['-id']
        verbose_name_plural = "sekolah"