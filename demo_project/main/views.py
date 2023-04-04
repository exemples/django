from django.shortcuts import render
from django.views.generic import TemplateView
# Create your views here.

def index(request):
    return render(request, 'main/index.html')


# Class based Views

class HomeView(TemplateView):
    template_name = "main/index.html"
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        print('-------------------', context)
        context['app_name'] = 'School Support Management'
        return context
    