from django.shortcuts import render

# Create your views here.
def jinja1(request):
    d={'name':'sandy','age':18}
    return render(request,'jinja1.html',d)