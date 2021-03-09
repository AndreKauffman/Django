from django.forms import ModelForm
from .models import Transacao


class Forms(ModelForm):
    class Meta:
        model = Transacao
        fields = ['data', 'descricao', 'valor', 'obs', 'categoria']
