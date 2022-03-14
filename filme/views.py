from django.shortcuts import render, reverse
from django.views.generic import TemplateView, DetailView, ListView, FormView
from .models import Filme
from django.contrib.auth.mixins import LoginRequiredMixin
from .forms import CriarContaForm

# Create your views here.


class HomePage(TemplateView):
    template_name = "home_page.html"

    def get(self, request, *args, **kwargs):
        if request.user.is_authenticated:
            return render(request, 'home_filmes.html')
        else:
            return super().get(request, *args, **kwargs)


class HomeFilmes(LoginRequiredMixin, ListView):
    template_name = "home_filmes.html"
    model = Filme


class PesquisaFilmes(LoginRequiredMixin, TemplateView):
    template_name = "pesquisa_filme.html"

    def get_context_data(self, **kwargs):
        context = super(PesquisaFilmes, self).get_context_data(**kwargs)
        pesquisa_filmes = Filme.objects.filter(titulo__icontains=self.request.GET.get("query"))
        context["pesquisa_filmes"] = pesquisa_filmes
        return context


class DetalhesFilmes(LoginRequiredMixin, DetailView):
    template_name = "detalhes_filmes.html"
    model = Filme

    def get(self, request, *args, **kwargs):
        filme = self.get_object()
        filme.visualizacoes += 1
        filme.save()
        request.user.filmes_visto.add(filme)
        return super().get(request, *args, **kwargs)

    def get_context_data(self, **kwargs):
        context = super(DetalhesFilmes, self).get_context_data(**kwargs)
        filmes_relacionados = Filme.objects.filter(categoria=self.get_object().categoria)[0:5]
        context["filmes_relacionados"] = filmes_relacionados
        return context


class EditarPerfil(LoginRequiredMixin, TemplateView):
    template_name = "editar_perfil.html"


class CriarConta(FormView):
    template_name = "criar_conta.html"
    form_class = CriarContaForm

    def form_valid(self, form):
        form.save()
        return super().form_valid(form)

    def get_success_url(self):
        return reverse("filme:login")


