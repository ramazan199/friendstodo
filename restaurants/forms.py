from django import forms

from .models import Todo
from .validators import validate_category
  


class TodoCreateForm(forms.ModelForm):
    #email           = forms.EmailField()
    #category         = forms.CharField(required=False, validators=[validate_category])
    class Meta:
        model = Todo
        fields = [
            'name',          
            'slug',
        ]

    def clean_name(self):
        name = self.cleaned_data.get("name")
        if name == "Hello":
            raise forms.ValidationError("Not a valid name")
        return name


