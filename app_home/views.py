from django.shortcuts import render

def home(request):
    return render(request,'first.html')
def greentea(request):
    return render(request, 'greentea.html')
def LGV50(request):
    return render(request, 'LGV50.html')
def LIKELION(request):
    return render(request, 'LIKELION.html')
# Create your views here.
