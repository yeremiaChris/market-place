from django.db import models

# Create your models here.
class Barang(models.Model):
    gambar = models.ImageField(upload_to='gambar')
    nama_barang = models.CharField(max_length=50)
    harga = models.DecimalField(decimal_places=2,max_digits=8)
    CATEGORY = [
        ('baju','baju'),
        ('celana','celana'),
        ('musik','musik')
    ]
    kategori = models.CharField(choices=CATEGORY,max_length=50)
    deskripsi = models.TextField()

    
    def __str__(self):
        return self.nama_barang

class Image(models.Model):
    barang = models.ForeignKey(Barang,on_delete=models.CASCADE)
    image = models.ImageField(upload_to='gambar')

    def __str__(self):
        return self.barang.nama_barang