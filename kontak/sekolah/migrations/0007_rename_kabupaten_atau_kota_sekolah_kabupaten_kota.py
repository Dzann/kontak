# Generated by Django 4.1.5 on 2023-01-20 07:47

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ("sekolah", "0006_alter_sekolah_npsn_alter_sekolah_status"),
    ]

    operations = [
        migrations.RenameField(
            model_name="sekolah",
            old_name="kabupaten_atau_kota",
            new_name="kabupaten_kota",
        ),
    ]
