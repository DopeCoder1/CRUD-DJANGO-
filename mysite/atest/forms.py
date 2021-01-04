from .models import Atestation
from django.forms import ModelForm,TextInput

class AtestationForm(ModelForm):
    class Meta:
        model = Atestation
        fields = ['fio','student_card','gpa']

        widgets = {
            'fio': TextInput(attrs={
                'class':'form-control',
                'placeholder':'FIO:'
            }),

            'student_card' : TextInput(attrs={
                'class' : 'form-control',
                'placeholder' : 'ID:'
            }),

            'gpa' : TextInput(attrs={
                'class' : 'form-control',
                'placeholder' : 'GPA:'
            })
        }
