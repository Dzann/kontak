from django.views.generic import ListView, DetailView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy
from django.shortcuts import render
from .models import DataSiswa

class DataSiswa(ListView):
    queryset = DataSiswa.objects.all()

def siswa(request):
    return render(request, "pageSiswa/dataSiswa_list.html")

class tambahSiswa(CreateView):
    model = DataSiswa
    fields = '__all__'
    success_url = reverse_lazy('siswa:siswa')