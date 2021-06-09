from django.shortcuts import render, redirect, get_object_or_404
from django.http import HttpResponse, HttpResponseRedirect
from django.contrib.auth.decorators import login_required
from django.contrib.auth import authenticate, login, logout
from .models import *
from .forms import *
from django.db.models import Q


# Create your views here.
def loginView(request):
    print("Masuk1",request.method)
    #print(request.GET)
    print("Masuk1a",request.POST)
    context = {
        'page_title':'LOGIN',
    }
    user = None

    if request.method == "GET":
        if request.user.is_authenticated:
            # logika untuk user
            print("Masuk2", request.method)
            #print(request.GET)
            print("masuk2a",request.GET)
            return redirect('index')
        else:
            # logika untuk anonymous
            #return render(request, 'login.html', context)
            print("Masuk3", request.method)
            #print(request.GET)
            print("masuk3a",request.GET)
            return redirect('login')


    if request.method == "POST":
        print("Masuk4", request.method)
        #print(request.GET)
        print("masuk4a",request.POST)
        username_login = request.POST['username']
        password_login = request.POST['password']

        user = authenticate(request, username=username_login, password=password_login)

        if user is not None:
            print("Masuk5", request.method)
            #print(request.GET)
            print("masuk5a",request.POST)
            login(request, user)
            return redirect('index')
        else:
            print("Masuk6", request.method)
            #print(request.GET)
            print("masuk6a",request.POST)
            return redirect('login')

    return redirect('login')


# Create your views here.
def index(request):
    if request.user.is_authenticated:
        if request.method == "POST":
            if request.POST["logout"] == "":
                logout(request)
                return redirect('login')

        queryWaktuDistinctTriwulan = Waktu.objects.filter(~Q(tahun=2019)).values('triwulan').distinct()
        hasil1 = Pemasok.objects.all().order_by('pemasok_id')
        hasil2 = PLTU.objects.all()
        hasil3 = Sumbertambang.objects.all().order_by('kode_sumber_tambang')
        hasil4 = Waktu.objects.all()
        context = {
            'judul':'Data Master',
            'kontributor':'Admin',
            'app_css':'master/css/styles.css',
            'data1':hasil1,
            'data2':hasil2,
            'data3':hasil3,
            'data4':hasil4,
            'queryWaktuDistinctTriwulan':queryWaktuDistinctTriwulan
        }
        return render(request,'master/index.html', context)

    else:
        #return render(request, 'login.html')
        return redirect('login')

def tambahpemasok(request):
    if request.method == 'POST':
        form = FormPemasok(request.POST)
        if form.is_valid():
            form.save()
        return HttpResponseRedirect('/master')
    else:
        return HttpResponseRedirect('/master')

def tambahpltu(request):
    if request.method == 'POST':
        form = FormPLTU(request.POST)
        if form.is_valid():
            form.save()
        return HttpResponseRedirect('/master')
    else:
        return HttpResponseRedirect('/master')

def tambahsumbertambang(request):
    if request.method == 'POST':
        form = FormSumberTambang(request.POST)
        if form.is_valid():
            form.save()
        return HttpResponseRedirect('/master')
    else:
        return HttpResponseRedirect('/master')

def hapuspemasok(request, pk):
    pemasok = Pemasok.objects.get(pk=pk)
    pemasok.delete()
    return HttpResponseRedirect('/master')
    #return HttpResponseRedirect('/master')

def hapuspltu(request, pk):
    pltu = PLTU.objects.get(pk=pk)
    pltu.delete()
    #return HttpResponseRedirect('/')
    return HttpResponseRedirect('/master')

def hapussumbertambang(request, pk):
    sumbertambang = Sumbertambang.objects.get(pk=pk)
    sumbertambang.delete()
    #return HttpResponseRedirect('/')
    return HttpResponseRedirect('/master')

def editpemasok(request, pk):

    if request.user.is_authenticated:
        if 'logout' in request.POST:
            logoutnya = request.POST['logout']
            if logoutnya == "":
                logout(request)
                return redirect('login')

        hasil1 = Pemasok.objects.filter(pk=pk)
        context = {
            'judul':'Edit Pemasok',
            'app_css':'blog/css/styles.css',
            'data1':hasil1,
        }
        return render(request,'master/editpemasok.html', context)
    else:
        #return render(request, 'login.html')
        return redirect('login')

def updatepemasok(request, pk):

    if request.user.is_authenticated:
        if 'logout' in request.POST:
            logoutnya = request.POST['logout']
            if logoutnya == "":
                logout(request)
                return redirect('login')

        instance = get_object_or_404(Pemasok, pk=pk)
        form = FormPemasok(request.POST or None, instance=instance)

        if form.is_valid():
            form.save()
        return HttpResponseRedirect('/master')
    else:
        #return render(request, 'login.html')
        return redirect('login')

