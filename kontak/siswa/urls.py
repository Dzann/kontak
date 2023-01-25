from django.urls import path

from . import views

app_name = 'siswa'

urlpatterns = {
    path('', views.siswa, name='siswa'),
    path('siswa/', views.DataSiswa.as_view(), name='siswas')
}