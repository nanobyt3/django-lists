from django import forms
from .models import Lists
from .models import List
from crispy_forms.helper import FormHelper


class ListsForm(forms.ModelForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.helper = FormHelper(self)
        self.helper.form_tag = False
    class Meta:
        model = Lists
        fields = "__all__"


class ListForm(forms.ModelForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.helper = FormHelper(self)
        self.helper.form_tag = False
    class Meta:
        model = List
        fields = "__all__"