def editpltu(request, pk):

    if request.user.is_authenticated:
        if 'logout' in request.POST:
            logoutnya = request.POST['logout']
            if logoutnya == "":
                logout(request)
                return redirect('login')

        hasil1 = PLTU.objects.filter(pk=pk)
        context = {
            'judul':'Edit PLTU',
            'app_css':'blog/css/styles.css',
            'data1':hasil1,
        }
        return render(request,'master/editpltu.html', context)
    else:
        #return render(request, 'login.html')
        return redirect('login')

def updatepltu(request, pk):

    if request.user.is_authenticated:
        if 'logout' in request.POST:
            logoutnya = request.POST['logout']
            if logoutnya == "":
                logout(request)
                return redirect('login')

        instance = get_object_or_404(PLTU, pk=pk)
        form = FormPLTU(request.POST or None, instance=instance)

        if form.is_valid():
            form.save()
        return HttpResponseRedirect('/master')
    else:
        #return render(request, 'login.html')
        return redirect('login')

def editsumbertambang(request, pk):

    if request.user.is_authenticated:
        if 'logout' in request.POST:
            logoutnya = request.POST['logout']
            if logoutnya == "":
                logout(request)
                return redirect('login')

        hasil1 = Sumbertambang.objects.filter(pk=pk)
        context = {
            'judul':'Edit Sumber Tambang',
            'app_css':'blog/css/styles.css',
            'data1':hasil1,
        }
        return render(request,'master/editsumbertambang.html', context)
    else:
        #return render(request, 'login.html')
        return redirect('login')

def updatesumbertambang(request, pk):

    if request.user.is_authenticated:
        if 'logout' in request.POST:
            logoutnya = request.POST['logout']
            if logoutnya == "":
                logout(request)
                return redirect('login')

        instance = get_object_or_404(Sumbertambang, pk=pk)
        form = FormSumberTambang(request.POST or None, instance=instance)

        if form.is_valid():
            form.save()
        return HttpResponseRedirect('/master')
    else:
        #return render(request, 'login.html')
        return redirect('login')

def tambahwaktu(request):
    if request.method == 'POST':
        print("AwalInputSolver",request.POST.items())
        print("AwalInputSolver",request.POST)
        print("AwalInputSolver",request.POST.__dict__)
        form = FormWaktu(request.POST)
        if form.is_valid():
            form.save()
        return HttpResponseRedirect('/master')
    else:
        return HttpResponseRedirect('/master')

def tambahpltu(request):
    if request.method == 'POST':
        form = FormPLTU(request.POST)
        if form.is_valid():
            form.save()
        return HttpResponseRedirect('/master')
    else:
        return HttpResponseRedirect('/master')

def hapuswaktu(request, pk):
    waktu = Waktu.objects.get(pk=pk)
    waktu.delete()
    return HttpResponseRedirect('/master')

def editmasterwaktu(request, pk):
    if request.user.is_authenticated:
        '''if request.method == "POST":
            if request.POST["logout"] == "":
                logout(request)
                return redirect('login')'''
        if 'logout' in request.POST:
            logoutnya = request.POST['logout']
            if logoutnya == "":
                logout(request)
                return redirect('login')

        #queryTableMasterSolver = FactSolverKontrakPemasok.objects.all()
        #queryPLTU = PLTU.objects.all()
        #queryPemasok = Pemasok.objects.all()
        #querySumberTambang = Sumbertambang.objects.all()
        #queryWaktu = Waktu.objects.all()
        queryWaktuDistinctTriwulan = Waktu.objects.all().values('triwulan').distinct()
        queryWaktuDistinctTahun = Waktu.objects.all().values('tahun').distinct()
        #queryJenisbbDistinct = Pemasok.objects.all().values('jenis_bb').distinct()

        querytwumum = Waktu.objects.filter(~Q(tahun=2019)).values('triwulan').distinct()
        querytw2019 = Waktu.objects.filter(Q(tahun=2019)).values('triwulan').distinct()
        querytahunumum = Waktu.objects.filter(~Q(tahun=2019)).values('tahun').distinct()


        #pltu = request.POST['id_pltu']
        #query_get_id_pltu = PLTU.objects.get(nama_pltu=pltu)
        #id_pltunya = query_get_id_pltu.pltu_id
        #queryPemasokDistinct = FactSolverKontrakPemasok.objects.filter(id_pltu=id_pltunya).values('id_pemasok').disinct()
        queryEditMasterWaktu = Waktu.objects.filter(pk=pk)
        context = {
            'judul':'Edit Master Solver',
            'kontributor':'Admin',
            'app_css':'blog/css/styles.css',
            #'dataMasterSolver':queryTableMasterSolver,
            #'queryPLTU':queryPLTU,
            #'queryPemasok':queryPemasok,
            #'querySumberTambang':querySumberTambang,
            #'queryWaktu':queryWaktu,
            'queryWaktuDistinctTriwulan':queryWaktuDistinctTriwulan,
            'queryWaktuDistinctTahun':queryWaktuDistinctTahun,
            #'queryPemasokDistinct':queryPemasokDistinct,
            #'queryEditMasterSolver':queryEditMasterSolver,
            #'queryJenisbbDistinct':queryJenisbbDistinct,
            'querytwumum':querytwumum,
            'querytw2019':querytw2019,
            'querytahunumum':querytahunumum,
            'queryEditMasterWaktu':queryEditMasterWaktu

        }

        return render(request,'master/editmasterwaktu.html', context)
    else:
        return redirect('login')

