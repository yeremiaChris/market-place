import os
os.environ.setdefault('DJANGO_SETTINGS_MODULE','tokoonline.settings')

import django

django.setup()

from toko_app.models import Barang
from faker import Faker

obj=Faker()

def call(n):
    num = 1
    for i in range(n):
        gambar = obj.image()
        nama_barang = obj.name()
        harga = obj.price()
        kategori = obj.category()
        deskripsi = obje.description()

        Barang.objects.get_or_create(gambar=gambar,nama_barang=nama_barang,harga=harga,kategori=kategori,deskripsi=deskripsi)


if __name__ == '__main__':
  print("Filling Random Data")
    call(10)
  print("Filling Done")
