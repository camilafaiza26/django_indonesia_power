from django import forms
from .models import FactSolverKontrakPemasok, FactSolverRangePasokanDiinginkan, FactSolverRencana

class ValidasiMasterSolver(forms.ModelForm):
    class Meta:
        model = FactSolverKontrakPemasok
        fields = ['pltu', 'pemasok','nama_sumber_tambang', 'gcv_kcal_kg', 'jenis_bb', 'ts_persen', 'fob_rp_mt', 'moda', 'freight_cost_rp_mt', 'cif_rp_mt', 'cif_rp_cal', 'waktu']

class ValidasiRangePasokanSolver(forms.ModelForm):
    class Meta:
        model = FactSolverRangePasokanDiinginkan
        fields = ['pltu', 'pemasok','waktu_0','minimal_volume', 'minimal_kali_perbulan', 'minimal_total_perbulan', 'maksimal_volume', 'maksimal_kali_perbulan', 'maksimal_total_perbulan']

class ValidasiRencanaSolver(forms.ModelForm):
    class Meta:
        model = FactSolverRencana
        fields = ['pltu','waktu','persentase_rencana_lrc_persen','persentase_rencana_mrc_persen', 'input_bb_mt', 'input_nilai_kalor_kcal_kg', 'input_total_sulphur']