def updatemasterwaktu(request, pk):
    if request.user.is_authenticated:
        '''if request.method == "POST":
            if request.POST["logout"] == "":
                logout(request)
                return redirect('login')'''
        if 'logout' in request.POST:
            logoutnya = request.POST['logout']
            if logoutnya == "":
                logout(request)
                return redirect('login')

        if request.method == 'POST':
            instance = get_object_or_404(Waktu, pk=pk)
            form = FormWaktu(request.POST or None, instance=instance)
            if form.is_valid():
                form.save()
            return HttpResponseRedirect('/master')
        else:
            return HttpResponseRedirect('/master')
    else:
        return redirect('login')

def tambahwaktu(request):
    if request.method == 'POST':
        print("AwalInputSolver",request.POST.items())
        print("AwalInputSolver",request.POST)
        print("AwalInputSolver",request.POST.__dict__)
        form = FormWaktu(request.POST)
        print("form")
        if form.is_valid():
            form.save()
        print(form.errors)

        return HttpResponseRedirect('/master')
    else:
        return HttpResponseRedirect('/master')

def hapuswaktu(request, pk):
    waktu = Waktu.objects.get(pk=pk)
    waktu.delete()
    return HttpResponseRedirect('/master')

def editmasterwaktu(request, pk):
    if request.user.is_authenticated:
        '''if request.method == "POST":
            if request.POST["logout"] == "":
                logout(request)
                return redirect('login')'''
        if 'logout' in request.POST:
            logoutnya = request.POST['logout']
            if logoutnya == "":
                logout(request)
                return redirect('login')

        #queryTableMasterSolver = FactSolverKontrakPemasok.objects.all()
        #queryPLTU = PLTU.objects.all()
        #queryPemasok = Pemasok.objects.all()
        #querySumberTambang = Sumbertambang.objects.all()
        #queryWaktu = Waktu.objects.all()
        queryWaktuDistinctTriwulan = Waktu.objects.all().values('triwulan').distinct()
        queryWaktuDistinctTahun = Waktu.objects.all().values('tahun').distinct()
        #queryJenisbbDistinct = Pemasok.objects.all().values('jenis_bb').distinct()

        querytwumum = Waktu.objects.filter(~Q(tahun=2019)).values('triwulan').distinct()
        querytw2019 = Waktu.objects.filter(Q(tahun=2019)).values('triwulan').distinct()
        querytahunumum = Waktu.objects.filter(~Q(tahun=2019)).values('tahun').distinct()


        #pltu = request.POST['id_pltu']
        #query_get_id_pltu = PLTU.objects.get(nama_pltu=pltu)
        #id_pltunya = query_get_id_pltu.pltu_id
        #queryPemasokDistinct = FactSolverKontrakPemasok.objects.filter(id_pltu=id_pltunya).values('id_pemasok').disinct()
        queryEditMasterWaktu = Waktu.objects.filter(pk=pk)
        context = {
            'judul':'Edit Master Solver',
            'kontributor':'Admin',
            'app_css':'blog/css/styles.css',
            #'dataMasterSolver':queryTableMasterSolver,
            #'queryPLTU':queryPLTU,
            #'queryPemasok':queryPemasok,
            #'querySumberTambang':querySumberTambang,
            #'queryWaktu':queryWaktu,
            'queryWaktuDistinctTriwulan':queryWaktuDistinctTriwulan,
            'queryWaktuDistinctTahun':queryWaktuDistinctTahun,
            #'queryPemasokDistinct':queryPemasokDistinct,
            #'queryEditMasterSolver':queryEditMasterSolver,
            #'queryJenisbbDistinct':queryJenisbbDistinct,
            'querytwumum':querytwumum,
            'querytw2019':querytw2019,
            'querytahunumum':querytahunumum,
            'queryEditMasterWaktu':queryEditMasterWaktu

        }

        return render(request,'master/editmasterwaktu.html', context)
    else:
        return redirect('login')

def updatemasterwaktu(request, pk):
    if request.user.is_authenticated:
        '''if request.method == "POST":
            if request.POST["logout"] == "":
                logout(request)
                return redirect('login')'''
        if 'logout' in request.POST:
            logoutnya = request.POST['logout']
            if logoutnya == "":
                logout(request)
                return redirect('login')

        if request.method == 'POST':
            instance = get_object_or_404(Waktu, pk=pk)
            form = FormWaktu(request.POST or None, instance=instance)
            if form.is_valid():
                form.save()
            print(form.errors)
            return HttpResponseRedirect('/master')
        else:
            return HttpResponseRedirect('/master')
    else:
        return redirect('login')
