from django.shortcuts import render, get_object_or_404, redirect
from django.views.generic import TemplateView
from django.contrib.auth.decorators import login_required
from django.utils.decorators import method_decorator
from .models import Publicaciones
from .forms import BibliotecaForms
# Create your views here.


class ListaBiblioteca(TemplateView):
    template_name = "biblioteca.html"

    def get_context_data(self, **kwargs):
        context = super(ListaBiblioteca, self).get_context_data(**kwargs)
        context['biblioteca_list'] = Publicaciones.objects.all()
        return context

@login_required
def bibliotecas_personales(request, template='admin/biblioteca_list_admin.html'):
    object_list = Publicaciones.objects.filter(user_id=request.user.id)

    return render(request, template, locals())

@login_required
def crear_biblioteca(request, template='admin/biblioteca_admin.html'):
    if request.method == 'POST':
        form = BibliotecaForms(request.POST, files=request.FILES)

        if form.is_valid():
            form_uncommited = form.save(commit=False)
            form_uncommited.user = request.user
            form_uncommited.save()

            form.save_m2m()

            #thread.start_new_thread(notify_all_notas, (form_uncommited,))
            return redirect('biblioteca')
    else:
        form = BibliotecaForms()

    return render(request, template, locals())

@login_required
def biblioteca_editar(request, id, template='admin/biblioteca_admin.html'):
    object = get_object_or_404(Publicaciones, id=id)

    if request.method == 'POST':
        form = BibliotecaForms(request.POST, request.FILES, instance=object)

        if form.is_valid() :
            form_uncommited = form.save(commit=False)
            form_uncommited.user = request.user
            form_uncommited.save()

            form.save_m2m()

            return redirect('biblioteca')
    else:
        form = BibliotecaForms(instance=object)

    return render(request, template, locals())

@login_required
def eliminar_biblioteca(request, id):
    nota = Publicaciones.objects.filter(id = id).delete()
    return redirect('biblioteca')
