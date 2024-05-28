# myapp/forms.py
from django import forms
from .models import IndexTS

class FilterForm(forms.Form):
    index_symbol = forms.ChoiceField(
        choices=[],
        widget=forms.RadioSelect,
        required=True,
        label="Select Index Symbol"
    )
    date = forms.ChoiceField(
        choices=[],
        widget=forms.Select,
        required=True,
        label="Select Date"
    )

    def __init__(self, *args, **kwargs):
        super(FilterForm, self).__init__(*args, **kwargs)
        self.fields['index_symbol'].choices = self.get_index_symbol_choices()
        self.fields['date'].choices = self.get_date_choices()

    def get_index_symbol_choices(self):
        choices = IndexTS.objects.values_list('index_symbol', 'index_symbol').distinct()
        return choices

    def get_date_choices(self):
        choices = IndexTS.objects.values_list('Date', 'Date').distinct()
        return [(choice[0], choice[0]) for choice in choices]
