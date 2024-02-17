from typing import Any
from django.shortcuts import render
from django.views.generic import (View, TemplateView,
                                  ListView, DetailView,
                                  CreateView, UpdateView, DeleteView)
from . import models
from django.urls import reverse
from django.urls import reverse_lazy



# Create your views here.
class IndexView(TemplateView):
    template_name = 'index.html'
    

class SchoolListView(ListView):
    context_object_name = 'schools'
    model = models.School


class SchoolDetailView(DetailView):
    context_object_name = 'school_detail'
    model = models.School
    template_name = 'basic_app/school_detail.html'


class SchoolCreateView(CreateView):
    template_name = 'basic_app/school_form.html'
    model = models.School
    fields = ['name', 'principal', 'location']

    def get_success_url(self):
        return reverse('basic_app:SclDetail', kwargs={'pk': self.object.pk})
    

class SchoolUpdateView(UpdateView):
    fields = ['name','principal']
    model = models.School


class SchoolDeleteView(DeleteView):
    model = models.School
    success_url = reverse_lazy('basic_app:SclList')
