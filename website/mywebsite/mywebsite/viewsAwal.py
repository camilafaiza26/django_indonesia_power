from django.shortcuts import render, redirect, get_object_or_404
from django.http import HttpResponse, HttpResponseRedirect
from django.contrib.auth.decorators import login_required
from django.contrib.auth import authenticate, login, logout
from .models import *
from .forms import *
from master.models import *
from master.forms import *
from blog.models import *
from blog.forms import *
import datetime
import urllib

#method login
def loginView(request):
	context = {
		'page_title':'LOGIN',
	}
	user = None

	if request.method == "GET":
		if request.user.is_authenticated:
			# logika untuk user
			return redirect('index')
		else:
			# logika untuk anonymous
			return render(request, 'login.html', context)


	if request.method == "POST":

		username_login = request.POST['username']
		password_login = request.POST['password']

		user = authenticate(request, username=username_login, password=password_login)

		if user is not None:
			login(request, user)
			return redirect('index')
		else:
			return redirect('login')


@login_required
def logoutView(request):
	context = {
		'page_title':'logout'
	}

	if request.method == "POST":
		if request.POST["logout"] == "Submit":
			logout(request)

		return redirect('index')


	return render(request, 'logout.html', context)


#method view
def index(request):
	if request.user.is_authenticated:
		if 'logout' in request.POST:
			logoutnya = request.POST['logout']
			if logoutnya == "":
				logout(request)
				return redirect('login')
		context = {
		'judul':'Dashboard Report Batubara',
		}
		return render(request,'index.html', context)
	else:
		return redirect('login')

def grading(request):
	if request.user.is_authenticated:
		if 'logout' in request.POST:
			logoutnya = request.POST['logout']
			if logoutnya == "":
				logout(request)
				return redirect('login')

		if 'caripltu' in request.POST:
			caripltu = request.POST['caripltu']
			nama_pltu = request.POST['nama_pltu']
			triwulan =  request.POST['triwulan']
			tahun = request.POST['tahun']
			if caripltu != None:
				pltu = PLTU.objects.values('pltu_id').filter(nama_pltu=nama_pltu)
				for idpltu in pltu:
				    print(idpltu['pltu_id'])
				waktu = Waktu.objects.values('waktu_id').filter(triwulan=triwulan,tahun=tahun)
				for idwaktu in waktu:
				    print(idwaktu['waktu_id'])

				hasil = FactGradingRekapanPenilaianPemasok.objects.filter(pltu=idpltu['pltu_id'],waktu=idwaktu['waktu_id']).order_by('waktu_id','-nilai_akhir')
				hasil2 = PLTU.objects.all()
				context = {
				'judul':'Penilaian Pemasok Batu Bara',
				'data':hasil,
				'data2':hasil2,
				}
				return render(request,'grading.html', context)

		if 'buatgrading' in request.POST:
			buatgrading = request.POST['buatgrading']
			nama_pltu = request.POST['nama_pltu']
			triwulan =  request.POST['triwulan']
			tahun = request.POST['tahun']
			if buatgrading != None:
				waktu = Waktu.objects.values('waktu_id','waktu_mulai','waktu_selesai').filter(triwulan=triwulan,tahun=tahun)
				for mulai in waktu:
				    waktu_mulai=mulai['waktu_mulai']
				for selesai in waktu:
				    waktu_selesai=selesai['waktu_selesai']
				for idwaktu in waktu:
				    waktu_id=idwaktu['waktu_id']
				pltu = PLTU.objects.values('pltu_id').filter(nama_pltu=nama_pltu)
				for idpltu in pltu:
				    pltu_id=idpltu['pltu_id']
				hasil = Rekap_shipment.objects.filter(pltu=nama_pltu, konfirmasi_rakor__range=[waktu_mulai,waktu_selesai])
				totalbaris = Rekap_shipment.objects.filter(pltu=nama_pltu, konfirmasi_rakor__range=[waktu_mulai,waktu_selesai]).count()
				hasil2 = PLTU.objects.all()
				context = {
				'judul':'Penilaian Pemasok Batu Bara',
				#'data':hasil,
				'data2':hasil,
				'nama_pltu':nama_pltu,
				'waktu':triwulan+" "+tahun,
				'waktuid':waktu_id,
				'pltuid':pltu_id,
				'totalbaris':totalbaris
				}
				return render(request,'buatgrading.html', context)

		else:
			hasil2 = PLTU.objects.all()
			context = {
				'judul':'Penilaian Pemasok Batu Bara',
				'data2':hasil2,
            }
			return render(request,'grading.html', context)
	else:
		return redirect('login')

