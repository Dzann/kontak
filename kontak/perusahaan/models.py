from django.db import models
from django.utils.translation import gettext_lazy as _


class jenisPerusahaan(models.TextChoices):
    PT = 'PT', _('perseroan terbatas')
    CV = 'CV', _('Commanditaire Vennootschap')
    FIRMA = 'VOF', _('vennootschap onder firma')
    PERSERO = 'PRS', _('PT. PERMODALAN NASIONAL MADANI (PERSERO)')
    KOPERASI = 'KO', _('Koperasi')
    PERSEORANGAN = 'PO', _('PERSEORANGAN')

class perusahaan(models.Model):
    nama = models.CharField(max_length=50)
    email = models.CharField(max_length=50)
    web = models.CharField(max_length=100, blank=True, null=True)
    no_Telpon = models.CharField(max_length=20)
    alamat = models.TextField(blank=True, null=True)
    jenis_Perusahaan = models.CharField(
        max_length=3,
        choices=jenisPerusahaan.choices,
    )

    create_at = models.DateTimeField(auto_now_add=True)
    update_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.nama

    class Meta:
        db_table = 'perusahaan'
        ordering = ['-id']