import os
os.environ.setdefault('DJANGO_SETTINGS_MODULE','tokoonline.settings')

import django
django.setup()

from toko_app.models import Barang
from faker import Faker 

faker = Faker()

foto = []
nama = []
for i in range(1, 5):
    foto.append('tshirt.png')
    nama.append('baju kaos design bagus','kaos modern masa kini','kaos oblong keren')



def call(n):
    num = 1
    for i in range(n):
        gambar = faker.randomElement(foto)
        nama_barang = faker.randomElement(nama)
        harga = faker.randomNumber(5)
        kategori = faker.randomElement(['baju','music','celana'])
        deskripsi = faker.text()

        Barang.objects.get_or_create(gambar=gambar,nama_barang=nama,harga=harga,kategori=kategori,deskripsi=deskripsi)


if __name__ == '__main__':
  print("Filling Random Data")
  call(10)
  print("Filling Done")
