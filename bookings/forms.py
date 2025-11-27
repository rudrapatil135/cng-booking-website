from django import forms
from .models import ConnectionRequest, PaymentDetail

class ConnectionRequestForm(forms.ModelForm):
    class Meta:
        model = ConnectionRequest
        fields = ['name', 'contact_number', 'age', 'gender', 'address', 'idproof']

class PaymentForm(forms.ModelForm):
    class Meta:
        model = PaymentDetail
        fields = ['card_holder', 'card_number', 'exp_month', 'exp_year', 'cvv']
        widgets = {
            'cvv': forms.PasswordInput(attrs={'maxlength': '3', 'inputmode': 'numeric', 'pattern': '[0-9]*'}),
            'card_number': forms.TextInput(attrs={'maxlength': '16', 'inputmode': 'numeric', 'pattern': '[0-9]*'}),
        }

    def clean_card_number(self):
        card_number = self.cleaned_data.get('card_number', '').replace(" ", "")  # Remove spaces
        if not card_number.isdigit() or len(card_number) != 16:
            raise forms.ValidationError("Enter a valid 16-digit card number.")
        return card_number

    def clean_cvv(self):
        cvv = self.cleaned_data.get('cvv', '').strip()  # Strip spaces
        if not cvv.isdigit() or len(cvv) != 3:
            raise forms.ValidationError("Enter a valid 3-digit CVV.")
        return cvv
