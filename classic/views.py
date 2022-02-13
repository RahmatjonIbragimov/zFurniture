from django.shortcuts import render
from .models import * 
from django.views.generic import ListView

class BlockPageView(ListView):
    model = Block
    template_name = 'index.html'
    paginate_by = 4


class ShowByCategoryView(ListView):
    model = Category
    template_name = 'index.html'
    #error bermaslik uchun
    allow_empty = False
    #object_list => category_list 
    context_object_name = 'category_list'


    def get_queryset(self):
        return Block.objects.filter(category__slug=self.kwargs['slug'])

class CategoryView(ListView):
    template_name = 'index.html '
    allow_empty = True


    def get_queryset(self):
        return Block.objects.filter(category__slug=self.kwargs['slug'])

class  SingleView ( ListView ): 
    model  =  Post 
    template_name  =  'single.html'

class  ArchiveView ( ListView ): 
    model  =  archive 
    template_name  =  'archive.html'

class  ContactView ( ListView ): 
    model  =  contact 
    template_name  =  'contact.html'


