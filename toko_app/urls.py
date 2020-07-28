from django.urls import path

from . import views


urlpatterns = [
    path('',views.index,name='index'),
    path('tambah-barang/',views.tambah_barang,name='tambah-barang'),
]
