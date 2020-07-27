from django.shortcuts import render
from django.views import View
from .forms import ContactForm
from django.http import HttpResponseRedirect

# Create your views here.
class Home_view(View):
    form_class = ContactForm
    template_name = 'Home/Index.html'

    def get(self, request):
        form = self.form_class()
        return render(request, self.template_name, {'form':form})

    def post(self, request):
        form = self.form_class(request.POST)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect('/')
        

class Generic(View):
    template_name = 'Home/generic.html'

    def get(self, request):
        return render(request, self.template_name, {})
  
    

