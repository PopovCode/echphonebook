from django.views.generic import TemplateView, CreateView

from . import forms


class HomePageView(TemplateView):
    template_name = 'phonebook/home.html'


class AddPhoneFormView(CreateView):
    template_name = 'phonebook/add_persone.html'
    form_class = forms.CreatePersonForm
