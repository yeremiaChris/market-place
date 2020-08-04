from django.shortcuts import render,redirect

from .forms import BarangForm,UpdateBarang
from django.forms import modelformset_factory
from .models import Image,Barang

from django import forms

from django.shortcuts import get_object_or_404

from django.contrib import messages
from django.core.paginator import Paginator





# Create your views here.
def index(request):
    barang = Barang.objects.filter(kategori='baju')
    celana = Barang.objects.filter(kategori='celana')
    musik = Barang.objects.filter(kategori='musik')
    return render(request,'toko_app/index.html',{'baju': barang,'musik': musik,'celana': celana})



def tambah_barang(request):
    form = BarangForm()
    formset = modelformset_factory(Image,extra=4,fields=('image',),widgets={
        'image': forms.ClearableFileInput(attrs={'class': 'coba'})  
    })
    if request.method == 'POST':
        form = BarangForm(request.POST or None,request.FILES or None)
        formset = formset(request.POST or None,request.FILES or None) 
        if form.is_valid() and formset.is_valid():
            item = form.save(commit=False)
            item.save()
            messages.success(request,'Barang berhasil di tambahkan ')
            for f in formset:
                try:
                    gambar = Image(barang=item,image=f.cleaned_data['image'])
                    gambar.save()
                except Exception as e:
                    break       
            
        return redirect('daftar-barang')
    else:
        form = BarangForm()
        formset = formset(queryset=Image.objects.none())

    return render(request,'toko_app/tambah_barang.html',{'form': form,'formset': formset})


def daftar_barang(request):
    barang = Barang.objects.all().order_by('-id')
    paginator = Paginator(barang,5)
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)
    return render(request, 'toko_app/daftar.html', {'barang': barang,'page_obj': page_obj})

def update_barang(request,pk):
    barang = get_object_or_404(Barang,id=pk)
    form = UpdateBarang(instance=barang)
    formset = modelformset_factory(Image, extra=4, fields=('image',), widgets={
        'image': forms.ClearableFileInput(attrs={'class': 'coba'})
    })
    if request.method == 'POST':
        form = UpdateBarang(request.POST,request.FILES,instance=barang)
        formset = formset(request.POST or None, request.FILES or None)
        if form.is_valid() and formset.is_valid():
            item = form.save(commit=False)
            item.save()
            print(formset.cleaned_data)

            for f in formsetL:
                if f.cleaned_data:
                    if f.cleaned_data['id'] is None:
                        gambar = Image(barang=item,image=f.cleaned_data['image'])
                        gambar.save()


            return redirect('daftar-barang')
    else:
        form = UpdateBarang(instance=barang)
    return render(request,'toko_app/update.html',{'form': form,'formset': formset})


def delete_barang(request,pk):
    barang = get_object_or_404(Barang,id=pk)
    if request.method == 'POST':
        barang.delete()
        return redirect('daftar-barang')
    return render(request,'toko_app/delete.html',{'form': barang})
