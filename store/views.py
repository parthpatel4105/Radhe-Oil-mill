from django.shortcuts import render


def radhe_home(request):
    return render(request, 'store/radhe_home.html')
