from django.urls import path

from . import views


urlpatterns = [
    path('',views.index,name='index'),
    path('tambah-barang/',views.tambah_barang,name='tambah-barang'),
    path('daftar-barang/',views.daftar_barang,name='daftar-barang'),
    path('update-barang/<str:pk>/',views.update_barang,name='update-barang'),
    path('daftar-barang/delete-barang/<str:pk>/',views.delete_barang,name='delete-barang'),
]
