from django.db import models
from django.utils.translation import gettext_lazy as _


class jenisSekolah(models.TextChoices):
    SMK = 'S', _('SMK')
    UNIVERSITAS = 'U', _('Universitas')

class sekolah(models.Model):
    nama = models.CharField(max_length=50)
    email = models.CharField(max_length=50)
    web = models.CharField(max_length=100, blank=True, null=True)
    no_Telpon = models.CharField(max_length=20)
    alamat = models.TextField(blank=True, null=True)
    jenis_Sekolah = models.CharField(
        max_length=1,
        choices=jenisSekolah.choices,
    )

    create_at = models.DateTimeField(auto_now_add=True)
    update_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.nama

    class Meta:
        db_table = 'sekolah'
        ordering = ['-id']