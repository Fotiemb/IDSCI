from django.http import HttpResponseRedirect
from django.shortcuts import render
from django.views.generic import ListView, TemplateView
from tablib import Dataset

from accounts.models import Data
from apps.forms import profilStudentForm
from apps.models import ProfilStudent, BookModel


class loginPage(ListView):
    model = Data
    template_name = "loginPage.html"
    context_object_name = 'datas'

    def get_queryset(self):
        return super().get_queryset()


class HomeView(TemplateView):
    template_name = "apps/dashboard.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["book"] = BookModel.objects.all()
        print(context)
        return context


def profile(request):
    if request.method == 'POST':
        form = profilStudentForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect('/dash/profile')
    else:
        form = profilStudentForm()
    return render(request, 'apps/profile.html', {'form': form, "data": ProfilStudent.objects.all()})


def book(request):
    return render(request, 'apps/book.html')


def message(request):
    return render(request, 'apps/message.html')


def aide(request):
    return render(request, 'apps/aide.html')


def reserver(request):
    return render(request, 'apps/book_reservation.html')
