from django import forms
from .models import Rekap_shipment
from datetime import date
from . import settings

class FormRekap(forms.ModelForm):


    class Meta:
        model = Rekap_shipment
        fields = ['pltu', 'no', 'periode', 'bbo_id', 'shipment_code', 'voyage_code', 'voyage', 'pemasok', 'nama_pemasok', 'transhipment_shifting', 'sumber_tambang', 'loading_port', 'unloading_port', 'tb', 'bg', 'konfirmasi_rakor', 'time_arrival', 'status_laycan', 'batas_maks_not_accepted', 'nor_accepted_pltu', 'despatch_demurrage_keterangan','despatch_demurrage_biaya', 'berthed_time', 'commenced_unloading', 'start_cleaning', 'completed_unloading','cast_off', 'gangguan_jam_coal_handling_facility', 'gangguan_jam_kendala_eksternal', 'gangguan_jam_force_majeur', 'gangguan_jam_gangguan_pengurang_flowrate', 'volume_b_l','volume_ds','initial_draught_surve_start','initial_draught_surve_finish', 'lift_off_loader_start', 'lift_off_loader_finish', 'final_draught_survey_start', 'final_draught_survey_fiinish','port_stay_day', 'port_stay_hour', 'berthing_time', 'initial_draught', 'waiting_commenced', 'persiapan_bongkar', 'lift_off_loader', 'final_draught', 'waiting_cast_off', 'persiapan_cast_off', 'waktu_tunggu_sandar', 'waktu_bongkar', 'waktu_cleaning', 'flowrate_gross_mt_hours', 'flowrate_nett_mt_hours', 'status_umpire', 'roaloading_gcv_arb_kcal_kg', 'roaloading_tm_arb', 'roaloading_im_adb', 'roaloading_ash_content_arb', 'roaloading_ash_content_adb', 'roaloading_vm_adb', 'roaloading_fc_adb', 'roaloading_total_sulphur_arb', 'roaloading_total_sulphur_dafb', 'roaloading_hgi_index', 'coaloading_gcv_arb_kcal_kg', 'coaloading_gcv_adb_kcal_kg', 'coaloading_gcv_db_kcal_kg', 'coaloading_gcv_dafb_kcal_kg', 'coaloading_tm_arb', 'coaloading_im_adb', 'coaloading_ash_content_arb', 'coaloading_ash_content_adb', 'coaloading_ash_content_db', 'coaloading_vm_arb', 'coaloading_vm_adb', 'coaloading_vm_db', 'coaloading_vm_dafb', 'coaloading_fc_arb', 'coaloading_fc_adb', 'coaloading_fc_db', 'coaloading_fc_dafb', 'coaloading_total_sulphur_arb', 'coaloading_total_sulphur_adb', 'coaloading_total_sulphur_db', 'coaloading_total_sulphur_dafb', 'coaloading_hgi_index', 'coaloading_idt_reducing_c', 'coaunloading_gcv_arb_kcal_kg', 'coaunloading_gcv_adb_kcal_kg', 'coaunloading_gcv_db_kcal_kg', 'coaunloading_gcv_dafb_kcal_kg', 'coaunloading_tm_arb', 'coaunloading_im_adb', 'coaunloading_ash_content_arb', 'coaunloading_ash_content_adb', 'coaunloading_ash_content_db', 'coaunloading_vm_arb', 'coaunloading_vm_adb', 'coaunloading_vm_db', 'coaunloading_vm_dafb', 'coaunloading_fc_arb', 'coaunloading_fc_adb', 'coaunloading_fc_db', 'coaunloading_fc_dafb', 'coaunloading_total_sulphur_arb', 'coaunloading_total_sulphur_adb', 'coaunloading_total_sulphur_db', 'coaunloading_total_sulphur_dafb', 'coaunloading_c_adb', 'coaunloading_h_adb', 'coaunloading_n_adb', 'coaunloading_n_dafb', 'coaunloading_o_adb', 'coaunloading_hgi_index', 'coaunloading_sizing_70mm', 'coaunloading_sizing_50mm', 'coaunloading_sizing_32mm', 'coaunloading_sizing_2_38mm', 'coaunloading_ashanalysis_sio2', 'coaunloading_ashanalysis_ai2o3', 'coaunloading_ashanalysis_fe2o3', 'coaunloading_ashanalysis_cao', 'coaunloading_ashanalysis_mgo', 'coaunloading_ashanalysis_na2o', 'coaunloading_ashanalysis_k2o', 'coaunloading_ashanalysis_tio2', 'coaunloading_ashanalysis_so3', 'coaunloading_ashanalysis_mno2', 'coaunloading_ashanalysis_p2o5', 'coaunloading_slagging_factor', 'coaunloading_fouling_factor', 'coaunloading_idt_reducing_c', 'coaunloading_ht_reducing_c', 'coaunloading_ht_oxidizing_c', 'coaunloading_hg_arb', 'labip_gcv_arb_kcal_kg', 'labip_gcv_adb_kcal_kg', 'labip_gcv_db_kcal_kg', 'labip_gcv_dafb', 'labip_tm_arb', 'labip_im_adb', 'labip_ash_content_arb', 'labip_ash_content_adb', 'labip_ash_content_db', 'labip_vm_arb', 'labip_vm_adb', 'labip_vm_db', 'labip_vm_dafb', 'labip_fc_arb', 'labip_fc_adb', 'labip_fc_db', 'labip_fc_dafb', 'labip_total_sulphur_arb', 'labip_total_sulphur_adb', 'labip_total_sulphur_db', 'labip_total_sulphur_dafb', 'labip_c_adb', 'labip_h_adb', 'labip_n_adb', 'labip_n_dafb', 'labip_o_adb', 'labip_hgi_index', 'quicktest_gcv_arb_kcal_kg', 'quicktest_tm_arb', 'quicktest_ahs_content_arb', 'quicktest_total_sulphur_arb']

    konfirmasi_rakor = forms.DateTimeField(input_formats=settings.DATETIME_INPUT_FORMATS)
    time_arrival=forms.DateTimeField(input_formats=settings.DATETIME_INPUT_FORMATS)
    batas_maks_not_accepted=forms.DateTimeField(input_formats=settings.DATETIME_INPUT_FORMATS)
    nor_accepted_pltu=forms.DateTimeField(input_formats=settings.DATETIME_INPUT_FORMATS)
    berthed_time=forms.DateTimeField(input_formats=settings.DATETIME_INPUT_FORMATS)
    commenced_unloading=forms.DateTimeField(input_formats=settings.DATETIME_INPUT_FORMATS)
    start_cleaning=forms.DateTimeField(input_formats=settings.DATETIME_INPUT_FORMATS)
    completed_unloading=forms.DateTimeField(input_formats=settings.DATETIME_INPUT_FORMATS)
    cast_off=forms.DateTimeField(input_formats=settings.DATETIME_INPUT_FORMATS)
    initial_draught_surve_start=forms.DateTimeField(input_formats=settings.DATETIME_INPUT_FORMATS)
    initial_draught_surve_finish=forms.DateTimeField(input_formats=settings.DATETIME_INPUT_FORMATS)
    lift_off_loader_start=forms.DateTimeField(input_formats=settings.DATETIME_INPUT_FORMATS,required = False)
    lift_off_loader_finish=forms.DateTimeField(input_formats=settings.DATETIME_INPUT_FORMATS,required = False)
    final_draught_survey_start=forms.DateTimeField(input_formats=settings.DATETIME_INPUT_FORMATS)
    final_draught_survey_fiinish=forms.DateTimeField(input_formats=settings.DATETIME_INPUT_FORMATS)



