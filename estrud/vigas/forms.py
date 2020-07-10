from django import forms


class VigaForm(forms.Form):
    LIMITES_CHOICES = (("x34", "Lim. x3-4"),)
    CONCRETO_CHOICES = (
        ("20", "C20"),
        ("25", "C25"),
        ("30", "C30"),
        ("35", "C35"),
        ("40", "C40"),
        ("45", "C45"),
        ("50", "C50"),
        ("55", "C55"),
        ("60", "C60"),
        ("65", "C65"),
        ("70", "C70"),
        ("75", "C75"),
        ("80", "C80"),
        ("85", "C85"),
        ("90", "C90"),)
    ACO_CHOICES = (("500", "CA-50"),)
    b = forms.DecimalField(label='b (cm)', widget=forms.NumberInput(attrs={
        'class': 'input',
        'placeholder': 'Largura'
        }))
    h = forms.DecimalField(label='h (cm)', widget=forms.NumberInput(attrs={
        'class': 'input',
        'placeholder': 'Altura'
        }))
    d = forms.DecimalField(label='d (cm)', widget=forms.NumberInput(attrs={
        'class': 'input',
        'placeholder': 'Altura Útil'
        }))
    d_linha = forms.DecimalField(label="d' (cm)", widget=forms.NumberInput(attrs={
        'class': 'input',
        'placeholder': 'Cobrimento'
        }))
    limites = forms.ChoiceField(label="Limite LN", choices=LIMITES_CHOICES)
    concreto = forms.ChoiceField(label="Concreto", choices=CONCRETO_CHOICES)
    aco = forms.ChoiceField(choices=ACO_CHOICES)
    esforco = forms.DecimalField(label='Mk (kN.m)', widget=forms.NumberInput(attrs={
        'class': 'input',
        'placeholder': 'Momento'
        }))
    gama_f = forms.DecimalField(label='γf', widget=forms.NumberInput(attrs={
        'class': 'input',
        'value': '1.4'
        }))
    description = forms.CharField(required=False)
