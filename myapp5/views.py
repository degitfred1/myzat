from django.shortcuts import render
from .models import music

def jam(request):
    hap1=music.objects.filter(title='wish1')
    hap2=music.objects.filter(title='wish2')
    hap3=music.objects.filter(title='asake')
    hap4=music.objects.filter(title='guc')

    return render(request,'index.html5',{'hap1':hap1,'hap2':hap2,'hap3':hap3,'hap4':hap4})