def caripemasok(request):
    #hasil1 = Rekap_shipment.objects.filter(pk=pk)
    if request.method == 'POST':
        nama_pemasok = request.POST['nama_pemasok']
        hasil = Data_grading.objects.filter(nama_pemasok=nama_pemasok)
        hasil3 = PLTU.objects.all()
        hasil4 = Pemasok.objects.all().order_by('pemasok_id')
        context = {
            'data2':hasil,
            'data3':hasil3,
            'data4':hasil4
        }
        return render(request,'index.html', context)
    else:
        return HttpResponseRedirect('/')

def detailgrading(request, pk):
	if request.user.is_authenticated:
		if request.method == "POST":
			if request.POST["logout"] == "":
				logout(request)
				return redirect('login')

		hasil1 = FactGradingRekapanPenilaianPemasok.objects.filter(pk=pk)
		for idpltu in hasil1:
			print(idpltu.pltu)
		for idpemasok in hasil1:
		    print(idpemasok.pemasok_id)
		for idwaktu in hasil1:
			print(idwaktu.waktu_id)
		hasil2 = FactGradingPerhitunganTertimbang.objects.filter(pltu=idpltu.pltu,pemasok=idpemasok.pemasok_id,waktu=idwaktu.waktu_id)
		hasil3 = FactGradingPenolakan.objects.filter(pltu=idpltu.pltu,pemasok=idpemasok.pemasok_id,waktu=idwaktu.waktu_id)
		context = {
			'data1':hasil1,
			'data2':hasil2,
			'data3':hasil3,
		}
		#http://127.0.0.1:8000/grading/detailgrading/31076
		return render(request,'detailgrading.html', context)
	else:
		return redirect('login')

def konfirgrading(request):
	if request.user.is_authenticated:
		if request.method == "POST":
			if 'logout' in request.POST:
				logoutnya = request.POST['logout']
				if logoutnya == "":
					logout(request)
					return redirect('login')

			pltu = request.POST['pltu']
			waktu = request.POST['waktu']
			FactGradingPerhitunganTertimbang.objects.filter(pltu_id=pltu,waktu_id=waktu).delete()
			totalbaris = int(request.POST['totalbaris'])
			for x in range(totalbaris):
				a = int(request.POST.getlist('pltu')[x])
				b = int(request.POST.getlist('pemasok')[x])
				c = request.POST.getlist('waktu')[x]
				d = request.POST.getlist('pt_gcv')[x]
				e = request.POST.getlist('pt_tm')[x]
				f = request.POST.getlist('pt_ts')[x]
				g = request.POST.getlist('pt_ash')[x]
				h = request.POST.getlist('pt_hgi')[x]
				i = request.POST.getlist('pt_idt')[x]
				j = request.POST.getlist('pt_mt')[x]
				insertnya = FactGradingPerhitunganTertimbang(pltu_id=a, pemasok_id=b, waktu_id=c,pt_gcv=d,pt_tm=e,pt_ts=f,pt_ash=g,pt_hgi=h,pt_idt=i,pt_mt=j)
				insertnya.save()
			#return HttpResponseRedirect('/inputgrading')
			totalbaris = FactGradingPerhitunganTertimbang.objects.filter(pltu_id=pltu,waktu_id=waktu).values('pemasok__nama_pemasok','pemasok_id').distinct().count()
			hasil1 = FactGradingPerhitunganTertimbang.objects.filter(pltu_id=pltu,waktu_id=waktu).values('pemasok__nama_pemasok','pemasok_id').distinct()
			print(hasil1)
			hasil2 = FactGradingPerhitunganTertimbang.objects.filter(pltu_id=pltu,waktu_id=waktu).values_list('pemasok',flat=True).distinct()
			hasil3 = list(hasil2)

			hasil4 = [int(numeric_string) for numeric_string in hasil3]
			hasil4 = FactGradingRekapanPenilaianPemasok.objects.filter(pltu_id=pltu,waktu_id=int(waktu)-1,pemasok_id__in=hasil4)
			#POSTS = Posts.objects.filter(ownerid__in=[f.hasil1 for f in hasil1])
			print(hasil4)
			from itertools import cycle
			hasil = zip(hasil1, cycle(hasil4)) if len(hasil1) > len(hasil4) else zip(cycle(hasil1), hasil4)
			#hasil=zip(hasil1, hasil4)
			context = {
				'data1':hasil1,
				'data4':hasil4,
				'data': hasil,
				'waktuid':waktu,
				'pltuid':pltu,
				'totalbaris':totalbaris
			}
			#print(hasil2)
			return render(request,'prosesgrading.html', context)
		else:
			return redirect('login')

