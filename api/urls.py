from django.urls import path, include
from .views import local_view, objeto_view, usuario_view, busca_local_view, logout_view, objetos_local_view, imagem_objeto_view, objeto_dono_view, inicio_view, imagem_local_view
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView

urlpatterns = [
    path('', inicio_view.Inicio.as_view(), name='inicio-list'),
    path('locais', local_view.LocalList.as_view(), name='local-list'),
    path('locais/<int:local_id>', local_view.LocalDetalhes.as_view(), name='local-detalhes'),
    path('locais/imagem', imagem_local_view.ImagemLocalList.as_view(),
         name='imagem-local-detalhes'),
    path('locais/busca', busca_local_view.BuscaLocal.as_view(), name='busca-local-list'),
    path('locais/<int:local_id>/objetos', objetos_local_view.ObjetosLocalID.as_view(), name='objetos-local'),
    path('objetos', objeto_view.ObjetoList.as_view(), name='objeto-list'),
    path('objetos/<int:objeto_id>', objeto_view.ObjetoDetalhes.as_view(), name='objeto-detalhes'),
    path('objetos/<int:objeto_id>/imagem', imagem_objeto_view.ImagemObjetoList.as_view(), name='imagem-objeto-detalhes'),
    path('objetos/<int:objeto_id>/donos', objeto_dono_view.ObjetosDonoID.as_view(), name='objeto-dono-detalhes'),
    path('usuarios', usuario_view.UsuarioList.as_view(), name='usuario-list'),
    path('auth/login', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('auth/token/refresh', TokenRefreshView.as_view(), name='token_refresh'),
    path('auth/logout', logout_view.Logout.as_view(), name='logout-list')

]