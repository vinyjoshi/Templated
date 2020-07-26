from django.shortcuts import render
from django.views import View

# Create your views here.
class Gallery(View):
    template_name = 'Gallery/gallery.html'

    def get(self, request):
        return render(request, self.template_name, {})
