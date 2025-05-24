# pessoas/serializers.py
from rest_framework import serializers
from .models import Pessoa

# Define um serializer para o modelo Pessoa.
# ModelSerializer simplifica a criação de serializers a partir de modelos.
class PessoaSerializer(serializers.ModelSerializer):
    class Meta:
        # Associa este serializer ao modelo Pessoa.
        model = Pessoa
        # Define quais campos do modelo Pessoa serão incluídos na serialização.
        fields = ['id', 'nome', 'idade'] # 'id' é geralmente incluído para referência
