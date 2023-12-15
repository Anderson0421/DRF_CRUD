#Importar serializers , este nos sirve para convertir los modelos en JSON
from rest_framework import serializers
from .models import Proyectos

#Creacion de la clase ProjectSerializer

# Es parecido a un formulario de django
class ProjectSerializer(serializers.ModelSerializer):
    class Meta:
        model = Proyectos
        fields = ('id','title', 'description', 'technology','created_at')
        read_only_fields = ('created_at',) # Esto es para que no se pueda modificar la fecha de creacion
        