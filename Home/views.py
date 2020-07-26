from django.shortcuts import render
from django.http import HttpResponseRedirect
from django.views import View
from .forms import ContactForm

# Create your views here.
class Home_view(View):
    template_name = 'Home/Index.html'

    def get(self, request):
        return render(request, self.template_name, {})

class Generic(View):
    template_name = 'Home/generic.html'

    def get(self, request):
        return render(request, self.template_name, {})

def Contact(request):
    if request.method == 'POST':
        form = ContactForm(request.POST )
        if form.is_valid():
            return HttpResponseRedirect('/Thanks/')
    else:
        form = ContactForm()
    