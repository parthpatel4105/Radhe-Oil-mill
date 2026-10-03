from django.contrib import messages
from django.shortcuts import redirect, render

from .forms import ContactForm


def radhe_home(request):
    return render(request, 'store/radhe_home.html')


def about(request):
    return render(request, 'store/about.html')


def contact(request):
    if request.method == 'POST':
        form = ContactForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, "Thanks! We've received your message and will get back to you soon.")
            return redirect('contact')
    else:
        form = ContactForm()
    return render(request, 'store/contact.html', {'form': form})
