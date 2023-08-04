from django.http import HttpResponse
from django.shortcuts import render


# Create your views here.
def demo(request):

    return render(request,"index.html")

#def addition(request):
    #x=int(request.GET['no1'])
   # y=int(request.GET['no2'])
   # res=x+y
   # return render(request,"result.html",{'result':res})



 #def substract(request):
   # a=int(request.GET['num1'])
   # b=int(request.GET['num2'])
   # c=a-b
   # return render(request,"Answer.html",{'Answer':c})

 #def multiplication(request):
  #  e=int(request.GET['m1'])
   # f=int(request.GET['m2'])
    #g=e*f
   # return render(request,"mulans.html",{'Answer':g})

 #def division(request):
  #  h=int(request.GET['d1'])
   # i=int(request.GET['d2'])
    #j=h/i
    #return render(request,"divans.html",{'Answer':j})