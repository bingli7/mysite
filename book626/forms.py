from django.forms import ModelForm
from .models import BasicInfo


class BasicInfoForm(ModelForm):

    class Meta:
        model = BasicInfo
        fields = '__all__'
