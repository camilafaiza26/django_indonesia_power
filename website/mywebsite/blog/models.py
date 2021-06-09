from django.db import models
from django.core.validators import MaxValueValidator
from master.models import *

# Create your models here.
class Rekap_shipment(models.Model):

    tm_id = models.IntegerField(primary_key=True,validators=[MaxValueValidator(99999999999)])
    pltu = models.CharField(null=True, blank=True,db_column='PLTU', max_length=50)  # Field name made lowercase.
    no = models.IntegerField(null=True, blank=True,validators=[MaxValueValidator(99999999999)])
    periode = models.CharField(null=True, blank=True,max_length=15)
    bbo_id = models.CharField(null=True, blank=True,max_length=20)
    shipment_code = models.CharField(null=True, blank=True,max_length=30)
    voyage_code = models.CharField(null=True, blank=True,max_length=30)
    voyage = models.IntegerField(null=True, blank=True,validators=[MaxValueValidator(99999999999)])
    pemasok = models.ForeignKey(Pemasok, models.DO_NOTHING)
    nama_pemasok = models.CharField(null=True, blank=True,max_length=10,db_column='pemasok')
    transhipment_shifting = models.CharField(null=True, blank=True,max_length=50 )  # Field renamed to remove unsuitable characters.
    sumber_tambang = models.CharField(null=True, blank=True,max_length=50,db_column='sumber_tambang')
    loading_port = models.CharField(null=True, blank=True,max_length=50)
    unloading_port = models.CharField(null=True, blank=True,max_length=30)
    tb = models.CharField(null=True, blank=True,max_length=30)
    bg = models.CharField(null=True, blank=True,max_length=30)
    konfirmasi_rakor = models.DateTimeField(null=True, blank=True,)
    time_arrival = models.DateTimeField(null=True, blank=True,)
    status_laycan = models.CharField(null=True, blank=True,max_length=25)
    batas_maks_not_accepted = models.DateTimeField(null=True, blank=True,)
    nor_accepted_pltu = models.DateTimeField(null=True, blank=True,)
    despatch_demurrage_keterangan = models.CharField(null=True, blank=True, max_length=30)  # Field renamed to remove unsuitable characters.
    despatch_demurrage_biaya = models.FloatField(null=True, blank=True)  # Field renamed to remove unsuitable characters.
    berthed_time = models.DateTimeField(null=True, blank=True,)
    commenced_unloading = models.DateTimeField(null=True, blank=True,)
    start_cleaning = models.DateTimeField(null=True, blank=True,)
    completed_unloading = models.DateTimeField(null=True, blank=True,)
    cast_off = models.DateTimeField(null=True, blank=True,)
    gangguan_jam_coal_handling_facility = models.FloatField(null=True, blank=True)  # Field renamed to remove unsuitable characters.
    gangguan_jam_kendala_eksternal = models.FloatField(null=True, blank=True,)  # Field renamed to remove unsuitable characters.
    gangguan_jam_force_majeur = models.FloatField(null=True, blank=True)  # Field renamed to remove unsuitable characters.
    gangguan_jam_gangguan_pengurang_flowrate = models.FloatField()  # Field renamed to remove unsuitable characters.
    volume_b_l = models.FloatField(null=True, blank=True)  # Field renamed to remove unsuitable characters.
    volume_ds = models.FloatField(null=True, blank=True)
    initial_draught_surve_start = models.DateTimeField(null=True, blank=True,)
    initial_draught_surve_finish = models.DateTimeField(null=True, blank=True,)
    lift_off_loader_start = models.DateTimeField(null=True, blank=True,)
    lift_off_loader_finish = models.DateTimeField(null=True, blank=True,)
    final_draught_survey_start = models.DateTimeField(null=True, blank=True,)
    final_draught_survey_fiinish = models.DateTimeField(null=True, blank=True,)
    port_stay_day = models.FloatField(null=True, blank=True,)
    port_stay_hour = models.FloatField(null=True, blank=True,)
    berthing_time = models.FloatField(null=True, blank=True,)
    initial_draught = models.FloatField(null=True, blank=True,)
    waiting_commenced = models.FloatField(null=True, blank=True,)
    persiapan_bongkar = models.FloatField(null=True, blank=True,)
    lift_off_loader = models.FloatField(null=True, blank=True,)
    final_draught = models.FloatField(null=True, blank=True,)
    waiting_cast_off = models.FloatField(null=True, blank=True,)
    persiapan_cast_off = models.FloatField(null=True, blank=True,)
    waktu_tunggu_sandar = models.FloatField(null=True, blank=True,)
    waktu_bongkar = models.FloatField(null=True, blank=True,)
    waktu_cleaning = models.FloatField(null=True, blank=True,)
    flowrate_gross_mt_hours = models.FloatField(null=True, blank=True)  # Field renamed to remove unsuitable characters. Field renamed because it ended with '_'.
    flowrate_nett_mt_hours = models.FloatField(null=True, blank=True)  # Field renamed to remove unsuitable characters. Field renamed because it ended with '_'.
    status_umpire = models.CharField(null=True, blank=True,max_length=15)
    roaloading_gcv_arb_kcal_kg = models.FloatField(null=True, blank=True)  # Field renamed to remove unsuitable characters. Field renamed because it ended with '_'.
    roaloading_tm_arb = models.FloatField(null=True, blank=True,db_column='roaloading_tm_arb_persen')  # Field renamed to remove unsuitable characters. Field renamed because it ended with '_'.
    roaloading_im_adb = models.FloatField(null=True, blank=True,db_column='roaloading_im_adb_persen')  # Field renamed to remove unsuitable characters. Field renamed because it ended with '_'.
    roaloading_ash_content_arb = models.FloatField(null=True, blank=True,db_column='roaloading_ash_content_arb_persen')  # Field renamed to remove unsuitable characters. Field renamed because it ended with '_'.
    roaloading_ash_content_adb = models.FloatField(null=True, blank=True,db_column='roaloading_ash_content_adb_persen')  # Field renamed to remove unsuitable characters. Field renamed because it ended with '_'.
    roaloading_vm_adb = models.FloatField(null=True, blank=True,db_column='roaloading_vm_adb_persen')  # Field renamed to remove unsuitable characters. Field renamed because it ended with '_'.
    roaloading_fc_adb = models.FloatField(null=True, blank=True,db_column='roaloading_fc_adb_persen')  # Field renamed to remove unsuitable characters. Field renamed because it ended with '_'.
    roaloading_total_sulphur_arb = models.FloatField(null=True, blank=True,db_column='roaloading_total_sulphur_arb_persen')  # Field renamed to remove unsuitable characters. Field renamed because it ended with '_'.
    roaloading_total_sulphur_dafb = models.FloatField(null=True, blank=True,db_column='roaloading_total_sulphur_dafb_persen')  # Field renamed to remove unsuitable characters. Field renamed because it ended with '_'.
    roaloading_hgi_index = models.FloatField(null=True, blank=True)  # Field renamed to remove unsuitable characters. Field renamed because it ended with '_'.
    coaloading_gcv_arb_kcal_kg = models.FloatField(null=True, blank=True)  # Field renamed to remove unsuitable characters. Field renamed because it ended with '_'.
    coaloading_gcv_adb_kcal_kg = models.FloatField(null=True, blank=True)  # Field renamed to remove unsuitable characters. Field renamed because it ended with '_'.
    coaloading_gcv_db_kcal_kg = models.FloatField(null=True, blank=True)  # Field renamed to remove unsuitable characters. Field renamed because it ended with '_'.
    coaloading_gcv_dafb_kcal_kg = models.IntegerField(null=True, blank=True,validators=[MaxValueValidator(99999999999)])  # Field renamed to remove unsuitable characters. Field renamed because it ended with '_'.
    coaloading_tm_arb = models.FloatField(null=True, blank=True,db_column='coaloading_tm_arb_persen')  # Field renamed to remove unsuitable characters. Field renamed because it ended with '_'.
    coaloading_im_adb = models.FloatField(null=True, blank=True,db_column='coaloading_im_adb_persen')  # Field renamed to remove unsuitable characters. Field renamed because it ended with '_'.
    coaloading_ash_content_arb = models.FloatField(null=True, blank=True,db_column='coaloading_ash_content_arb_persen')  # Field renamed to remove unsuitable characters. Field renamed because it ended with '_'.
    coaloading_ash_content_adb = models.FloatField(null=True, blank=True,db_column='coaloading_ash_content_adb_persen')  # Field renamed to remove unsuitable characters. Field renamed because it ended with '_'.
    coaloading_ash_content_db = models.FloatField(null=True, blank=True,db_column='coaloading_ash_content_db_persen')  # Field renamed to remove unsuitable characters. Field renamed because it ended with '_'.
    coaloading_vm_arb = models.FloatField(null=True, blank=True,db_column='coaloading_vm_arb_persen')  # Field renamed to remove unsuitable characters. Field renamed because it ended with '_'.
    coaloading_vm_adb = models.FloatField(null=True, blank=True,db_column='coaloading_vm_adb_persen')  # Field renamed to remove unsuitable characters. Field renamed because it ended with '_'.
    coaloading_vm_db = models.FloatField(null=True, blank=True,db_column='coaloading_vm_db_persen')  # Field renamed to remove unsuitable characters. Field renamed because it ended with '_'.
    coaloading_vm_dafb = models.FloatField(null=True, blank=True,db_column='coaloading_vm_dafb_persen')  # Field renamed to remove unsuitable characters. Field renamed because it ended with '_'.
    coaloading_fc_arb = models.FloatField(null=True, blank=True,db_column='coaloading_fc_arb_persen')  # Field renamed to remove unsuitable characters. Field renamed because it ended with '_'.
    coaloading_fc_adb = models.FloatField(null=True, blank=True,db_column='coaloading_fc_adb_persen')  # Field renamed to remove unsuitable characters. Field renamed because it ended with '_'.
    coaloading_fc_db = models.FloatField(null=True, blank=True,db_column='coaloading_fc_db_persen')  # Field renamed to remove unsuitable characters. Field renamed because it ended with '_'.
    coaloading_fc_dafb = models.FloatField(null=True, blank=True,db_column='coaloading_fc_dafb_persen')  # Field renamed to remove unsuitable characters. Field renamed because it ended with '_'.
    coaloading_total_sulphur_arb = models.FloatField(null=True, blank=True,db_column='coaloading_total_sulphur_arb_persen')  # Field renamed to remove unsuitable characters. Field renamed because it ended with '_'.
    coaloading_total_sulphur_adb = models.FloatField(null=True, blank=True,db_column='coaloading_total_sulphur_adb_persen')  # Field renamed to remove unsuitable characters. Field renamed because it ended with '_'.
    coaloading_total_sulphur_db = models.FloatField(null=True, blank=True,db_column='coaloading_total_sulphur_db_persen')  # Field renamed to remove unsuitable characters. Field renamed because it ended with '_'.
    coaloading_total_sulphur_dafb = models.FloatField(null=True, blank=True,db_column='coaloading_total_sulphur_dafb_persen')  # Field renamed to remove unsuitable characters. Field renamed because it ended with '_'.
    coaloading_hgi_index = models.FloatField(null=True, blank=True)  # Field renamed to remove unsuitable characters. Field renamed because it ended with '_'.
    coaloading_idt_reducing_c = models.FloatField(null=True, blank=True,db_column="coaloading_idt_reducing_'c")  # Field renamed to remove unsuitable characters. Field renamed because it ended with '_'.
    coaunloading_gcv_arb_kcal_kg = models.FloatField(null=True, blank=True)  # Field renamed to remove unsuitable characters. Field renamed because it ended with '_'.
    coaunloading_gcv_adb_kcal_kg = models.FloatField(null=True, blank=True)  # Field renamed to remove unsuitable characters. Field renamed because it ended with '_'.
    coaunloading_gcv_db_kcal_kg = models.FloatField(null=True, blank=True)  # Field renamed to remove unsuitable characters. Field renamed because it ended with '_'.
    coaunloading_gcv_dafb_kcal_kg = models.FloatField(null=True, blank=True)  # Field renamed to remove unsuitable characters. Field renamed because it ended with '_'.
    coaunloading_tm_arb = models.FloatField(null=True, blank=True,db_column='coaunloading_tm_arb_persen')  # Field renamed to remove unsuitable characters. Field renamed because it ended with '_'.
    coaunloading_im_adb = models.FloatField(null=True, blank=True,db_column='coaunloading_im_adb_persen')  # Field renamed to remove unsuitable characters. Field renamed because it ended with '_'.
    coaunloading_ash_content_arb = models.FloatField(null=True, blank=True,db_column='coaunloading_ash_content_arb_persen')  # Field renamed to remove unsuitable characters. Field renamed because it ended with '_'.
    coaunloading_ash_content_adb = models.FloatField(null=True, blank=True,db_column='coaunloading_ash_content_adb_persen')  # Field renamed to remove unsuitable characters. Field renamed because it ended with '_'.
    coaunloading_ash_content_db = models.FloatField(null=True, blank=True,db_column='coaunloading_ash_content_db_persen')  # Field renamed to remove unsuitable characters. Field renamed because it ended with '_'.
    coaunloading_vm_arb = models.FloatField(null=True, blank=True,db_column='coaunloading_vm_arb_persen')  # Field renamed to remove unsuitable characters. Field renamed because it ended with '_'.
    coaunloading_vm_adb = models.FloatField(null=True, blank=True,db_column='coaunloading_vm_adb_persen')  # Field renamed to remove unsuitable characters. Field renamed because it ended with '_'.
    coaunloading_vm_db = models.FloatField(null=True, blank=True,db_column='coaunloading_vm_db_persen')  # Field renamed to remove unsuitable characters. Field renamed because it ended with '_'.
    coaunloading_vm_dafb = models.FloatField(null=True, blank=True,db_column='coaunloading_vm_dafb_persen')  # Field renamed to remove unsuitable characters. Field renamed because it ended with '_'.
    coaunloading_fc_arb = models.FloatField(null=True, blank=True,db_column='coaunloading_fc_arb_persen')  # Field renamed to remove unsuitable characters. Field renamed because it ended with '_'.
    coaunloading_fc_adb = models.FloatField(null=True, blank=True,db_column='coaunloading_fc_adb_persen')  # Field renamed to remove unsuitable characters. Field renamed because it ended with '_'.
    coaunloading_fc_db = models.FloatField(null=True, blank=True,db_column='coaunloading_fc_db_persen')  # Field renamed to remove unsuitable characters. Field renamed because it ended with '_'.
    coaunloading_fc_dafb = models.FloatField(null=True, blank=True,db_column='coaunloading_fc_dafb_persen')  # Field renamed to remove unsuitable characters. Field renamed because it ended with '_'.
    coaunloading_total_sulphur_arb = models.FloatField(null=True, blank=True,db_column='coaunloading_total_sulphur_arb_persen')  # Field renamed to remove unsuitable characters. Field renamed because it ended with '_'.
    coaunloading_total_sulphur_adb = models.FloatField(null=True, blank=True,db_column='coaunloading_total_sulphur_adb_persen')  # Field renamed to remove unsuitable characters. Field renamed because it ended with '_'.
    coaunloading_total_sulphur_db = models.FloatField(null=True, blank=True,db_column='coaunloading_total_sulphur_db_persen')  # Field renamed to remove unsuitable characters. Field renamed because it ended with '_'.
    coaunloading_total_sulphur_dafb = models.FloatField(null=True, blank=True,db_column='coaunloading_total_sulphur_dafb_persen')  # Field renamed to remove unsuitable characters. Field renamed because it ended with '_'.
    coaunloading_c_adb = models.FloatField(null=True, blank=True,db_column='coaunloading_c_adb_persen')  # Field renamed to remove unsuitable characters. Field renamed because it ended with '_'.
    coaunloading_h_adb = models.FloatField(null=True, blank=True,db_column='coaunloading_h_adb_persen')  # Field renamed to remove unsuitable characters. Field renamed because it ended with '_'.
    coaunloading_n_adb = models.FloatField(null=True, blank=True,db_column='coaunloading_n_adb_persen')  # Field renamed to remove unsuitable characters. Field renamed because it ended with '_'.
    coaunloading_n_dafb = models.FloatField(null=True, blank=True,db_column='coaunloading_n_dafb_persen')  # Field renamed to remove unsuitable characters. Field renamed because it ended with '_'.
    coaunloading_o_adb = models.FloatField(null=True, blank=True,db_column='coaunloading_o_adb_persen')  # Field renamed to remove unsuitable characters. Field renamed because it ended with '_'.
    coaunloading_hgi_index = models.FloatField(null=True, blank=True)  # Field renamed to remove unsuitable characters. Field renamed because it ended with '_'.
    coaunloading_sizing_70mm = models.FloatField(null=True, blank=True,db_column='coaunloading_sizing_persen_70mm')  # Field renamed to remove unsuitable characters.
    coaunloading_sizing_50mm = models.FloatField(null=True, blank=True,db_column='coaunloading_sizing_persen_50mm')  # Field renamed to remove unsuitable characters.
    coaunloading_sizing_32mm = models.FloatField(null=True, blank=True,db_column='coaunloading_sizing_persen_32mm')  # Field renamed to remove unsuitable characters.
    coaunloading_sizing_2_38mm = models.FloatField(null=True, blank=True,db_column='coaunloading_sizing_persen_2,38mm')  # Field renamed to remove unsuitable characters.
    coaunloading_ashanalysis_sio2 = models.FloatField(null=True, blank=True,db_column='coaunloading_ashanalysis_persen_SiO2')  # Field name made lowercase. Field renamed to remove unsuitable characters.
    coaunloading_ashanalysis_ai2o3 = models.FloatField(null=True, blank=True,db_column='coaunloading_ashanalysis_persen_AI2O3')  # Field name made lowercase. Field renamed to remove unsuitable characters.
    coaunloading_ashanalysis_fe2o3 = models.FloatField(null=True, blank=True,db_column='coaunloading_ashanalysis_persen_FE2O3')  # Field name made lowercase. Field renamed to remove unsuitable characters.
    coaunloading_ashanalysis_cao = models.FloatField(null=True, blank=True,db_column='coaunloading_ashanalysis_persen_CaO')  # Field name made lowercase. Field renamed to remove unsuitable characters.
    coaunloading_ashanalysis_mgo = models.FloatField(null=True, blank=True,db_column='coaunloading_ashanalysis_persen_MgO')  # Field name made lowercase. Field renamed to remove unsuitable characters.
    coaunloading_ashanalysis_na2o = models.FloatField(null=True, blank=True,db_column='coaunloading_ashanalysis_persen_Na2O')  # Field name made lowercase. Field renamed to remove unsuitable characters.
    coaunloading_ashanalysis_k2o = models.FloatField(null=True, blank=True,db_column='coaunloading_ashanalysis_persen_K2O')  # Field name made lowercase. Field renamed to remove unsuitable characters.
    coaunloading_ashanalysis_tio2 = models.FloatField(null=True, blank=True,db_column='coaunloading_ashanalysis_persen_TiO2')  # Field name made lowercase. Field renamed to remove unsuitable characters.
    coaunloading_ashanalysis_so3 = models.FloatField(null=True, blank=True,db_column='coaunloading_ashanalysis_persen_SO3')  # Field name made lowercase. Field renamed to remove unsuitable characters.
    coaunloading_ashanalysis_mno2 = models.FloatField(null=True, blank=True,db_column='coaunloading_ashanalysis_persen_MnO2')  # Field name made lowercase. Field renamed to remove unsuitable characters.
    coaunloading_ashanalysis_p2o5 = models.FloatField(null=True, blank=True,db_column='coaunloading_ashanalysis_persen_P2O5')  # Field name made lowercase. Field renamed to remove unsuitable characters.
    coaunloading_slagging_factor = models.CharField(null=True, blank=True,max_length=15)
    coaunloading_fouling_factor = models.CharField(null=True, blank=True,max_length=15)
    coaunloading_idt_reducing_c = models.FloatField(null=True, blank=True,db_column="coaunloading_idt_reducing_'c")  # Field name made lowercase. Field renamed to remove unsuitable characters. Field renamed because it ended with '_'.
    coaunloading_ht_reducing_c = models.FloatField(null=True, blank=True,db_column="coaunloading_ht_reducing_'c")  # Field name made lowercase. Field renamed to remove unsuitable characters. Field renamed because it ended with '_'.
    coaunloading_ht_oxidizing_c = models.FloatField(null=True, blank=True,db_column="coaunloading_ht_oxidizing_'c")  # Field name made lowercase. Field renamed to remove unsuitable characters. Field renamed because it ended with '_'.
    coaunloading_hg_arb = models.FloatField(null=True)
    labip_gcv_arb_kcal_kg = models.FloatField(null=True, blank=True)  # Field renamed to remove unsuitable characters. Field renamed because it ended with '_'.
    labip_gcv_adb_kcal_kg = models.FloatField(null=True, blank=True)  # Field renamed to remove unsuitable characters. Field renamed because it ended with '_'.
    labip_gcv_db_kcal_kg = models.FloatField(null=True, blank=True)  # Field renamed to remove unsuitable characters. Field renamed because it ended with '_'.
    labip_gcv_dafb = models.FloatField(null=True, blank=True,db_column='labip_gcv_dafb_kcal_kg')  # Field renamed to remove unsuitable characters. Field renamed because it ended with '_'.
    labip_tm_arb = models.FloatField(null=True, blank=True,db_column='labip_tm_arb_persen')  # Field renamed to remove unsuitable characters. Field renamed because it ended with '_'.
    labip_im_adb = models.FloatField(null=True, blank=True,db_column='labip_im_adb_persen')  # Field renamed to remove unsuitable characters. Field renamed because it ended with '_'.
    labip_ash_content_arb = models.FloatField(null=True, blank=True,db_column='labip_ash_content_arb_persen')  # Field renamed to remove unsuitable characters. Field renamed because it ended with '_'.
    labip_ash_content_adb = models.FloatField(null=True, blank=True,db_column='labip_ash_content_adb_persen')  # Field renamed to remove unsuitable characters. Field renamed because it ended with '_'.
    labip_ash_content_db = models.FloatField(null=True, blank=True,db_column='labip_ash_content_db_persen')  # Field renamed to remove unsuitable characters. Field renamed because it ended with '_'.
    labip_vm_arb = models.FloatField(null=True, blank=True,db_column='labip_vm_arb_persen')  # Field renamed to remove unsuitable characters. Field renamed because it ended with '_'.
    labip_vm_adb = models.FloatField(null=True, blank=True,db_column='labip_vm_adb_persen')  # Field renamed to remove unsuitable characters. Field renamed because it ended with '_'.
    labip_vm_db = models.FloatField(null=True, blank=True,db_column='labip_vm_db_persen')  # Field renamed to remove unsuitable characters. Field renamed because it ended with '_'.
    labip_vm_dafb = models.FloatField(null=True, blank=True,db_column='labip_vm_dafb_persen')  # Field renamed to remove unsuitable characters. Field renamed because it ended with '_'.
    labip_fc_arb = models.FloatField(null=True, blank=True,db_column='labip_fc_arb_persen')  # Field renamed to remove unsuitable characters. Field renamed because it ended with '_'.
    labip_fc_adb = models.FloatField(null=True, blank=True,db_column='labip_fc_adb_persen')  # Field renamed to remove unsuitable characters. Field renamed because it ended with '_'.
    labip_fc_db = models.FloatField(null=True, blank=True,db_column='labip_fc_db_persen')  # Field renamed to remove unsuitable characters. Field renamed because it ended with '_'.
    labip_fc_dafb = models.FloatField(null=True, blank=True,db_column='labip_fc_dafb_persen')  # Field renamed to remove unsuitable characters. Field renamed because it ended with '_'.
    labip_total_sulphur_arb = models.FloatField(null=True, blank=True,db_column='labip_total_sulphur_arb_persen')  # Field renamed to remove unsuitable characters. Field renamed because it ended with '_'.
    labip_total_sulphur_adb = models.FloatField(null=True, blank=True,db_column='labip_total_sulphur_adb_persen')  # Field renamed to remove unsuitable characters. Field renamed because it ended with '_'.
    labip_total_sulphur_db = models.FloatField(null=True, blank=True,db_column='labip_total_sulphur_db_persen')  # Field renamed to remove unsuitable characters. Field renamed because it ended with '_'.
    labip_total_sulphur_dafb = models.FloatField(null=True, blank=True,db_column='labip_total_sulphur_dafb_persen')  # Field renamed to remove unsuitable characters. Field renamed because it ended with '_'.
    labip_c_adb = models.FloatField(null=True, blank=True,db_column='labip_c_adb_persen')  # Field renamed to remove unsuitable characters. Field renamed because it ended with '_'.
    labip_h_adb = models.FloatField(null=True, blank=True,db_column='labip_h_adb_persen')  # Field renamed to remove unsuitable characters. Field renamed because it ended with '_'.
    labip_n_adb = models.FloatField(null=True, blank=True,db_column='labip_n_adb_persen')  # Field renamed to remove unsuitable characters. Field renamed because it ended with '_'.
    labip_n_dafb = models.FloatField(null=True, blank=True,db_column='labip_n_dafb_persen')  # Field renamed to remove unsuitable characters. Field renamed because it ended with '_'.
    labip_o_adb = models.FloatField(null=True, blank=True,db_column='labip_o_adb_persen')  # Field renamed to remove unsuitable characters. Field renamed because it ended with '_'.
    labip_hgi_index = models.FloatField(null=True, blank=True)  # Field renamed to remove unsuitable characters. Field renamed because it ended with '_'.
    quicktest_gcv_arb_kcal_kg = models.FloatField(null=True, blank=True)  # Field renamed to remove unsuitable characters. Field renamed because it ended with '_'.
    quicktest_tm_arb = models.FloatField(null=True, blank=True,db_column='quicktest_tm_arb_persen')  # Field renamed to remove unsuitable characters. Field renamed because it ended with '_'.
    quicktest_ahs_content_arb = models.FloatField(null=True, blank=True,db_column='quicktest_ash_content_arb_persen')  # Field renamed to remove unsuitable characters. Field renamed because it ended with '_'.
    quicktest_total_sulphur_arb = models.FloatField(null=True, blank=True,db_column='quicktest_total_sulphur_arb_persen')  # Field renamed to remove unsuitable characters. Field renamed because it ended with '_'.



    class Meta:
        managed = False
        db_table = 'tm_grading_all'
# Create your models here.
