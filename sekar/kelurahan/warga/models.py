from django.db import models
from django import forms

class Warga(models.Model):
    nik = models.CharField(max_length=16, unique=True, verbose_name="Nomor induk kependudukan")
    nama_lengkap = models.CharField(max_length=100, verbose_name="Nama lengkap")
    alamat = models.TextField(verbose_name="Alamat tinggal")
    no_telepon = models.CharField(max_length=15, blank=True, verbose_name="nomer telepon")
    tanggal_registrasi = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.nama_lengkap


class Pengaduan(models.Model):
    STATUS_CHOICES = [
        ('BARU', 'Baru'),
        ('DIPROSES', 'Diproses'),
        ('SELESAI', 'Selesai'),
    ]
    
    judul = models.CharField(max_length=200)
    deskripsi = models.TextField()
    status = models.CharField(max_length=10, choices=STATUS_CHOICES, default='BARU')
    tanggal_lapor = models.DateTimeField(auto_now_add=True)
    
    # Kunci relasinya ada di sini!
    pelapor = models.ForeignKey(Warga, on_delete=models.CASCADE, related_name='pengaduan')

    def __str__(self):
        return self.judul

class WargaForm(forms.ModelForm):
    class Meta:
        model = Warga
        fields = ['nik', 'nama_lengkap', 'alamat', 'no_telepon']