def prosesgrading(request):
	if request.user.is_authenticated:
		if request.method == "POST":
			if 'logout' in request.POST:
				logoutnya = request.POST['logout']
				if logoutnya == "":
					logout(request)
					return redirect('login')

		if 'caripltu' in request.POST:
			caripltu = request.POST['caripltu']
			nama_pltu = request.POST['nama_pltu']
			triwulan =  request.POST['triwulan']
			tahun = request.POST['tahun']
			if caripltu != None:
				pltu = PLTU.objects.values('pltu_id').filter(nama_pltu=nama_pltu)
				for idpltu in pltu:
				    print(idpltu['pltu_id'])
				waktu = Waktu.objects.values('waktu_id').filter(triwulan=triwulan,tahun=tahun)
				for idwaktu in waktu:
				    print(idwaktu['waktu_id'])

				hasil = FactGradingRekapanPenilaianPemasok.objects.filter(pltu=idpltu['pltu_id'],waktu=idwaktu['waktu_id']).order_by('waktu_id','-nilai_akhir')
				hasil2 = PLTU.objects.all()
				context = {
				'judul':'Penilaian Pemasok Batu Bara',
				'data':hasil,
				'data2':hasil2,
				}
				return render(request,'grading.html', context)

		if 'buatgrading' in request.POST:
			buatgrading = request.POST['buatgrading']
			nama_pltu = request.POST['nama_pltu']
			triwulan =  request.POST['triwulan']
			tahun = request.POST['tahun']
			if buatgrading != None:
				waktu = Waktu.objects.values('waktu_id','waktu_mulai','waktu_selesai').filter(triwulan=triwulan,tahun=tahun)
				for mulai in waktu:
				    waktu_mulai=mulai['waktu_mulai']
				for selesai in waktu:
				    waktu_selesai=selesai['waktu_selesai']
				for idwaktu in waktu:
				    waktu_id=idwaktu['waktu_id']
				pltu = PLTU.objects.values('pltu_id').filter(nama_pltu=nama_pltu)
				for idpltu in pltu:
				    pltu_id=idpltu['pltu_id']
				hasil = Rekap_shipment.objects.filter(pltu=nama_pltu, konfirmasi_rakor__range=[waktu_mulai,waktu_selesai])
				totalbaris = Rekap_shipment.objects.filter(pltu=nama_pltu, konfirmasi_rakor__range=[waktu_mulai,waktu_selesai]).count()
				hasil2 = PLTU.objects.all()
				context = {
				'judul':'Penilaian Pemasok Batu Bara',
				#'data':hasil,
				'data2':hasil,
				'nama_pltu':nama_pltu,
				'waktu':triwulan+" "+tahun,
				'waktuid':waktu_id,
				'pltuid':pltu_id,
				'totalbaris':totalbaris
				}
				return render(request,'buatgrading.html', context)

		else:
			pltu = request.POST['pltu']
			waktu = request.POST['waktu']
			FactGradingRekapanPenilaianPemasok.objects.filter(pltu_id=pltu,waktu_id=waktu).delete()
			totalbaris = int(request.POST['totalbaris'])
			for x in range(totalbaris):
				a = int(request.POST.getlist('pltu')[x])
				id_pemasok = int(request.POST.getlist('pemasok')[x])
				c = request.POST.getlist('waktu')[x]
				d = request.POST.getlist('p1_gcv_typical')[x]
				e = request.POST.getlist('p1_tm_typical')[x]
				f = request.POST.getlist('p1_ts_typical')[x]
				g = request.POST.getlist('p1_ash_typical')[x]
				h = request.POST.getlist('p1_hgi_typical')[x]
				i = request.POST.getlist('p1_idt_typical')[x]
				j = request.POST.getlist('p1_gcv_penolakan')[x]
				k = request.POST.getlist('p1_tm_penolakan')[x]
				l = request.POST.getlist('p1_ts_penolakan')[x]
				m = request.POST.getlist('p1_ash_penolakan')[x]
				n = request.POST.getlist('p1_hgi_penolakan1')[x]
				o = request.POST.getlist('p1_hgi_penolakan2')[x]
				p = request.POST.getlist('p1_idt_penolakan')[x]
				q = request.POST.getlist('p2_konfirmasi')[x]
				#insertnya = FactGradingRekapanPenilaianPemasok(pltu_id=a, pemasok_id=b, waktu_id=c,p1_gcv_typical=d,p1_tm_typical=e,p1_ts_typical=f,p1_ash_typical=g,p1_hgi_typical=h,p1_idt_typical=i,p1_gcv_penolakan=j,p1_tm_penolakan=k,p1_ts_penolakan=l,p1_ash_penolakan=m,p1_hgi_penolakan1=n,p1_hgi_penolakan2=o,p1_idt_penolakan=p,p2_konfirmasi=q)
				#insertnya.save()

				print("\n ============== ++ PROGRAM Penilaian Pemasok Batu Bara ++ ================ \n\n")
				jumlah_data = 0
				pltu_id = pltu
				waktu_id = waktu

				# MENCARI NAMA PLTU BERDASARKAN variabel pltu_id
				nama_pltu = PLTU.objects.filter(
					pltu_id=pltu_id).values_list(
					'nama_pltu', flat=True).get()

				print(
					" \n\n ====================================================================== ")
				print("   ++++++++++   NAMA PLTU =   ", nama_pltu, "+++++++++++")
				print(" ====================================================================== ")

				# list pemasok khusus PLTU terpilih
				list_nama_pemasok = list(FactGradingPerhitunganTertimbang.objects.filter(
					pltu_id=pltu_id).values_list('pemasok_id__nama_pemasok', flat=True).distinct())
				list_id_pemasok = list(FactGradingPerhitunganTertimbang.objects.filter(
					pltu_id=pltu_id).values_list('pemasok_id', flat=True).distinct())

				print("\n LIST Nama pemasok = ", list_nama_pemasok)
				print("\n LIST ID Pemasok =", list_id_pemasok)
				print("\n Banyaknya pemasok di ", nama_pltu, " : ", len(list_nama_pemasok))
				nama_pemasok=FactGradingPerhitunganTertimbang.objects.filter(pltu_id=pltu,waktu_id=waktu,pemasok_id=id_pemasok).values('pemasok__nama_pemasok').distinct()
				print(" \n\n @@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@  ")
				print(" NAMA PEMASOK =   ", nama_pemasok)
				print(" ID PEMASOK =   ", id_pemasok)
				print(" ID PLTU =   ", pltu_id)
				print(" @@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@  ")

				#  Nilai perhitungan tertimbang dilakukan FILTER berdasarkan PLTU DAN WAKTU-nya
				gcv_tertimbang = list(FactGradingPerhitunganTertimbang.objects.filter(
					pltu_id=pltu_id).filter(waktu_id=waktu_id).filter(pemasok_id__nama_pemasok__contains=nama_pemasok).values_list('pt_gcv', flat=True))
				tm_tertimbang = list(FactGradingPerhitunganTertimbang.objects.filter(
					pltu_id=pltu_id).filter(waktu_id=waktu_id).filter(pemasok_id__nama_pemasok__contains=nama_pemasok).values_list('pt_tm', flat=True))
				ts_tertimbang = list(FactGradingPerhitunganTertimbang.objects.filter(
					pltu_id=pltu_id).filter(waktu_id=waktu_id).filter(pemasok_id__nama_pemasok__contains=nama_pemasok).values_list('pt_ts', flat=True))
				ash_tertimbang = list(FactGradingPerhitunganTertimbang.objects.filter(
					pltu_id=pltu_id).filter(waktu_id=waktu_id).filter(pemasok_id__nama_pemasok__contains=nama_pemasok).values_list('pt_ash', flat=True))
				hgi_tertimbang = list(FactGradingPerhitunganTertimbang.objects.filter(
					pltu_id=pltu_id).filter(waktu_id=waktu_id).filter(pemasok_id__nama_pemasok__contains=nama_pemasok).values_list('pt_hgi', flat=True))
				idt_tertimbang = list(FactGradingPerhitunganTertimbang.objects.filter(
					pltu_id=pltu_id).filter(waktu_id=waktu_id).filter(pemasok_id__nama_pemasok__contains=nama_pemasok).values_list('pt_idt', flat=True))
				print("\n Idt tertimbang : \n", idt_tertimbang)
				mt_tertimbang = list(FactGradingPerhitunganTertimbang.objects.filter(
					pltu_id=pltu_id).filter(waktu_id=waktu_id).filter(pemasok_id__nama_pemasok__contains=nama_pemasok,).values_list('pt_mt', flat=True))

				'''
		        # Nilai penolakan pada tabel grading penolakan
		        gcv_penolakan = list(FactGradingPenolakan.objects.filter(
		            pltu_id=pltu_id).filter(waktu_id=waktu_id).filter(pemasok_id__nama_pemasok__contains=nama_pemasok).
		            values_list('pn_gcv', flat=True))
		        tm_penolakan = list(FactGradingPenolakan.objects.filter(
		            pltu_id=pltu_id).filter(waktu_id=waktu_id).filter(pemasok_id__nama_pemasok__contains=nama_pemasok).values_list('pn_tm', flat=True))
		        ts_penolakan = list(FactGradingPenolakan.objects.filter(
		            pltu_id=pltu_id).filter(waktu_id=waktu_id).filter(pemasok_id__nama_pemasok__contains=nama_pemasok).values_list('pn_ts', flat=True))
		        ash_penolakan = list(FactGradingPenolakan.objects.filter(
		            pltu_id=pltu_id).filter(waktu_id=waktu_id).filter(pemasok_id__nama_pemasok__contains=nama_pemasok).values_list('pn_ash', flat=True))
		        hgi_penolakan = list(FactGradingPenolakan.objects.filter(
		            pltu_id=pltu_id).filter(waktu_id=waktu_id).filter(pemasok_id__nama_pemasok__contains=nama_pemasok).values_list('pn_hgi', flat=True))
		        idt_penolakan = list(FactGradingPenolakan.objects.filter(
		            pltu_id=pltu_id).filter(waktu_id=waktu_id).filter(pemasok_id__nama_pemasok__contains=nama_pemasok).values_list('pn_idt', flat=True))
		        mt_penolakan = list(FactGradingPenolakan.objects.filter(
		            pltu_id=pltu_id).filter(waktu_id=waktu_id).filter(pemasok_id__nama_pemasok__contains=nama_pemasok,).values_list('pn_mt', flat=True))
		        '''
				print("\n LIST MT :  \n",mt_tertimbang)

		        # nilai typical,nilai batas penolakan adalah nilai yang di-INPUT user,bukan dari rekap shipment
				realisasi_pencapaian_pasokan = float(sum(mt_tertimbang))
				'''
				# nilai input pemasok ke-1
				if(nama_pemasok == 'AI REG'):
					typical_gcv = float(4200)
					penolakan_gcv = float(4000)
					typical_tm = float(35)
					penolakan_tm = float(36)
					typical_ts = float(0.33)
					penolakan_ts = float(0.35)
					typical_ash = float(5)
					penolakan_ash = float(6)
					typical_hgi = float(60)
					penolakan_hgi_1 = float(48)
					penolakan_hgi_2 = float(70)
					typical_idt = float(1150)
					penolakan_idt = float(1100)
					konfirmasi_pencapaian_pasokan = float(112500)

				# nilai input pemasok ke-2
				if(nama_pemasok == 'PLNBB LRC'):
					typical_gcv = float(4200)
					penolakan_gcv = float(4000)
					typical_tm = float(34)
					penolakan_tm = float(37)
					typical_ts = float(0.2)
					penolakan_ts = float(0.4)
					typical_ash = float(4)
					penolakan_ash = float(7)
					typical_hgi = float(60)
					penolakan_hgi_1 = float(45)
					penolakan_hgi_2 = float(65)
					typical_idt = float(1150)
					penolakan_idt = float(1100)
					konfirmasi_pencapaian_pasokan = float(112500)

				# nilai input pemasok ke-3
				if(nama_pemasok == 'DP'):
					typical_gcv = float(4650)
					penolakan_gcv = float(4200)
					typical_tm = float(31)
					penolakan_tm = float(35)
					typical_ts = float(0.16)
					penolakan_ts = float(0.35)
					typical_ash = float(3.54)
					penolakan_ash = float(6)
					typical_hgi = float(53)
					penolakan_hgi_1 = float(42)
					penolakan_hgi_2 = float(65)
					typical_idt = float(1345)
					penolakan_idt = float(1100)
					konfirmasi_pencapaian_pasokan = float(4500)

				typical_gcv = float(4650)
				penolakan_gcv = float(4200)
				typical_tm = float(31)
				penolakan_tm = float(35)
				typical_ts = float(0.16)
				penolakan_ts = float(0.35)
				typical_ash = float(3.54)
				penolakan_ash = float(6)
				typical_hgi = float(53)
				penolakan_hgi_1 = float(42)
				penolakan_hgi_2 = float(65)
				typical_idt = float(1345)
				penolakan_idt = float(1100)
				konfirmasi_pencapaian_pasokan = float(4500)
				'''
				typical_gcv = float(d)
				penolakan_gcv = float(j)
				typical_tm = float(e)
				penolakan_tm = float(k)
				typical_ts = float(f)
				penolakan_ts = float(l)
				typical_ash = float(g)
				penolakan_ash = float(m)
				typical_hgi = float(h)
				penolakan_hgi_1 = float(n)
				penolakan_hgi_2 = float(o)
				typical_idt = float(i)
				penolakan_idt = float(p)
				konfirmasi_pencapaian_pasokan = float(q)
				# Nilai penolakan pada tabel grading penolakan
				gcv_penolakan = []
				tm_penolakan = []
				ts_penolakan = []
				ash_penolakan = []
				hgi_penolakan = []
				idt_penolakan = []
				mt_penolakan = []
				jumlah_penolakan = 0
				for a in (gcv_tertimbang):
					if(a < penolakan_gcv):
						jumlah_penolakan += 1
					selisih = a-penolakan_gcv
					gcv_penolakan.append(selisih)
				for a in (tm_tertimbang):
					if(a > penolakan_tm):
						jumlah_penolakan += 1
					selisih = a-penolakan_tm
					tm_penolakan.append(selisih)
				for a in (ts_tertimbang):
					if(a > penolakan_ts):
						jumlah_penolakan += 1
					selisih = a-penolakan_ts
					ts_penolakan.append(selisih)
				for a in (ash_tertimbang):
					if(a > penolakan_ash):
						jumlah_penolakan += 1
					selisih = a-penolakan_ash
					ash_penolakan.append(selisih)
				for a in (hgi_tertimbang):
					if(a > penolakan_hgi_2):
						jumlah_penolakan += 1
					selisih = a-penolakan_hgi_2
					hgi_penolakan.append(selisih)
				for a in (idt_tertimbang):
					if(a < penolakan_idt):
						jumlah_penolakan += 1
					selisih = a-penolakan_idt
					idt_penolakan.append(selisih)

				print("\n  Jumlah penolakan shipment: ", jumlah_penolakan)
				print("\n  GCV Penolakan : ", gcv_penolakan)
				print("\n  TM Penolakan : ", tm_penolakan)
				print("\n  TS Penolakan : ", ts_penolakan)
				print("\n  ASH Penolakan : ", ash_penolakan)
				print("\n  HGI Penolakan : ", hgi_penolakan)
				print("\n  IDT Penolakan : ", idt_penolakan)
				print("\n Realisasi pencapaian pasokan :  \n",
					realisasi_pencapaian_pasokan)

		        # jumlah_penolakan = float(0)
				hasil_kali_gcv = []
				for i, (gcv, mt) in enumerate(zip(gcv_tertimbang, mt_tertimbang)):
					kali = gcv*mt
					hasil_kali_gcv.append(kali)
				total_gcv_kali_mt = sum(hasil_kali_gcv)

				hasil_kali_tm = []
				for i, (tm, mt) in enumerate(zip(tm_tertimbang, mt_tertimbang)):
					kali = tm*mt
					hasil_kali_tm.append(kali)
				total_tm_kali_mt = sum(hasil_kali_tm)

				hasil_kali_ts = []
				for i, (ts, mt) in enumerate(zip(ts_tertimbang, mt_tertimbang)):
					kali = ts*mt
					hasil_kali_ts.append(kali)
				total_ts_kali_mt = sum(hasil_kali_ts)

				hasil_kali_ash = []
				for i, (ash, mt) in enumerate(zip(ash_tertimbang, mt_tertimbang)):
					kali = ash*mt
					hasil_kali_ash.append(kali)
				total_ash_kali_mt = sum(hasil_kali_ash)

				hasil_kali_hgi = []
				for i, (hgi, mt) in enumerate(zip(hgi_tertimbang, mt_tertimbang)):
					kali = hgi*mt
					hasil_kali_hgi.append(kali)
				total_hgi_kali_mt = sum(hasil_kali_hgi)

				hasil_kali_idt = []
				for i, (idt, mt) in enumerate(zip(idt_tertimbang, mt_tertimbang)):
					kali = idt*mt
					hasil_kali_idt.append(kali)
				total_idt_kali_mt = sum(hasil_kali_idt)

				gcv_realisasi = total_gcv_kali_mt/sum(mt_tertimbang)
				tm_realisasi = total_tm_kali_mt/sum(mt_tertimbang)
				ts_realisasi = total_ts_kali_mt/sum(mt_tertimbang)
				ash_realisasi = total_ash_kali_mt/sum(mt_tertimbang)
				hgi_realisasi = total_hgi_kali_mt/sum(mt_tertimbang)
				idt_realisasi = total_idt_kali_mt/sum(mt_tertimbang)

				print("\n  GCV realisasi : ", gcv_realisasi)
				print("  TM realisasi : ", tm_realisasi)
				print("  TS realisasi : ", ts_realisasi)
				print("  ASH realisasi : ", ash_realisasi)
				print("  HGI realisasi : ", hgi_realisasi)
				print("  IDT realisasi : ", idt_realisasi)

				'''       1. Penilaian Kualitas Batubara      '''
				def func_nilai_pengurang_gcv(gcv_realisasi, typical_gcv, penolakan_gcv):
					if(gcv_realisasi >= typical_gcv):
						nilai_pengurang_gcv = 0
					elif(gcv_realisasi >= (penolakan_gcv+(typical_gcv-penolakan_gcv)/2)):
						nilai_pengurang_gcv = -5
					elif(gcv_realisasi >= penolakan_gcv):
						nilai_pengurang_gcv = -10
					else:
						nilai_pengurang_gcv = -15
					return nilai_pengurang_gcv
				nilai_pengurang_gcv = func_nilai_pengurang_gcv(
					gcv_realisasi, typical_gcv, penolakan_gcv)
				print("\nNilai pengurang GCV : ", nilai_pengurang_gcv)

				def func_nilai_pengurang(nilai_realisasi, nilai_typical, nilai_penolakan):
					if(nilai_realisasi <= nilai_typical):
						nilai_pengurang = 0
					elif(nilai_realisasi <= (nilai_typical+(nilai_penolakan-nilai_typical)/2)):
						nilai_pengurang = -2.5
					elif(nilai_realisasi <= nilai_penolakan):
						nilai_pengurang = -5
					else:
						nilai_pengurang = -10
					return nilai_pengurang

				nilai_pengurang_tm = func_nilai_pengurang(
		            tm_realisasi, typical_tm, penolakan_tm)
				print("Nilai pengurang TM : ", nilai_pengurang_tm)

				nilai_pengurang_ts = func_nilai_pengurang(
					ts_realisasi, typical_ts, penolakan_ts)
				print("Nilai pengurang TS : ", nilai_pengurang_ts)

				nilai_pengurang_ash = func_nilai_pengurang(
					ash_realisasi, typical_ash, penolakan_ash)
				print("Nilai pengurang ASH : ", nilai_pengurang_ash)

				def func_nilai_pengurang_hgi(hgi_realisasi, penolakan_hgi_1, penolakan_hgi_2):
					if(hgi_realisasi <= penolakan_hgi_1 or hgi_realisasi >= penolakan_hgi_2):
						nilai_pengurang_hgi = -10
					else:
						nilai_pengurang_hgi = 0
					return nilai_pengurang_hgi

				nilai_pengurang_hgi = func_nilai_pengurang_hgi(
					hgi_realisasi, penolakan_hgi_1, penolakan_hgi_2)
				print("Nilai pengurang HGI : ", nilai_pengurang_hgi)

				def func_nilai_pengurang_idt(idt_realisasi, typical_idt, penolakan_idt):
					if(idt_realisasi >= typical_idt):
						nilai_pengurang_idt = 0
					elif(idt_realisasi >= penolakan_idt):
						nilai_pengurang_idt = -5
					else:
						nilai_pengurang_idt = -10
					return nilai_pengurang_idt

				nilai_pengurang_idt = func_nilai_pengurang_idt(
					idt_realisasi, typical_idt, penolakan_idt)
				print("Nilai pengurang IDT : ", nilai_pengurang_idt)
				'''
				2. Pencapaian Pasokan Terhadap Konfirmasi Triwulanan      '''
				def func_pencapaian_pasokan(persentase_realisasi):
					if(persentase_realisasi >= 0.95):
						nilai_pengurang = 0
					elif(persentase_realisasi >= 0.75):
						nilai_pengurang = -5
					elif(persentase_realisasi >= 0.50):
						nilai_pengurang = -10
					elif(persentase_realisasi >= 0.30):
						nilai_pengurang = -15
					else:
						nilai_pengurang = -20
					return nilai_pengurang
				persentase_realisasi = (realisasi_pencapaian_pasokan/konfirmasi_pencapaian_pasokan)*100
				print("\nPersentase realisasi pencapaian pasokan ",
		              persentase_realisasi*100, "%")

				nilai_pengurang_pasokan = func_pencapaian_pasokan(
		            persentase_realisasi)
				print("\n Nilai pengurang Pasokan : ", nilai_pengurang_pasokan)

				'''  3. Pengurang Persentase Batas
		            Penolakan  '''
				total_shipment = len(mt_tertimbang)
				print("\n Total shipment : \n", total_shipment)
				if(total_shipment == 0):
					total_shipment += 1

				def func_batas_penolakan(persentase_penolakan):
					if(persentase_penolakan <= 0):
						nilai_pengurang = 0
					elif(persentase_penolakan <= 2):
						nilai_pengurang = -5
					elif(persentase_penolakan <= 4):
						nilai_pengurang = -10
					elif(persentase_penolakan <= 6):
						nilai_pengurang = -15
					elif(persentase_penolakan <= 8):
						nilai_pengurang = -20
					else:
						nilai_pengurang = -25
					return nilai_pengurang

				persentase_penolakan = jumlah_penolakan/total_shipment
				print("\nPersentase penolakan : ",
					persentase_penolakan*100, "%")
				nilai_pengurang_batas_penolakan = func_batas_penolakan(
					persentase_penolakan)
				print("Nilai pengurang Batas penolakan : ",
					nilai_pengurang_batas_penolakan)

		        # PENILAIAN
				nilai_awal = 100
				nilai_akhir_gcv = nilai_awal+nilai_pengurang_gcv
				nilai_akhir_tm = nilai_akhir_gcv+nilai_pengurang_tm
				nilai_akhir_ts = nilai_akhir_tm+nilai_pengurang_ts
				nilai_akhir_ash = nilai_akhir_ts+nilai_pengurang_ash
				nilai_akhir_hgi = nilai_akhir_ash+nilai_pengurang_hgi
				nilai_akhir_idt = nilai_akhir_hgi+nilai_pengurang_idt
				nilai_akhir_pasokan = nilai_akhir_idt+nilai_pengurang_pasokan
				nilai_akhir_penolakan = nilai_akhir_pasokan+nilai_pengurang_batas_penolakan
				nilai_final = nilai_akhir_penolakan

				print(" \n Nilai Akhir pemasok ",
					nama_pemasok, " adalah : ", nilai_final)

				if(nilai_final >= 90):
					klasifikasi = 'A (Excellent)'
				elif(nilai_final >= 85):
					klasifikasi = 'B+ (Better)'
				elif(nilai_final >= 80):
					klasifikasi = 'B (Good)'
				elif(nilai_final >= 75):
					klasifikasi = 'C+ (Fair)'
				elif(nilai_final >= 70):
					klasifikasi = 'C (Fair Enough)'
				elif(nilai_final >= 60):
					klasifikasi = 'D (Poor)'
				elif(nilai_final < 60):
					klasifikasi = 'E (Very Poor)'
				print("\n Klasifikasi = ", klasifikasi)

		        # ++++++++++++++++++++++++++++++++++ INPUT DATABASE +++++++++++++++++++++++++++++++++
		        # ++++++++++++++++++++++++++++++++++ INPUT DATABASE +++++++++++++++++++++++++++++++++
		        # ++++++++++++++++++++++++++++++++++ INPUT DATABASE +++++++++++++++++++++++++++++++++
				FactGradingRekapanPenilaianPemasok.objects.create(
					pltu_id=pltu_id, pemasok_id=id_pemasok, waktu_id=waktu_id, p1_gcv_typical=typical_gcv, p1_gcv_penolakan=penolakan_gcv,
					p1_tm_typical=typical_tm, p1_tm_penolakan=penolakan_tm,  p1_ts_typical=typical_ts, p1_ts_penolakan=penolakan_ts,
					p1_ash_typical=typical_ash, p1_ash_penolakan=penolakan_ash, p1_hgi_typical=typical_hgi, p1_hgi_penolakan1=penolakan_hgi_1,
		            p1_hgi_penolakan2=penolakan_hgi_2, p1_idt_typical=typical_idt, p1_idt_penolakan=penolakan_idt,
		            p1_gcv_realisasi=gcv_realisasi, p1_tm_realisasi=tm_realisasi, p1_ts_realisasi=ts_realisasi, p1_ash_realisasi=ash_realisasi,
		            p1_hgi_realisasi=hgi_realisasi, p1_idt_realisasi=idt_realisasi,
		            p1_gcv_pengurang=nilai_pengurang_gcv, p1_tm_pengurang=nilai_pengurang_tm, p1_ts_pengurang=nilai_pengurang_ts,
		            p1_ash_pengurang=nilai_pengurang_ash, p1_hgi_pengurang=nilai_pengurang_hgi, p1_idt_pengurang=nilai_pengurang_idt,
		            p1_gcv_nilaiakhir=nilai_akhir_gcv, p1_tm_nilaiakhir=nilai_akhir_tm, p1_ts_nilaiakhir=nilai_akhir_ts,
		            p1_ash_nilaiakhir=nilai_akhir_ash, p1_hgi_nilaiakhir=nilai_akhir_hgi, p1_idt_nilaiakhir=nilai_akhir_idt,
		            p2_konfirmasi=konfirmasi_pencapaian_pasokan, p2_realisasi=realisasi_pencapaian_pasokan, p2_persentase_pasokan=persentase_realisasi,
		            p2_pengurang_pasokan=nilai_pengurang_pasokan, p2_nilai_akhir=nilai_akhir_pasokan,
		            p3_total_shipment=total_shipment, p3_jmlh_shipment_tertolak=jumlah_penolakan, p3_persentase_penolakan=persentase_penolakan,
		            p3_pengurang_penolakan=nilai_pengurang_batas_penolakan, nilai_akhir=nilai_final, klasifikasi=klasifikasi
		        )
				print("\n INSERT PENILAIAN KE DATABASE BERHASIL !! \n")
				print(totalbaris)

			hasil = FactGradingRekapanPenilaianPemasok.objects.filter(pltu=pltu,waktu=waktu).order_by('waktu_id','-nilai_akhir')
			hasil2 = PLTU.objects.all()
			context = {
				'judul':'Penilaian Pemasok Batu Bara',
				'data':hasil,
				'data2':hasil2,
			}
			#return redirect('grading')
			return render(request,'grading.html', context)

	else:
		return redirect('login')

def tambahpemasok(request):
    if request.method == 'POST':
        form = FormPemasok(request.POST)
        if form.is_valid():
            form.save()
        return HttpResponseRedirect('/master')
    else:
        return HttpResponseRedirect('/master')

def printnilai(request, pk):
	if request.user.is_authenticated:
		if request.method == "POST":
			if request.POST["logout"] == "":
				logout(request)
				return redirect('login')

		hasil1 = FactGradingRekapanPenilaianPemasok.objects.filter(pk=pk)
		now = datetime.datetime.now()
		context = {
			'data1':hasil1,
			'waktu':now
		}
		return render(request,'print.html', context)
	else:
		return redirect('login')
