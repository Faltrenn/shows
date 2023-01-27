from django.shortcuts import render, redirect
from .models import Shows
from django.http.request import HttpRequest

from django.http import JsonResponse


from django.contrib.auth import authenticate, logout as logoutt, login as loginn

from pyUFbr.baseuf import ufbr

estados = ufbr.list_uf

# Create your views here.

def index(request: HttpRequest):
    return render(request, "index.html")

def list(request: HttpRequest):
    shows = Shows.objects.all()
    return render(request, "list.html", context={"title": "Listagem", "shows": shows})

def search(request: HttpRequest):
    showsFounded = None
    if request.GET:
        showsFounded = Shows.objects.filter(banda__icontains=request.GET.get("bandaName"))
    return render(request, "search.html", context={"title": "Consulta", "showsFounded": showsFounded})

def crud(request: HttpRequest):
    if not request.user.is_authenticated:
        return redirect("login")
    shows = Shows.objects.all()
    return render(request, "crud.html", context={"title": "Crud", "shows": shows})

def about(request: HttpRequest):
    return render(request, "about.html", context={"title": "Sobre"})

def login(request: HttpRequest):
    if request.POST:
        user = authenticate(
            username=request.POST.get("username"),
            password=request.POST.get("password")
        )
        if user is not None:
            loginn(request, user)
            return redirect("crud")
    return render(request, "login.html", context={"title": "login"})

def logout(request: HttpRequest):
    logoutt(request)
    return redirect("list")

def createShow(request: HttpRequest):
    if request.POST:
        Shows.objects.create(
            banda = request.POST.get("banda"),
            local = request.POST.get("local"),
            estado = request.POST.get("estado"),
            cidade = request.POST.get("cidade"),
            data = request.POST.get("data")
        )
        return redirect("crud")
    return render(request, "showForm.html", context={"estados": estados, "cidades": ufbr.list_cidades(estados[0])})

def editShow(request: HttpRequest, show_id):
    if show_id:
        try:
            show = Shows.objects.filter(pk=show_id).get()
            if request.POST:
                show.banda = request.POST.get("banda")
                show.local = request.POST.get("local")
                show.estado = request.POST.get("estado")
                show.cidade = request.POST.get("cidade")
                show.data = request.POST.get("data")
                show.save()
                return redirect("crud")
            
            show.data = show.data.strftime('%Y-%m-%d')
            return render(request, "showForm.html", context={"estados": estados, "cidades": ufbr.list_cidades(show.estado), "show": show})
        except:
            print("Show inválido")
            return redirect("crud")
    return redirect("crud")

def deleteShow(request: HttpRequest, show_id):
    if request.user.is_authenticated:
        try:
            show = Shows.objects.filter(pk=show_id).get()
            show.delete()
            return redirect("crud")
        except:
            print("Show inválido")
            return redirect("crud")
    return redirect("crud")

def getCities(request):
    data = {"cidades": ufbr.list_cidades(request.POST.get("estado"))}
    return JsonResponse(data)
