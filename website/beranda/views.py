from django.shortcuts import render

# Create your views here.
def index(request):
    context ={
        'nama': 'Data Mahasiswa',
    }
    return render(request, 'index.html', context) 