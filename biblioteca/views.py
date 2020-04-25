from django.shortcuts import render
from django.views.generic import TemplateView
from .models import Publicaciones

# Create your views here.


class ListaBiblioteca(TemplateView):
    template_name = "biblioteca.html"

    def get_context_data(self, **kwargs):
        context = super(ListaBiblioteca, self).get_context_data(**kwargs)
        context['biblioteca_list'] = Publicaciones.objects.all()
        return context
