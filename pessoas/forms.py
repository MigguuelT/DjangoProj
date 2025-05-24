# pessoas/forms.py
from django import forms
from .models import Pessoa

# Define um formulário ModelForm para o modelo Pessoa.
# ModelForm simplifica a criação de formulários a partir de modelos.
class PessoaForm(forms.ModelForm):
    class Meta:
        # Associa este formulário ao modelo Pessoa.
        model = Pessoa
        # Define quais campos do modelo Pessoa serão incluídos no formulário.
        fields = ['nome', 'idade']
        # Opcional: Adiciona widgets para personalizar a renderização dos campos HTML.
        # Aqui, estamos adicionando classes Tailwind CSS para estilização.
        widgets = {
            'nome': forms.TextInput(attrs={'class': 'mt-1 block w-full rounded-md border-gray-300 shadow-sm focus:border-indigo-500 focus:ring-indigo-500 sm:text-sm p-2'}),
            'idade': forms.NumberInput(attrs={'class': 'mt-1 block w-full rounded-md border-gray-300 shadow-sm focus:border-indigo-500 focus:ring-indigo-500 sm:text-sm p-2'}),
        }
