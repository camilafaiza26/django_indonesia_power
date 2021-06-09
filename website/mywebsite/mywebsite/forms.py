from django import forms
from .models import *

class FormPerhitunganTertimbang(forms.ModelForm):
    class Meta:
        model = FactGradingPerhitunganTertimbang
        fields = ['pltu','pemasok','waktu','pt_gcv','pt_tm','pt_ts','pt_ash','pt_hgi','pt_idt','pt_mt']
