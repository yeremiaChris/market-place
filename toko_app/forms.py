from django import forms

from .models import Barang

class BarangForm(forms.ModelForm):
    class Meta:
        model = Barang
        fields = ['gambar','nama_barang','harga','kategori','deskripsi']
        widgets = {
            'kategori': forms.Select(attrs={'class': 'js-example-basic-single'}),
            'deskripsi': forms.Textarea(attrs={'cols': '96','rows': '10'})
        }


class UpdateBarang(forms.ModelForm):
    class Meta:
        model = Barang
        fields = ['gambar', 'nama_barang', 'harga', 'kategori', 'deskripsi']
        widgets = {
            'kategori': forms.Select(attrs={'class': 'js-example-basic-single'}),
            'deskripsi': forms.Textarea(attrs={'cols': '96', 'rows': '10'})
        }
    
    def save(self,commit=True):
        barang = self.instance
        barang.nama_barang = self.cleaned_data['nama_barang']
        barang.harga = self.cleaned_data['harga']
        barang.kategori = self.cleaned_data['kategori']
        barang.deskripsi = self.cleaned_data['deskripsi']

        if self.cleaned_data['gambar']:
            barang.gambar = self.cleaned_data['gambar']

        if commit:
           barang.save()
        return barang




