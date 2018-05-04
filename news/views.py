from django.shortcuts import render, redirect
from django.views.generic.dates import ArchiveIndexView
from django.views.generic.detail import DetailView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from news.models import New
from generic.mixins import CategoryListMixin, PageNumberMixin
from generic.controllers import PageNumberView
from django.urls import reverse_lazy
from django.contrib.messages.views import SuccessMessageMixin
from django.contrib import messages

# Create your views here.


class NewListView(ArchiveIndexView, CategoryListMixin):
    model = New
    fields = "__all__"
    date_field = "posted"
    template_name = "news_index.html"
    paginate_by = 10
    allow_empty = True
    allow_future = True


class NewDetailView(DetailView):
    model = New
    fields = "__all__"
    template_name = "new.html"


class NewCreate(CategoryListMixin, SuccessMessageMixin, CreateView):
    model = New
    fields = "__all__"
    template_name = "new_add.html"
    success_url = reverse_lazy("news_index")
    success_message = "Новость успешно добавлена"


class NewUpdate(SuccessMessageMixin, UpdateView, PageNumberView, PageNumberMixin):
    model = New
    fields = "__all__"
    template_name = "new_edit.html"
    success_url = reverse_lazy("news_index")
    success_message = "Новость успешно изменена"


class NewDelete(DeleteView, PageNumberMixin, PageNumberView):
    model = New
    template_name = "new_delete.html"
    success_url = reverse_lazy("news_index")

    def post(self, request, *args, **kwargs):
        messages.add_message(request, messages.SUCCESS, "Новость успешно удалена")
        return super(NewDelete, self).post(request, *args, **kwargs)
