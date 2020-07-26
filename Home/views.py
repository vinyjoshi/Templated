from django.shortcuts import render
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
    form = ContactForm(request.POST or None)
    if form.is_valid():
        form.save()
    
    context = {
        'form' : form,
    }
    return render(request, 'Home/Index.html', context)    
    