from .models import Proyectos
from .serializers import ProjectSerializer
from rest_framework import viewsets,permissions

# El viewset nos da los metodos CRUD (Create, Read, Update, Delete)
class ProjectViewSet(viewsets.ModelViewSet):
    queryset = Proyectos.objects.all()
    permission_classes = [permissions.AllowAny]
    # Con esto decimos que cualquier usuario puede ver los proyectos por el AllowAny

    serializer_class = ProjectSerializer
    # Con esto decimos que el serializer que vamos a usar es el que creamos en serializers.py