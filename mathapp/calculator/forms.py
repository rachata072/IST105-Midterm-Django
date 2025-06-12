from django import forms

class CalculatorForm(forms.Form):
    OPERATION_CHOICES = [
        ('add', 'Add'),
        ('sub', 'Subtract'),
        ('mul', 'Multiply'),
        ('div', 'Divide'),
    ]
    
    input1 = forms.FloatField(label='First Number')
    input2 = forms.FloatField(label='Second Number')
    operation = forms.ChoiceField(label='Operation', choices=OPERATION_CHOICES) 