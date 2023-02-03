from django.http import HttpResponseRedirect
from django.shortcuts import render
from django.views.generic import ListView, CreateView
from tablib import Dataset
from accounts.models import Data, CustomUser
from accounts.resources import dataResource


def importExcel(request):
    if request.method == 'POST':
        per_res = dataResource()
        dataset = Dataset()
        new_persons = request.FILES['my_file']
        imported_data = dataset.load(new_persons.read(), format='xlsx')
        for data in imported_data:
            value = Data(
                data[0],
                data[1],
                data[2],
            )
            value.save()

    return render(request, "accounts/form.html")


class login(ListView):
    model = Data
    # template_name = "accounts/login.html"
    context_object_name = 'data'

    """def get_queryset(self):
        return super().get_queryset()"""


def signup(request):
    if request.method == "POST":
        if len(request.POST) == 5:
            return _extracted_from_signup_(request)
        if len(request.POST) == 3:
            # print(request.POST)
            username = request.POST.get("username")
            password = request.POST.get("password")
            inscrit = [str(i) for i in CustomUser.objects.all()]
            if username.lstrip().rstrip() in inscrit:
                return HttpResponseRedirect("dash/dashboard/")
            else:
                return render(request, "accounts/login.html", {"error": "Login invalide", "ema": CustomUser.objects.all()})
    return render(request, 'accounts/login.html', {"d": Data.objects.all(), "ema": CustomUser.objects.all()})


# TODO Rename this here and in `signup`
def _extracted_from_signup_(request):
    username = request.POST.get("username")
    if username == "":
        return render(request, "accounts/login.html", {"error": " Nom invalide", "d": Data.objects.all()})
    email = request.POST.get("email")
    if email:
        cut = email.split('@')
        if cut[-1] != 'inphb.ci':
            return render(request, "accounts/login.html", {"error": "Email invalide"})
    if telephone := request.POST.get("telephone"):
        if len(telephone) != 10:
            return render(request, "accounts/login.html", {"error": "Numero pas valide"})
    password = request.POST.get("password")
    if len(password) < 6:
        return render(request, "accounts/login.html", {"error": "Mot de passe court"})
    CustomUser.objects.create_user(username=username, password=password, email=email, telephone=telephone)
    return render(request, "accounts/login.html", {"success": "inscrition réussie"})
