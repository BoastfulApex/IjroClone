from django import forms
from .models import DocsObjects

class CreatePdfForm(forms.Form):
    file = forms.FileField()
    url = forms.CharField(
        widget=forms.TextInput(
            attrs={
                "placeholder": "Document ID si",
                "class": "form-control",
            }
        ))
    document_address = forms.CharField(
        widget=forms.TextInput(
            attrs={
                "placeholder": "Kim tomonidan imzolangan",
                "class": "form-control",
            }
        ))
    who_signed = forms.CharField(
        widget=forms.TextInput(
            attrs={
                "placeholder": "Kim tomonidan imzolangan",
                "class": "form-control",
            }
        ))
    signatory_position = forms.CharField(
        widget=forms.TextInput(
            attrs={
                "placeholder": "Imzolovchi Lavozimi",
                "class": "form-control",
            }
        ))
    signatory_workplace = forms.CharField(
        widget=forms.TextInput(
            attrs={
                "placeholder": "Imzolovchi ish joyi",
                "class": "form-control",
            }
        ))
    performer = forms.CharField(
        widget=forms.TextInput(
            attrs={
                "placeholder": "Ijrochi",
                "class": "form-control",
            }
        ))
    performer_position = forms.CharField(
        widget=forms.TextInput(
            attrs={
                "placeholder": "Ijrochi lavozimi",
                "class": "form-control",
            }
        ))
    performer_workplace = forms.CharField(
        widget=forms.TextInput(
            attrs={
                "placeholder": "Ijrochi ish joyi",
                "class": "form-control",
            }
        ))

    date = forms.DateField(
        widget=forms.DateInput(
            attrs={
                'type': 'date'
            }
        ))

    start_ERI = forms.DateField(
        widget=forms.DateInput(
            attrs={
                'type': 'date'
            }
        ))

    end_ERI = forms.DateField(
        widget=forms.DateInput(
            attrs={
                'type': 'date'
            }
        ))

    given_by_ERI = forms.CharField(
        widget=forms.TextInput(
            attrs={
                "placeholder": "ERI bergan tashkilot",
                "class": "form-control",
            }
        ))

    # class Meta:
    #     model = DocsObjects
    #     fir


class GetPinForm(forms.Form):
    code = forms.CharField(
        widget=forms.TextInput(
            attrs={
                "class": "form-control",
                "id": "repopinmodel-pin_code",
                "aria - required": "true",
            }
        ))
