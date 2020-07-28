import os
os.environ['DJANGO_SETTINGS_MODULE'] = 'tokoonline.settings'

import django
django.setup()

from toko_app.models import Barang
from faker import Faker 

faker = Faker()

import random

baju = ['gambar/tshirt.png', 'gambar/sayur_YsP4jSz.png']
nama = ['kaos oblong ','sape bahan jati']
jenis = ['baju', 'music', 'celana']
def call(n):
    num = 1
    for i in range(n):
        gambar = faker.random.choice(baju)
        nama_barang = faker.random.choice(nama)
        harga = faker.random.randint(1,5)
        kategori = faker.random.choice(jenis)
        deskripsi = faker.text()

        Barang.objects.get_or_create(gambar=gambar,nama_barang=nama,harga=harga,kategori=kategori,deskripsi=deskripsi)


if __name__ == '__main__':
  print("Filling Random Data")
  call(100)
  print("Filling Done")
