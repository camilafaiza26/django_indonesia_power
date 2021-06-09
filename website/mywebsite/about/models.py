from django.db import models
from django.core.validators import MaxValueValidator
from master.models import Pemasok, PLTU, Waktu, Sumbertambang

# Create your models here.
class FactSolverKontrakPemasok(models.Model):
    kontrakpemasok_id = models.IntegerField(primary_key=True)
    pltu = models.ForeignKey(PLTU, on_delete=models.DO_NOTHING)
    pemasok = models.ForeignKey(Pemasok, on_delete=models.DO_NOTHING,)
    #sumbertambang = models.ForeignKey(Sumbertambang, on_delete=models.DO_NOTHING)
    nama_sumber_tambang = models.CharField(max_length=500)
    gcv_kcal_kg = models.IntegerField(blank=True, null=True)
    jenis_bb = models.CharField(max_length=3, blank=True, null=True)
    ts_persen = models.FloatField(blank=True, null=True)
    fob_rp_mt = models.FloatField(blank=True, null=True)
    moda = models.CharField(max_length=30, blank=True, null=True)
    freight_cost_rp_mt = models.FloatField(blank=True, null=True)
    cif_rp_mt = models.FloatField(blank=True, null=True)
    cif_rp_cal = models.FloatField(blank=True, null=True)
    waktu = models.ForeignKey(Waktu, on_delete=models.DO_NOTHING,)

    class Meta:
        managed = False
        db_table = 'fact_solver_kontrak_pemasok'

class FactSolverHasilSatuan(models.Model):
    noproses_id = models.IntegerField(primary_key=True)
    persentase_lrc_persen = models.FloatField()
    persentase_mrc_persen = models.FloatField()
    volume_lrc_mt = models.FloatField()
    volume_mrc_mt = models.FloatField()
    total_volume_akhir = models.FloatField()
    total_kalori_akhir = models.FloatField()
    total_ts_akhir = models.FloatField()
    total_harga_akhir = models.FloatField()
    rp_cal = models.FloatField()
    rp_mt = models.FloatField()
    #rp_mt_setahun = models.FloatField(db_column='rp/mt setahun')  # Field renamed to remove unsuitable characters.
    nilai_kalor_kcal_kg = models.FloatField(db_column='nilai_kalor_kCal_kg')  # Field name made lowercase.
    total_sulphur_persen = models.FloatField()  # Field renamed to remove unsuitable characters.
    status_model = models.CharField(max_length=50)

    class Meta:
        managed = False
        db_table = 'fact_solver_hasil_satuan'

class FactSolverHasilOptimalisasisolver(models.Model):
    hasil_id = models.AutoField(primary_key=True)
    pltu = models.ForeignKey(PLTU, models.DO_NOTHING, blank=True, null=True)
    pemasok = models.ForeignKey(Pemasok, models.DO_NOTHING, blank=True, null=True)
    noproses = models.ForeignKey(FactSolverHasilSatuan, models.DO_NOTHING)
    waktu = models.DateTimeField(blank=True, null=True)
    nama_sumber_tambang = models.CharField(max_length=500, blank=True, null=True)
    hasilsolver_volume_mt = models.FloatField(blank=True, null=True)
    hasilsolver_kalori_kcal = models.FloatField(blank=True, null=True)
    hasilsolver_ts_persen = models.FloatField(blank=True, null=True)
    hasilsolver_harga_rp_mt_cal = models.FloatField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'fact_solver_hasil_optimalisasisolver'

class FactSolverRencana(models.Model):
    rencana_id = models.AutoField(primary_key=True)
    pltu = models.ForeignKey(PLTU, models.DO_NOTHING, blank=True, null=True)
    waktu = models.DateTimeField()
    persentase_rencana_lrc_persen = models.FloatField(db_column='persentase_rencana_LRC_persen', blank=True, null=True)  # Field name made lowercase.
    persentase_rencana_mrc_persen = models.FloatField(db_column='persentase_rencana_MRC_persen', blank=True, null=True)  # Field name made lowercase.
    input_bb_mt = models.FloatField(blank=True, null=True)
    input_nilai_kalor_kcal_kg = models.FloatField(db_column='input_nilai_kalor_kCal_kg', blank=True, null=True)  # Field name made lowercase.
    input_total_sulphur = models.FloatField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'fact_solver_rencana'


class FactSolverResumeHasilOptimasi(models.Model):
    rhos_id = models.AutoField(primary_key=True)
    pltu = models.ForeignKey(PLTU, models.DO_NOTHING, blank=True, null=True)
    pemasok = models.ForeignKey(Pemasok, models.DO_NOTHING, blank=True, null=True)
    noproses = models.ForeignKey(FactSolverHasilSatuan, models.DO_NOTHING)
    waktu = models.DateTimeField(blank=True, null=True)
    jenis_bb = models.CharField(max_length=3, blank=True, null=True)
    rhos_volume = models.FloatField(blank=True, null=True)
    rhos_kalori_kcal = models.FloatField(db_column='rhos_kalori_kCal', blank=True, null=True)  # Field name made lowercase.
    rhos_ts_persen = models.FloatField(blank=True, null=True)
    rhos_harga_rp_mt_cal = models.FloatField(blank=True, null=True)


    class Meta:
        managed = False
        db_table = 'fact_solver_resume_hasil_optimasi'

class FactSolverRangePasokanDiinginkan(models.Model):
    range_pasokan_id = models.IntegerField(primary_key=True)
    pltu = models.ForeignKey(PLTU, models.DO_NOTHING)
    pemasok = models.ForeignKey(Pemasok, models.DO_NOTHING)
    waktu_0 = models.DateTimeField(db_column='waktu')  # Field renamed because of name conflict.
    minimal_volume = models.FloatField()
    minimal_kali_perbulan = models.IntegerField()
    minimal_total_perbulan = models.FloatField()
    maksimal_volume = models.FloatField()
    maksimal_kali_perbulan = models.IntegerField()
    maksimal_total_perbulan = models.FloatField()

    class Meta:
        managed = False
        db_table = 'fact_solver_range_pasokan_diinginkan'

