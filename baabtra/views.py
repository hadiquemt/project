from django.shortcuts import render

# Create your views here.


def baabtra_home(request):
    return render(request,'baabtraa/baabtrahome.html')


def page2(request):
    return render(request,'baabtraa/page2.html')


def aboutus(request):
    return render(request,'baabtraa/aboutus.html')
    

def css(request):
    return render(request,'baabtraa/css.html')


def css2(request):
    return render(request,'baabtraa/css2.html')


def grid(request):
    return render(request,'baabtraa/grid.html')


def grid2(request):
    return render(request,'baabtraa/grid2.html')


def flex(request):
    return render(request,'baabtraa/flex.html')


def bootstp(request):
    return render(request,'baabtraa/bootstp.html')


def homenew(request):
    return render(request,'baabtraa/homenew.html')


def bootstrpgrd(request):
    return render(request,'baabtraa/bootstrapgrid.html')


def baabtra_newhome(request):
    return render(request,'baabtraa/babtrahomenew.html')



    