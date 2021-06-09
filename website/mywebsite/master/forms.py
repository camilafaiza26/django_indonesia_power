from django import forms
from .models import Pemasok, PLTU, Sumbertambang, Waktu

class FormPemasok(forms.ModelForm):
    class Meta:
        model = Pemasok
        fields = ['nama_pemasok','jenis_bb','kontrak','ts']

class FormPLTU(forms.ModelForm):
    class Meta:
        model = PLTU
        fields = ['nama_pltu','lokasi_pltu','kode_pltu']

class FormSumberTambang(forms.ModelForm):
    class Meta:
        model = Sumbertambang
        fields = ['kode_sumber_tambang','nama_sumber_tambang']

class FormWaktu(forms.ModelForm):
    class Meta:
        model = Waktu
        fields = ['waktu_mulai','waktu_selesai','triwulan', 'tahun']
