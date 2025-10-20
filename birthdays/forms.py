from django import forms
from .models import Student

class StudentBirthdayForm(forms.ModelForm):
    birth_day = forms.ChoiceField(
        choices=[(i, i) for i in range(1, 32)],
        widget=forms.Select(attrs={
            'class': 'form-select',
            'required': True
        })
    )
    
    class Meta:
        model = Student
        fields = [
            'full_name', 'email', 'phone_number', 'gender',
            'birth_month', 'birth_day', 'level', 'alias',
            'profile_picture', 'held_office', 'office_position'
        ]
        widgets = {
            'full_name': forms.TextInput(attrs={
                'class': 'form-input',
                'placeholder': 'Enter your full name',
                'required': True
            }),
            'email': forms.EmailInput(attrs={
                'class': 'form-input',
                'placeholder': 'Email address (optional)'
            }),
            'phone_number': forms.TextInput(attrs={
                'class': 'form-input',
                'placeholder': 'WhatsApp number',
                'required': True
            }),
            'gender': forms.RadioSelect(attrs={
                'class': 'form-radio'
            }),
            'birth_month': forms.RadioSelect(attrs={
                'class': 'month-radio'
            }),
            'level': forms.RadioSelect(attrs={
                'class': 'level-radio'
            }),
            'alias': forms.TextInput(attrs={
                'class': 'form-input',
                'placeholder': 'Nickname (optional)'
            }),
            'profile_picture': forms.FileInput(attrs={
                'class': 'form-file',
                'accept': 'image/*'
            }),
            'held_office': forms.CheckboxInput(attrs={
                'class': 'form-checkbox'
            }),
            'office_position': forms.TextInput(attrs={
                'class': 'form-input',
                'placeholder': 'Position held (if applicable)'
            })
        }
    
    def clean_birth_day(self):
        day = self.cleaned_data.get('birth_day')
        return int(day)