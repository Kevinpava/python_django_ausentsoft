from django.forms import ModelForm
from .models import Task

from django.forms.widgets import DateInput
from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User

class CustomUserCreationForm(UserCreationForm):
    class Meta:
        model = User
        fields = ('username', 'password1', 'password2')
        widgets = {
            'username': forms.TextInput(attrs={'class': 'form-control'}),
            'password1': forms.PasswordInput(attrs={'class': 'form-control'}),
            'password2': forms.PasswordInput(attrs={'class': 'form-control'}),
        }



class TaskForm(forms.ModelForm):
    paid_vacation = forms.BooleanField(required=False, label='Vacaciones pagas')
    date_range = forms.CharField(widget=forms.TextInput(attrs={'type': 'text', 'class': 'daterange'}), label='Rango de fechas')

    class Meta:
        model = Task
        fields = ['title', 'description', 'paid_vacation', 'date_range']
        widgets = {
            'title': forms.TextInput(attrs={
                'class': 'form-control block w-full px-3 py-2 border border-gray-300 rounded-md shadow-sm focus:outline-none focus:ring-blue-500 focus:border-blue-500 sm:text-sm'}),
            'description': forms.Textarea(attrs={
                'class': 'form-control block w-full px-3 py-2 border border-gray-300 rounded-md shadow-sm focus:outline-none focus:ring-blue-500 focus:border-blue-500 sm:text-sm'}),
        }

    def __init__(self, *args, **kwargs):
        super(TaskForm, self).__init__(*args, **kwargs)
        for field in self.fields.values():
            if not isinstance(field.widget, forms.widgets.DateInput):
                field.widget.attrs.update({'class': 'form-control block w-full px-3 py-2 border border-gray-300 rounded-md shadow-sm focus:outline-none focus:ring-blue-500 focus:border-blue-500 sm:text-sm'})