from django.db import models
from django.core.validators import MaxValueValidator

# Create your models here.

# Create your models here.
class Pemasok(models.Model):
    pemasok_id = models.IntegerField(primary_key=True, validators=[MaxValueValidator(99999)])
    nama_pemasok = models.CharField(max_length=100, blank=True, null=True)
    jenis_bb = models.CharField(max_length=3, blank=True, null=True)
    kontrak = models.CharField(max_length=30, blank=True, null=True)
    ts = models.CharField(max_length=30, blank=True, null=True)

    class Meta:
        db_table = 'dim_pemasok'

class PLTU(models.Model):
    pltu_id = models.IntegerField(primary_key=True, validators=[MaxValueValidator(99999)])
    nama_pltu = models.CharField(max_length=50, blank=True, null=True)
    lokasi_pltu = models.CharField(max_length=100, blank=True, null=True)
    kode_pltu = models.CharField(max_length=5, blank=True, null=True)

    class Meta:
        db_table = 'dim_pltu'

class Sumbertambang(models.Model):
    sumbertambang_id = models.IntegerField(primary_key=True, validators=[MaxValueValidator(9999999999)])
    nama_sumber_tambang = models.CharField(max_length=500, blank=True, null=True)
    kode_sumber_tambang = models.CharField(max_length=100, blank=True, null=True)
    class Meta:
        db_table = 'dim_sumbertambang'

class Waktu(models.Model):
    waktu_id = models.IntegerField(primary_key=True, validators=[MaxValueValidator(9999999999)])
    waktu_mulai = models.DateField(blank=True, null=True)
    waktu_selesai = models.DateField(blank=True, null=True)
    triwulan = models.CharField(max_length=7, blank=True, null=True)
    tahun = models.TextField(blank=True, null=True)  # This field type is a guess.

    class Meta:
        #managed = False
        db_table = 'dim_waktu'
