from django.shortcuts import render,redirect

from .forms import BarangForm
from django.forms import modelformset_factory
from .models import Image,Barang


# Create your views here.
def index(request):
    barang = Barang.objects.all()
    return render(request,'toko_app/index.html',{'barang': barang})

def tambah_barang(request):
    form = BarangForm()
    formset = modelformset_factory(Image,extra=3,fields=('image',))
    if request.method == 'POST':
        form = BarangForm(request.POST or None,request.FILES or None)
        formset = formset(request.POST or None,request.FILES or None) 
        if form.is_valid() and formset.is_valid():
            item = form.save(commit=False)
            item.save()

            for f in formset:
                try:
                    gambar = Image(barang=item,image=f.cleaned_data['image'])
                    gambar.save()
                except Exception as e:
                    break       
        return redirect('index')
    else:
        form = BarangForm()
        formset = formset(queryset=Image.objects.none())

    return render(request,'toko_app/tambah_barang.html',{'form': form,'formset': formset})
