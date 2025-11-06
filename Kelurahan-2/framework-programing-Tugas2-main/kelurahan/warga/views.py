from django.shortcuts import render
from django.views.generic import ListView
from django.views.generic import DetailView
from .models import Warga, Pengaduan
from django.urls import reverse_lazy
from django.views.generic import ListView, DetailView, CreateView
from .forms import PengaduanForm

from .models import Warga, Pengaduan
from .forms import WargaForm 


class WargaListView(ListView):
    model = Warga

class WargaDetailView(DetailView):
    model = Warga

class PengaduanListView(ListView):
    model = Pengaduan

class WargaCreateView(CreateView):
    model = Warga
    form_class = WargaForm
    template_name = 'warga/warga_form.html'
    success_url = reverse_lazy('warga-list')

class PengaduanCreateView(CreateView):
    model = Pengaduan
    form_class = PengaduanForm
    template_name = 'warga/pengaduan_form.html'
    success_url = reverse_lazy('daftar_pengaduan')
    