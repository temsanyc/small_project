from .models import Task
from django.forms import ModelForm,TextInput,Textarea,widgets

class TaskForm(ModelForm):
    class Meta:
        model=Task
        fields=["title","task"]
        widgets= {"title":TextInput( attrs={'class':'form-control','place_holder':'Введите название статьи'}),
                  "task":Textarea(attrs={'class':'form-control','place_holder':'Введите описание статьи'})}

