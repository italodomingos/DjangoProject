from django.urls import path
from .views import HomePage, HomeFilmes, DetalhesFilmes, PesquisaFilmes, EditarPerfil, CriarConta
from django.contrib.auth import views as auth_view
app_name = 'filme'

urlpatterns = [
    path('', HomePage.as_view(), name='hompage'),
    path('filmes/', HomeFilmes.as_view(), name='homefilmes'),
    path('filmes/<int:pk>', DetalhesFilmes.as_view(), name='detalhesfilmes'),
    path('pesquisa_filmes/', PesquisaFilmes.as_view(), name='pesquisafilme'),
    path('login/', auth_view.LoginView.as_view(template_name='login.html'), name='login'),
    path('logout/', auth_view.LogoutView.as_view(template_name='home_page.html'), name='logout'),
    path('editar_perfil', EditarPerfil.as_view(template_name="editar_perfil.html"), name="editar_perfil"),
    path('criar_conta', CriarConta.as_view(template_name="criar_conta.html"), name="criar_conta"),

]


