from django.shortcuts import render

# Create your views here.

def condi(request):
    d={'name':'suni','age':22,'marks':60}
    return render(request,'conditions.html',context=d)
