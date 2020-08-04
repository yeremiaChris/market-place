import os

os.environ.setdefault('DJANGO_SETTINGS_MODULE','tokoonline.settings')

import django
django.setup()

from toko_app.models import Barang
from faker import Faker
import random


faker = Faker();

image = ['/gambar/tshirt.png', '/gambar/lll_1JTlvcb.jpg', '/gambar/celana.jpeg']
nama_barang = ['baju keren kali','musicnya sangat keren','celana motif keren']
jenis = ['baju','celana','musik']

def call(n):
    for i in range(n):
        gambar = faker.random.choice(image)
        nama = faker.random.choice(nama_barang)
        harga = faker.random.randint(1000,100000)
        kategori = faker.random.choice(jenis)
        deskripsi = faker.text()

        Barang.objects.get_or_create(gambar=gambar,nama_barang=nama,harga=harga,kategori=kategori,deskripsi=deskripsi)



if __name__ == '__main__':
    print('membuat random data')
    call(90)
    print('mengisi selesai')
