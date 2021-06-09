from django.db import models
from django.core.validators import MaxValueValidator
from master.models import *

# Create your models here.

# Create your models here.
class Data_grading(models.Model):
    id_grading = models.IntegerField(primary_key=True, validators=[MaxValueValidator(99999999999)])
    nama_pltu = models.CharField(max_length=100, blank=True, null=True)
    nama_pemasok = models.CharField(max_length=100, blank=True, null=True)
    gcv_realisasi = models.FloatField(blank=True, null=True)
    tm_realisasi = models.FloatField(blank=True, null=True)
    ts_realisasi = models.FloatField(blank=True, null=True)
    ash_realisasi = models.FloatField(blank=True, null=True)
    hgi_realisasi = models.FloatField(blank=True, null=True)
    idt_realisasi = models.FloatField(blank=True, null=True)
    pengurang_gcv = models.FloatField(blank=True, null=True)
    pengurang_tm = models.FloatField(blank=True, null=True)
    pengurang_ts = models.FloatField(blank=True, null=True)
    pengurang_ash = models.FloatField(blank=True, null=True)
    pengurang_hgi = models.FloatField(blank=True, null=True)
    pengurang_idt = models.FloatField(blank=True, null=True)
    persentase_realisasi = models.FloatField(blank=True, null=True)
    pengurang_pasokan = models.FloatField(blank=True, null=True)
    persentase_penolakan = models.FloatField(blank=True, null=True)
    pengurang_batas_penolakan = models.FloatField(blank=True, null=True)
    nilai_akhir = models.FloatField(blank=True, null=True)
    klasifikasi = models.CharField(max_length=100, blank=True, null=True)

    class Meta:
        db_table = 'grading_supplier'

class FactGradingRekapanPenilaianPemasok(models.Model):
    rekapanpenilaian_id = models.AutoField(primary_key=True)
    pltu = models.ForeignKey(PLTU, models.DO_NOTHING, blank=True, null=True)
    pemasok = models.ForeignKey(Pemasok, models.DO_NOTHING, blank=True, null=True)
    waktu = models.ForeignKey(Waktu, models.DO_NOTHING, blank=True, null=True)
    p1_gcv_typical = models.FloatField(blank=True, null=True)
    p1_gcv_penolakan = models.FloatField(blank=True, null=True)
    p1_tm_typical = models.FloatField(blank=True, null=True)
    p1_tm_penolakan = models.FloatField(blank=True, null=True)
    p1_ts_typical = models.FloatField(blank=True, null=True)
    p1_ts_penolakan = models.FloatField(blank=True, null=True)
    p1_ash_typical = models.FloatField(blank=True, null=True)
    p1_ash_penolakan = models.FloatField(blank=True, null=True)
    p1_hgi_typical = models.FloatField(blank=True, null=True)
    p1_hgi_penolakan1 = models.FloatField(blank=True, null=True)
    p1_hgi_penolakan2 = models.FloatField(blank=True, null=True)
    p1_idt_typical = models.FloatField(blank=True, null=True)
    p1_idt_penolakan = models.FloatField(blank=True, null=True)
    p1_gcv_realisasi = models.FloatField(blank=True, null=True)
    p1_tm_realisasi = models.FloatField(blank=True, null=True)
    p1_ts_realisasi = models.FloatField(blank=True, null=True)
    p1_ash_realisasi = models.FloatField(blank=True, null=True)
    p1_hgi_realisasi = models.FloatField(blank=True, null=True)
    p1_idt_realisasi = models.FloatField(blank=True, null=True)
    p1_gcv_pengurang = models.FloatField(blank=True, null=True)
    p1_tm_pengurang = models.FloatField(blank=True, null=True)
    p1_ts_pengurang = models.FloatField(blank=True, null=True)
    p1_ash_pengurang = models.FloatField(blank=True, null=True)
    p1_hgi_pengurang = models.FloatField(blank=True, null=True)
    p1_idt_pengurang = models.FloatField(blank=True, null=True)
    p1_gcv_nilaiakhir = models.FloatField(blank=True, null=True)
    p1_tm_nilaiakhir = models.FloatField(blank=True, null=True)
    p1_ts_nilaiakhir = models.FloatField(blank=True, null=True)
    p1_ash_nilaiakhir = models.FloatField(blank=True, null=True)
    p1_hgi_nilaiakhir = models.FloatField(blank=True, null=True)
    p1_idt_nilaiakhir = models.FloatField(blank=True, null=True)
    p2_konfirmasi = models.FloatField(blank=True, null=True)
    p2_realisasi = models.FloatField(blank=True, null=True)
    p2_persentase_pasokan = models.FloatField(blank=True, null=True)
    p2_pengurang_pasokan = models.FloatField(blank=True, null=True)
    p2_nilai_akhir = models.FloatField(blank=True, null=True)
    p3_total_shipment = models.FloatField(blank=True, null=True)
    p3_jmlh_shipment_tertolak = models.FloatField(blank=True, null=True)
    p3_persentase_penolakan = models.FloatField(blank=True, null=True)
    p3_pengurang_penolakan = models.FloatField(blank=True, null=True)
    nilai_akhir = models.FloatField(blank=True, null=True)
    klasifikasi = models.CharField(max_length=50, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'fact_grading_rekapan_penilaian_pemasok'

class FactGradingPerhitunganTertimbang(models.Model):
    perhitungan_tertimbang_id = models.AutoField(primary_key=True)
    pltu = models.ForeignKey(PLTU, models.DO_NOTHING, blank=True, null=True)
    pemasok = models.ForeignKey(Pemasok, models.DO_NOTHING, blank=True, null=True)
    waktu = models.ForeignKey(Waktu, models.DO_NOTHING, blank=True, null=True)
    pt_gcv = models.FloatField(blank=True, null=True)
    pt_tm = models.FloatField(blank=True, null=True)
    pt_ts = models.FloatField(blank=True, null=True)
    pt_ash = models.FloatField(blank=True, null=True)
    pt_hgi = models.FloatField(blank=True, null=True)
    pt_idt = models.FloatField(blank=True, null=True)
    pt_mt = models.FloatField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'fact_grading_perhitungan_tertimbang'

class FactGradingPenolakan(models.Model):
    penolakan_id = models.AutoField(primary_key=True)
    pltu = models.ForeignKey(PLTU, models.DO_NOTHING, blank=True, null=True)
    pemasok = models.ForeignKey(Pemasok, models.DO_NOTHING, blank=True, null=True)
    waktu = models.ForeignKey(Waktu, models.DO_NOTHING, blank=True, null=True)
    pn_gcv = models.FloatField(blank=True, null=True)
    pn_tm = models.FloatField(blank=True, null=True)
    pn_ts = models.FloatField(blank=True, null=True)
    pn_ash = models.FloatField(blank=True, null=True)
    pn_hgi = models.FloatField(blank=True, null=True)
    pn_idt = models.FloatField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'fact_grading_penolakan'
