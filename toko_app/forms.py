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

