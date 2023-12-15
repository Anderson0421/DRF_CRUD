from rest_framework import routers
from .api import ProjectViewSet
# Este modelo routers nos permite crear las rutas de nuestra API de manera automatica 

router = routers.DefaultRouter()

# Este router register espera como parametro la ruta y el viewset que queremos registrar
# y opcionalmente un nombre para la ruta

router.register('api/project/v1',ProjectViewSet, 'projects')


urlpatterns = router.urls