# This is an auto-generated Django model module.
# You'll have to do the following manually to clean this up:
#   * Rearrange models' order
#   * Make sure each model has one field with primary_key=True
#   * Make sure each ForeignKey and OneToOneField has `on_delete` set to the desired behavior
#   * Remove `managed = False` lines if you wish to allow Django to create, modify, and delete the table
# Feel free to rename the models, but don't rename db_table values or field names.
from django.db import models


class AuthGroup(models.Model):
    name = models.CharField(unique=True, max_length=150)

    class Meta:
        managed = False
        db_table = 'auth_group'


class AuthGroupPermissions(models.Model):
    group = models.ForeignKey(AuthGroup, models.DO_NOTHING)
    permission = models.ForeignKey('AuthPermission', models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'auth_group_permissions'
        unique_together = (('group', 'permission'),)


class AuthPermission(models.Model):
    name = models.CharField(max_length=255)
    content_type = models.ForeignKey('DjangoContentType', models.DO_NOTHING)
    codename = models.CharField(max_length=100)

    class Meta:
        managed = False
        db_table = 'auth_permission'
        unique_together = (('content_type', 'codename'),)


class AuthUser(models.Model):
    password = models.CharField(max_length=128)
    last_login = models.DateTimeField(blank=True, null=True)
    is_superuser = models.IntegerField()
    username = models.CharField(unique=True, max_length=150)
    first_name = models.CharField(max_length=150)
    last_name = models.CharField(max_length=150)
    email = models.CharField(max_length=254)
    is_staff = models.IntegerField()
    is_active = models.IntegerField()
    date_joined = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'auth_user'


class AuthUserGroups(models.Model):
    user = models.ForeignKey(AuthUser, models.DO_NOTHING)
    group = models.ForeignKey(AuthGroup, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'auth_user_groups'
        unique_together = (('user', 'group'),)


class AuthUserUserPermissions(models.Model):
    user = models.ForeignKey(AuthUser, models.DO_NOTHING)
    permission = models.ForeignKey(AuthPermission, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'auth_user_user_permissions'
        unique_together = (('user', 'permission'),)


class DimPemasok(models.Model):
    id_pemasok = models.AutoField(primary_key=True)
    nama_pemasok = models.CharField(max_length=100)
    jenis_bb = models.CharField(max_length=3)

    class Meta:
        managed = False
        db_table = 'dim_pemasok'


class DimPltu(models.Model):
    id_pltu = models.AutoField(primary_key=True)
    nama_pltu = models.CharField(max_length=50)
    lokasi_pltu = models.CharField(max_length=100)

    class Meta:
        managed = False
        db_table = 'dim_pltu'


class DimSumbertambang(models.Model):
    id_sumber_tambang = models.CharField(max_length=100)
    nama_sumber_tambang = models.CharField(max_length=500)

    class Meta:
        managed = False
        db_table = 'dim_sumbertambang'


class DimWaktu(models.Model):
    id_waktu = models.IntegerField(primary_key=True)
    waktu_mulai = models.DateField()
    waktu_selesai = models.DateField()
    triwulan = models.CharField(max_length=3)
    tahun = models.TextField()  # This field type is a guess.

    class Meta:
        managed = False
        db_table = 'dim_waktu'


class DjangoAdminLog(models.Model):
    action_time = models.DateTimeField()
    object_id = models.TextField(blank=True, null=True)
    object_repr = models.CharField(max_length=200)
    action_flag = models.PositiveSmallIntegerField()
    change_message = models.TextField()
    content_type = models.ForeignKey('DjangoContentType', models.DO_NOTHING, blank=True, null=True)
    user = models.ForeignKey(AuthUser, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'django_admin_log'


class DjangoContentType(models.Model):
    app_label = models.CharField(max_length=100)
    model = models.CharField(max_length=100)

    class Meta:
        managed = False
        db_table = 'django_content_type'
        unique_together = (('app_label', 'model'),)


class DjangoMigrations(models.Model):
    app = models.CharField(max_length=255)
    name = models.CharField(max_length=255)
    applied = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'django_migrations'


class FactGradingRekapanPenilaianPemasok(models.Model):
    id_rekapanpenilaian = models.IntegerField()
    id_pltu = models.IntegerField()
    id_pemasok = models.IntegerField()
    id_waktu = models.IntegerField()
    p1_gcv_typical = models.FloatField()
    p1_gcv_penolakan = models.FloatField()
    p1_tm_typical = models.FloatField()
    p1_tm_penolakan = models.FloatField()
    p1_ts_typical = models.FloatField()
    p1_ts_penolakan = models.FloatField()
    p1_ash_typical = models.FloatField()
    p1_ash_penolakan = models.FloatField()
    p1_hgi_typical = models.FloatField()
    p1_hgi_penolakan1 = models.FloatField()
    p1_hgi_penolakan2 = models.FloatField()
    p1_idt_typical = models.FloatField()
    p1_idt_penolakan = models.FloatField()
    p1_gcv_realisasi = models.FloatField()
    p1_tm_realisasi = models.FloatField()
    p1_ts_realisasi = models.FloatField()
    p1_ash_realisasi = models.FloatField()
    p1_hgi_realisasi = models.FloatField()
    p1_idt_realisasi = models.FloatField()
    p1_gcv_pengurang = models.FloatField()
    p1_tm_pengurang = models.FloatField()
    p1_ts_pengurang = models.FloatField()
    p1_ash_pengurang = models.FloatField()
    p1_hgi_pengurang = models.FloatField()
    p1_idt_pengurang = models.FloatField()
    p2_konfirmasi = models.FloatField()
    p2_realisasi = models.FloatField()
    p2_persentase_pasokan = models.FloatField()
    p2_pengurang_pasokan = models.FloatField()
    p3_jmlh_shipment_tertolak = models.FloatField()
    p3_persentase_penolakan = models.FloatField()
    p3_pengurang_penolakan = models.FloatField()
    nilai_akhir = models.FloatField()
    klasifikasi = models.CharField(max_length=50)

    class Meta:
        managed = False
        db_table = 'fact_grading_rekapan_penilaian_pemasok'


class FactSolverKontrakPemasok(models.Model):
    id_kontrakpemasok = models.IntegerField()
    id_pltu = models.IntegerField()
    id_pemasok = models.IntegerField()
    id_sumbertambang = models.CharField(max_length=100)
    gcv_kcal_kg_field = models.IntegerField(db_column='gcv(kcal/kg)')  # Field renamed to remove unsuitable characters. Field renamed because it ended with '_'.
    jenis_bb = models.CharField(max_length=3)
    ts_field = models.FloatField(db_column='ts(%)')  # Field renamed to remove unsuitable characters. Field renamed because it ended with '_'.
    fob_rp_mt_field = models.FloatField(db_column='fob(rp/mt)')  # Field renamed to remove unsuitable characters. Field renamed because it ended with '_'.
    moda = models.CharField(max_length=30)
    freight_cost_rp_mt_field = models.FloatField(db_column='freight_cost(rp/mt)')  # Field renamed to remove unsuitable characters. Field renamed because it ended with '_'.
    cif_rp_mt_field = models.FloatField(db_column='cif(rp/mt)')  # Field renamed to remove unsuitable characters. Field renamed because it ended with '_'.
    cif_rp_cal_field = models.FloatField(db_column='cif(rp/cal)')  # Field renamed to remove unsuitable characters. Field renamed because it ended with '_'.
    id_waktu = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'fact_solver_kontrak pemasok'


class FactSolverResumeHasilOptimasi(models.Model):
    id_rhos = models.IntegerField()
    id_pltu = models.IntegerField()
    id_pemasok = models.IntegerField()
    id_waktu = models.IntegerField()
    jenis_bb = models.CharField(max_length=3)
    rhos_volume = models.FloatField()
    rhos_kalori_kcal_field = models.FloatField(db_column='rhos_kalori(kcal)')  # Field renamed to remove unsuitable characters. Field renamed because it ended with '_'.
    rhos_ts_field = models.FloatField(db_column='rhos_ts(%)')  # Field renamed to remove unsuitable characters. Field renamed because it ended with '_'.
    rhos_harga_rp_cal_field = models.FloatField(db_column='rhos_harga(rp/cal)')  # Field renamed to remove unsuitable characters. Field renamed because it ended with '_'.

    class Meta:
        managed = False
        db_table = 'fact_solver_resume_hasil_optimasi'


class GradingSupplier(models.Model):
    id_grading = models.AutoField(primary_key=True)
    nama_pltu = models.CharField(max_length=100)
    nama_pemasok = models.CharField(max_length=100)
    gcv_realisasi = models.FloatField()
    tm_realisasi = models.FloatField()
    ts_realisasi = models.FloatField()
    ash_realisasi = models.FloatField()
    hgi_realisasi = models.FloatField()
    idt_realisasi = models.FloatField()
    pengurang_gcv = models.FloatField()
    pengurang_tm = models.FloatField()
    pengurang_ts = models.FloatField()
    pengurang_ash = models.FloatField()
    pengurang_hgi = models.FloatField()
    pengurang_idt = models.FloatField()
    persentase_realisasi = models.FloatField()
    pengurang_pasokan = models.FloatField()
    persentase_penolakan = models.FloatField()
    pengurang_batas_penolakan = models.FloatField()
    nilai_akhir = models.FloatField()
    klasifikasi = models.CharField(max_length=100, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'grading_supplier'


class TmGrading(models.Model):
    id_tm = models.IntegerField()
    no = models.IntegerField()
    periode = models.DateField()
    bbo_id = models.IntegerField()
    shipment_code = models.IntegerField()
    voyage_code = models.IntegerField()
    voyage = models.IntegerField()
    pemasok = models.CharField(max_length=10)
    transhipment_shifting = models.IntegerField(db_column='transhipment/shifting')  # Field renamed to remove unsuitable characters.
    sumber_tambang = models.CharField(max_length=50)
    loading_port = models.CharField(max_length=50)
    unloading_port = models.CharField(max_length=2)
    tb = models.CharField(max_length=30)
    bg = models.CharField(max_length=30)
    konfirmasi_rakor = models.DateTimeField()
    time_arrival = models.DateTimeField()
    status_laycan = models.CharField(max_length=7)
    batas_maks_not_accepted = models.DateTimeField()
    nor_accepted_pltu = models.DateTimeField()
    despatch_demurrage_keterangan = models.CharField(db_column='despatch/demurrage_keterangan', max_length=30)  # Field renamed to remove unsuitable characters.
    despatch_demurrage_biaya = models.FloatField(db_column='despatch/demurrage_biaya')  # Field renamed to remove unsuitable characters.
    berthed_time = models.DateTimeField()
    commenced_unloading = models.DateTimeField()
    start_cleaning = models.DateTimeField()
    completed_unloading = models.DateTimeField()
    cast_off = models.DateTimeField()
    gangguan_jam_coal_handling_facility = models.IntegerField(db_column='gangguan(jam)_coal_handling_facility')  # Field renamed to remove unsuitable characters.
    gangguan_jam_kendala_eksternal = models.IntegerField(db_column='gangguan(jam)_kendala_eksternal')  # Field renamed to remove unsuitable characters.
    gangguan_jam_force_majeur = models.IntegerField(db_column='gangguan(jam)_force_majeur')  # Field renamed to remove unsuitable characters.
    gangguan_jam_gangguan_pengurang_flowrate = models.IntegerField(db_column='gangguan(jam)_gangguan_pengurang_flowrate')  # Field renamed to remove unsuitable characters.
    volume_b_l = models.FloatField(db_column='volume_b/l')  # Field renamed to remove unsuitable characters.
    volume_ds = models.FloatField()
    initial_draught_surve_start = models.DateTimeField()
    initial_draught_surve_finish = models.DateTimeField()
    lift_off_loader_start = models.DateTimeField()
    lift_off_loader_finish = models.DateTimeField()
    final_draught_survey_start = models.DateTimeField()
    final_draught_survey_fiinish = models.DateTimeField()
    port_stay_day = models.IntegerField()
    port_stay_hour = models.IntegerField()
    berthing_time = models.IntegerField()
    initial_draught = models.IntegerField()
    waiting_commenced = models.IntegerField()
    persiapan_bongkar = models.IntegerField()
    lift_off_loader = models.IntegerField()
    final_draught = models.IntegerField()
    waiting_cast_off = models.IntegerField()
    persiapan_cast_off = models.IntegerField()
    waktu_tunggu_sandar = models.IntegerField()
    waktu_bongkar = models.IntegerField()
    waktu_cleaning = models.IntegerField()
    flowrate_gross_mt_hours_field = models.IntegerField(db_column='flowrate_gross(mt/hours)')  # Field renamed to remove unsuitable characters. Field renamed because it ended with '_'.
    flowrate_nett_mt_hours_field = models.IntegerField(db_column='flowrate_nett(mt/hours)')  # Field renamed to remove unsuitable characters. Field renamed because it ended with '_'.
    status_umpire = models.CharField(max_length=5)
    roaloading_gcv_arb_kcal_kg_field = models.FloatField(db_column='roaloading_gcv_arb(kcal/kg)')  # Field renamed to remove unsuitable characters. Field renamed because it ended with '_'.
    roaloading_tm_arb_field = models.FloatField(db_column='roaloading_tm_arb(%)')  # Field renamed to remove unsuitable characters. Field renamed because it ended with '_'.
    roaloading_im_adb_field = models.FloatField(db_column='roaloading_im_adb(%)')  # Field renamed to remove unsuitable characters. Field renamed because it ended with '_'.
    roaloading_ash_content_arb_field = models.FloatField(db_column='roaloading_ash_content_arb(%)')  # Field renamed to remove unsuitable characters. Field renamed because it ended with '_'.
    roaloading_ash_content_adb_field = models.FloatField(db_column='roaloading_ash_content_adb(%)')  # Field renamed to remove unsuitable characters. Field renamed because it ended with '_'.
    roaloading_vm_adb_field = models.FloatField(db_column='roaloading_vm_adb(%)')  # Field renamed to remove unsuitable characters. Field renamed because it ended with '_'.
    roaloading_fc_adb_field = models.FloatField(db_column='roaloading_fc_adb(%)')  # Field renamed to remove unsuitable characters. Field renamed because it ended with '_'.
    roaloading_total_sulphur_arb_field = models.FloatField(db_column='roaloading_total_sulphur_arb(%)')  # Field renamed to remove unsuitable characters. Field renamed because it ended with '_'.
    roaloading_total_sulphur_dafb_field = models.FloatField(db_column='roaloading_total_sulphur_dafb(%)')  # Field renamed to remove unsuitable characters. Field renamed because it ended with '_'.
    roaloading_hgi_index_field = models.FloatField(db_column='roaloading_hgi(index)')  # Field renamed to remove unsuitable characters. Field renamed because it ended with '_'.
    coaloading_gcv_arb_kcal_kg_field = models.FloatField(db_column='coaloading_gcv_arb(kcal/kg)')  # Field renamed to remove unsuitable characters. Field renamed because it ended with '_'.
    coaloading_gcv_adb_kcal_kg_field = models.FloatField(db_column='coaloading_gcv_adb(kcal/kg)')  # Field renamed to remove unsuitable characters. Field renamed because it ended with '_'.
    coaloading_gcv_db_kcal_kg_field = models.FloatField(db_column='coaloading_gcv_db(kcal/kg)')  # Field renamed to remove unsuitable characters. Field renamed because it ended with '_'.
    coaloading_gcv_dafb_kcal_kg_field = models.IntegerField(db_column='coaloading_gcv_dafb(kcal/kg)')  # Field renamed to remove unsuitable characters. Field renamed because it ended with '_'.
    coaloading_tm_arb_field = models.FloatField(db_column='coaloading_tm_arb(%)')  # Field renamed to remove unsuitable characters. Field renamed because it ended with '_'.
    coaloading_im_adb_field = models.FloatField(db_column='coaloading_im_adb(%)')  # Field renamed to remove unsuitable characters. Field renamed because it ended with '_'.
    coaloading_ash_content_arb_field = models.FloatField(db_column='coaloading_ash_content_arb(%)')  # Field renamed to remove unsuitable characters. Field renamed because it ended with '_'.
    coaloading_ash_content_adb_field = models.FloatField(db_column='coaloading_ash_content_adb(%)')  # Field renamed to remove unsuitable characters. Field renamed because it ended with '_'.
    coaloading_ash_content_db_field = models.FloatField(db_column='coaloading_ash_content_db(%)')  # Field renamed to remove unsuitable characters. Field renamed because it ended with '_'.
    coaloading_vm_arb_field = models.FloatField(db_column='coaloading_vm_arb(%)')  # Field renamed to remove unsuitable characters. Field renamed because it ended with '_'.
    coaloading_vm_adb_field = models.FloatField(db_column='coaloading_vm_adb(%)')  # Field renamed to remove unsuitable characters. Field renamed because it ended with '_'.
    coaloading_vm_db_field = models.FloatField(db_column='coaloading_vm_db(%)')  # Field renamed to remove unsuitable characters. Field renamed because it ended with '_'.
    coaloading_vm_dafb_field = models.FloatField(db_column='coaloading_vm_dafb(%)')  # Field renamed to remove unsuitable characters. Field renamed because it ended with '_'.
    coaloading_fc_arb_field = models.FloatField(db_column='coaloading_fc_arb(%)')  # Field renamed to remove unsuitable characters. Field renamed because it ended with '_'.
    coaloading_fc_adb_field = models.FloatField(db_column='coaloading_fc_adb(%)')  # Field renamed to remove unsuitable characters. Field renamed because it ended with '_'.
    coaloading_fc_db_field = models.FloatField(db_column='coaloading_fc_db(%)')  # Field renamed to remove unsuitable characters. Field renamed because it ended with '_'.
    coaloading_fc_dafb_field = models.FloatField(db_column='coaloading_fc_dafb(%)')  # Field renamed to remove unsuitable characters. Field renamed because it ended with '_'.
    coaloading_total_sulphur_arb_field = models.FloatField(db_column='coaloading_total_sulphur_arb(%)')  # Field renamed to remove unsuitable characters. Field renamed because it ended with '_'.
    coaloading_total_sulphur_adb_field = models.FloatField(db_column='coaloading_total_sulphur_adb(%)')  # Field renamed to remove unsuitable characters. Field renamed because it ended with '_'.
    coaloading_total_sulphur_db_field = models.FloatField(db_column='coaloading_total_sulphur_db(%)')  # Field renamed to remove unsuitable characters. Field renamed because it ended with '_'.
    coaloading_total_sulphur_dafb_field = models.FloatField(db_column='coaloading_total_sulphur_dafb(%)')  # Field renamed to remove unsuitable characters. Field renamed because it ended with '_'.
    coaloading_hgi_index_field = models.FloatField(db_column='coaloading_hgi(index)')  # Field renamed to remove unsuitable characters. Field renamed because it ended with '_'.
    coaloading_idt_reducing_c_field = models.FloatField(db_column="coaloading_idt_reducing('c)")  # Field renamed to remove unsuitable characters. Field renamed because it ended with '_'.
    coaunloading_gcv_arb_kcal_kg_field = models.FloatField(db_column='coaunloading_gcv_arb(kcal/kg)')  # Field renamed to remove unsuitable characters. Field renamed because it ended with '_'.
    coaunloading_gcv_adb_kcal_kg_field = models.FloatField(db_column='coaunloading_gcv_adb(kcal/kg)')  # Field renamed to remove unsuitable characters. Field renamed because it ended with '_'.
    coaunloading_gcv_db_kcal_kg_field = models.FloatField(db_column='coaunloading_gcv_db(kcal/kg)')  # Field renamed to remove unsuitable characters. Field renamed because it ended with '_'.
    coaunloading_gcv_dafb_kcal_kg_field = models.FloatField(db_column='coaunloading_gcv_dafb(kcal/kg)')  # Field renamed to remove unsuitable characters. Field renamed because it ended with '_'.
    coaunloading_tm_arb_field = models.FloatField(db_column='coaunloading_tm_arb(%)')  # Field renamed to remove unsuitable characters. Field renamed because it ended with '_'.
    coaunloading_im_adb_field = models.FloatField(db_column='coaunloading_im_adb(%)')  # Field renamed to remove unsuitable characters. Field renamed because it ended with '_'.
    coaunloading_ash_content_arb_field = models.FloatField(db_column='coaunloading_ash_content_arb(%)')  # Field renamed to remove unsuitable characters. Field renamed because it ended with '_'.
    coaunloading_ash_content_adb_field = models.FloatField(db_column='coaunloading_ash_content_adb(%)')  # Field renamed to remove unsuitable characters. Field renamed because it ended with '_'.
    coaunloading_ash_content_db_field = models.FloatField(db_column='coaunloading_ash_content_db(%)')  # Field renamed to remove unsuitable characters. Field renamed because it ended with '_'.
    coaunloading_vm_arb_field = models.FloatField(db_column='coaunloading_vm_arb(%)')  # Field renamed to remove unsuitable characters. Field renamed because it ended with '_'.
    coaunloading_vm_adb_field = models.FloatField(db_column='coaunloading_vm_adb(%)')  # Field renamed to remove unsuitable characters. Field renamed because it ended with '_'.
    coaunloading_vm_db_field = models.FloatField(db_column='coaunloading_vm_db(%)')  # Field renamed to remove unsuitable characters. Field renamed because it ended with '_'.
    coaunloading_vm_dafb_field = models.FloatField(db_column='coaunloading_vm_dafb(%)')  # Field renamed to remove unsuitable characters. Field renamed because it ended with '_'.
    coaunloading_fc_arb_field = models.FloatField(db_column='coaunloading_fc_arb(%)')  # Field renamed to remove unsuitable characters. Field renamed because it ended with '_'.
    coaunloading_fc_adb_field = models.FloatField(db_column='coaunloading_fc_adb(%)')  # Field renamed to remove unsuitable characters. Field renamed because it ended with '_'.
    coaunloading_fc_db_field = models.FloatField(db_column='coaunloading_fc_db(%)')  # Field renamed to remove unsuitable characters. Field renamed because it ended with '_'.
    coaunloading_fc_dafb_field = models.FloatField(db_column='coaunloading_fc_dafb(%)')  # Field renamed to remove unsuitable characters. Field renamed because it ended with '_'.
    coaunloading_total_sulphur_arb_field = models.FloatField(db_column='coaunloading_total_sulphur_arb(%)')  # Field renamed to remove unsuitable characters. Field renamed because it ended with '_'.
    coaunloading_total_sulphur_adb_field = models.FloatField(db_column='coaunloading_total_sulphur_adb(%)')  # Field renamed to remove unsuitable characters. Field renamed because it ended with '_'.
    coaunloading_total_sulphur_db_field = models.FloatField(db_column='coaunloading_total_sulphur_db(%)')  # Field renamed to remove unsuitable characters. Field renamed because it ended with '_'.
    coaunloading_total_sulphur_dafb_field = models.FloatField(db_column='coaunloading_total_sulphur_dafb(%)')  # Field renamed to remove unsuitable characters. Field renamed because it ended with '_'.
    coaunloading_c_adb_field = models.FloatField(db_column='coaunloading_c_adb(%)')  # Field renamed to remove unsuitable characters. Field renamed because it ended with '_'.
    coaunloading_h_adb_field = models.FloatField(db_column='coaunloading_h_adb(%)')  # Field renamed to remove unsuitable characters. Field renamed because it ended with '_'.
    coaunloading_n_adb_field = models.FloatField(db_column='coaunloading_n_adb(%)')  # Field renamed to remove unsuitable characters. Field renamed because it ended with '_'.
    coaunloading_n_dafb_field = models.FloatField(db_column='coaunloading_n_dafb(%)')  # Field renamed to remove unsuitable characters. Field renamed because it ended with '_'.
    coaunloading_o_adb_field = models.FloatField(db_column='coaunloading_o_adb(%)')  # Field renamed to remove unsuitable characters. Field renamed because it ended with '_'.
    coaunloading_hgi_index_field = models.FloatField(db_column='coaunloading_hgi(index)')  # Field renamed to remove unsuitable characters. Field renamed because it ended with '_'.
    coaunloading_sizing_70mm = models.FloatField(db_column='coaunloading_sizing(%)_70mm')  # Field renamed to remove unsuitable characters.
    coaunloading_sizing_50mm = models.FloatField(db_column='coaunloading_sizing(%)_50mm')  # Field renamed to remove unsuitable characters.
    coaunloading_sizing_32mm = models.FloatField(db_column='coaunloading_sizing(%)_32mm')  # Field renamed to remove unsuitable characters.
    coaunloading_sizing_2_38mm = models.FloatField(db_column='coaunloading_sizing(%)_2,38mm')  # Field renamed to remove unsuitable characters.
    coaunloading_ashanalysis_sio2 = models.FloatField(db_column='coaunloading_ashanalysis(%)_SiO2')  # Field name made lowercase. Field renamed to remove unsuitable characters.
    coaunloading_ashanalysis_ai2o3 = models.FloatField(db_column='coaunloading_ashanalysis(%)_AI2O3')  # Field name made lowercase. Field renamed to remove unsuitable characters.
    coaunloading_ashanalysis_fe2o3 = models.FloatField(db_column='coaunloading_ashanalysis(%)_FE2O3')  # Field name made lowercase. Field renamed to remove unsuitable characters.
    coaunloading_ashanalysis_cao = models.FloatField(db_column='coaunloading_ashanalysis(%)_CaO')  # Field name made lowercase. Field renamed to remove unsuitable characters.
    coaunloading_ashanalysis_mgo = models.FloatField(db_column='coaunloading_ashanalysis(%)_MgO')  # Field name made lowercase. Field renamed to remove unsuitable characters.
    coaunloading_ashanalysis_na2o = models.FloatField(db_column='coaunloading_ashanalysis(%)_Na2O')  # Field name made lowercase. Field renamed to remove unsuitable characters.
    coaunloading_ashanalysis_k2o = models.FloatField(db_column='coaunloading_ashanalysis(%)_K2O')  # Field name made lowercase. Field renamed to remove unsuitable characters.
    coaunloading_ashanalysis_tio2 = models.FloatField(db_column='coaunloading_ashanalysis(%)_TiO2')  # Field name made lowercase. Field renamed to remove unsuitable characters.
    coaunloading_ashanalysis_so3 = models.FloatField(db_column='coaunloading_ashanalysis(%)_SO3')  # Field name made lowercase. Field renamed to remove unsuitable characters.
    coaunloading_ashanalysis_mno2 = models.FloatField(db_column='coaunloading_ashanalysis(%)_MnO2')  # Field name made lowercase. Field renamed to remove unsuitable characters.
    coaunloading_ashanalysis_p2o5 = models.FloatField(db_column='coaunloading_ashanalysis(%)_P2O5')  # Field name made lowercase. Field renamed to remove unsuitable characters.
    coaunloading_slagging_factor = models.FloatField()
    coaunloading_fouling_factor = models.FloatField()
    coaunloading_idt_reducing_c_field = models.FloatField(db_column="coaunloading_idt_reducing('C)")  # Field name made lowercase. Field renamed to remove unsuitable characters. Field renamed because it ended with '_'.
    coaunloading_ht_reducing_c_field = models.FloatField(db_column="coaunloading_ht_reducing('C)")  # Field name made lowercase. Field renamed to remove unsuitable characters. Field renamed because it ended with '_'.
    coaunloading_ht_oxidizing_c_field = models.FloatField(db_column="coaunloading_ht_oxidizing('C)")  # Field name made lowercase. Field renamed to remove unsuitable characters. Field renamed because it ended with '_'.
    coaunloading_hg_arb = models.FloatField()
    labip_gcv_arb_kcal_kg_field = models.FloatField(db_column='labip_gcv_arb(kcal/kg)')  # Field renamed to remove unsuitable characters. Field renamed because it ended with '_'.
    labip_gcv_adb_kcal_kg_field = models.FloatField(db_column='labip_gcv_adb(kcal/kg)')  # Field renamed to remove unsuitable characters. Field renamed because it ended with '_'.
    labip_gcv_db_kcal_kg_field = models.FloatField(db_column='labip_gcv_db(kcal/kg)')  # Field renamed to remove unsuitable characters. Field renamed because it ended with '_'.
    labip_gcv_dafb_field = models.FloatField(db_column='labip_gcv_dafb(%)')  # Field renamed to remove unsuitable characters. Field renamed because it ended with '_'.
    labip_tm_arb_field = models.FloatField(db_column='labip_tm_arb(%)')  # Field renamed to remove unsuitable characters. Field renamed because it ended with '_'.
    labip_im_adb_field = models.FloatField(db_column='labip_im_adb(%)')  # Field renamed to remove unsuitable characters. Field renamed because it ended with '_'.
    labip_ash_content_arb_field = models.FloatField(db_column='labip_ash_content_arb(%)')  # Field renamed to remove unsuitable characters. Field renamed because it ended with '_'.
    labip_ash_content_adb_field = models.FloatField(db_column='labip_ash_content_adb(%)')  # Field renamed to remove unsuitable characters. Field renamed because it ended with '_'.
    labip_ash_content_db_field = models.FloatField(db_column='labip_ash_content_db(%)')  # Field renamed to remove unsuitable characters. Field renamed because it ended with '_'.
    labip_vm_arb_field = models.FloatField(db_column='labip_vm_arb(%)')  # Field renamed to remove unsuitable characters. Field renamed because it ended with '_'.
    labip_vm_adb_field = models.FloatField(db_column='labip_vm_adb(%)')  # Field renamed to remove unsuitable characters. Field renamed because it ended with '_'.
    labip_vm_db_field = models.FloatField(db_column='labip_vm_db(%)')  # Field renamed to remove unsuitable characters. Field renamed because it ended with '_'.
    labip_vm_dafb_field = models.FloatField(db_column='labip_vm_dafb(%)')  # Field renamed to remove unsuitable characters. Field renamed because it ended with '_'.
    labip_fc_arb_field = models.FloatField(db_column='labip_fc_arb(%)')  # Field renamed to remove unsuitable characters. Field renamed because it ended with '_'.
    labip_fc_adb_field = models.FloatField(db_column='labip_fc_adb(%)')  # Field renamed to remove unsuitable characters. Field renamed because it ended with '_'.
    labip_fc_db_field = models.FloatField(db_column='labip_fc_db(%)')  # Field renamed to remove unsuitable characters. Field renamed because it ended with '_'.
    labip_fc_dafb_field = models.FloatField(db_column='labip_fc_dafb(%)')  # Field renamed to remove unsuitable characters. Field renamed because it ended with '_'.
    labip_total_sulphur_arb_field = models.FloatField(db_column='labip_total_sulphur_arb(%)')  # Field renamed to remove unsuitable characters. Field renamed because it ended with '_'.
    labip_total_sulphur_adb_field = models.FloatField(db_column='labip_total_sulphur_adb(%)')  # Field renamed to remove unsuitable characters. Field renamed because it ended with '_'.
    labip_total_sulphur_db_field = models.FloatField(db_column='labip_total_sulphur_db(%)')  # Field renamed to remove unsuitable characters. Field renamed because it ended with '_'.
    labip_total_sulphur_dafb_field = models.FloatField(db_column='labip_total_sulphur_dafb(%)')  # Field renamed to remove unsuitable characters. Field renamed because it ended with '_'.
    labip_c_adb_field = models.FloatField(db_column='labip_c_adb(%)')  # Field renamed to remove unsuitable characters. Field renamed because it ended with '_'.
    labip_h_adb_field = models.FloatField(db_column='labip_h_adb(%)')  # Field renamed to remove unsuitable characters. Field renamed because it ended with '_'.
    labip_n_adb_field = models.FloatField(db_column='labip_n_adb(%)')  # Field renamed to remove unsuitable characters. Field renamed because it ended with '_'.
    labip_n_dafb_field = models.FloatField(db_column='labip_n_dafb(%)')  # Field renamed to remove unsuitable characters. Field renamed because it ended with '_'.
    labip_o_adb_field = models.FloatField(db_column='labip_o_adb(%)')  # Field renamed to remove unsuitable characters. Field renamed because it ended with '_'.
    labip_hgi_index_field = models.FloatField(db_column='labip_hgi(index)')  # Field renamed to remove unsuitable characters. Field renamed because it ended with '_'.
    quicktest_gcv_arb_kcal_kg_field = models.FloatField(db_column='quicktest_gcv_arb(kcal/kg)')  # Field renamed to remove unsuitable characters. Field renamed because it ended with '_'.
    quicktest_tm_arb_field = models.FloatField(db_column='quicktest_tm_arb(%)')  # Field renamed to remove unsuitable characters. Field renamed because it ended with '_'.
    quicktest_ahs_content_arb_field = models.FloatField(db_column='quicktest_ahs_content_arb(%)')  # Field renamed to remove unsuitable characters. Field renamed because it ended with '_'.
    quicktest_total_sulphur_arb_field = models.FloatField(db_column='quicktest_total_sulphur_arb(%)')  # Field renamed to remove unsuitable characters. Field renamed because it ended with '_'.

    class Meta:
        managed = False
        db_table = 'tm_grading'
