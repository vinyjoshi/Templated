from django.shortcuts import render
from django.views import View

# Create your views here.
class Home_view(View):
    template_name = 'Home/Index.html'

    def get(self, request):
        return render(request, self.template_name, {})