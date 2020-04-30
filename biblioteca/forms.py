# -*- coding: utf-8 -*-
from django import forms
from models import *

from ckeditor_uploader.widgets import CKEditorUploadingWidget


class BibliotecaForms(forms.ModelForm):
    descripcion = forms.CharField(widget=CKEditorUploadingWidget())
    titulo = forms.CharField(widget=forms.TextInput(attrs={'class':'span7','rel':"tooltip", 'title':"Tratar de redactar títulos resumidos"}))
    #adjunto = forms.FileField(required=True)
    class Meta:
        model = Publicaciones
        exclude = ('slug','fecha','user',)