class BlogForm(forms.Form):
    #python data type
    nama    = forms.CharField(max_length=10)
    alamat  = forms.CharField(required=False)
    nomer   = forms.IntegerField(required=False)
    disimal = forms.DecimalField(required=False)
    check   = forms.BooleanField(required=False)

    #String input
    email_field = forms.EmailField()
    regex       = forms.RegexField(regex=r'(P?<test>)')
    slug        = forms.SlugField()
    url_field   = forms.URLField()
    ip  = forms.GenericIPAddressField()

    Pilihan = (
        ('nilai1','pilihan1'),
        ('nilai2','pilihan2'),
        ('nilai3','pilihan3'),
    )

    choice_field = forms.ChoiceField(choices=Pilihan)
    multi_choice = forms.MultipleChoiceField(choices=Pilihan)
    multi_typed = forms.TypedMultipleChoiceField(choices=Pilihan)
    null_boolean = forms.NullBooleanField()

    #date time
    date_field = forms.DateTimeField()
    datetime_field  = forms.DateTimeField()
    duration_field = forms.DurationField()
    time_field = forms.TimeField()
    splitdatetime   = forms.SplitDateTimeField()

    file    = forms.FileField()
    image   = forms.ImageField()

class ContactForm(forms.Form):
    nama_lengkap = forms.CharField(
        label = 'Nama Lengkap',
        max_length = 20,
        widget = forms.TextInput(
            attrs={
                'class':'form-control',
                'placeholder':'masukan nama lengkap'
            }
        )
    )

    GENDER = {
        ('P','Pria'),
        ('W','Wanita'),
    }
    jenis_kelamin   = forms.ChoiceField(
        widget = forms.RadioSelect,
        choices=GENDER)
    YEAR = range(1945,2045,1)
    tanggal_lahir = forms.DateTimeField(
        widget = forms.SelectDateWidget(years=YEAR)
    )

    email_field = forms.EmailField(label="email")
    alamat = forms.CharField(
        widget = forms.Textarea,
        max_length = 100,
        required= False)

    agree = forms.BooleanField()
