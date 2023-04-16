from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def hai(request):
    if request.method=='POST':
        un=request.POST['un']
        pw=request.POST['pw']
        print(un)
        print(pw)
        return HttpResponse('Data is submitted successfully')



    return render(request,'hai.html')