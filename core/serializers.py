from rest_framework import serializers
from core.models import Inventario, Categoria

class InventarioSerializer(serializers.ModelSerializer):
    class Meta:
        model = Inventario
        fields = ['id_inventario', 'modelo', 'talla', 'valor', 'categoria', 'imagen']
        
class CategoriaSerializer(serializers.ModelSerializer):
    class Meta:
        model = Categoria
        fields = ['id_categoria', 'nombre_categoria']