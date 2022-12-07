from decimal import Decimal

from django import forms
from django.shortcuts import render

from decimal_mask.widgets import (
    DecimalMaskWidget,
    MoneyMaskWidget,
    PercentMaskWidget,
)


class TestForm(forms.Form):
    decimal1 = forms.DecimalField(
        label="Decimal (en-US)",
        widget=DecimalMaskWidget(),
    )
    decimal2 = forms.DecimalField(
        label="Decimal (pt-BR)",
        widget=DecimalMaskWidget(
            decimal_attrs={
                "locales": "pt-BR",
                "decimalPlaces": 3,
            },
        ),
    )
    money1 = forms.DecimalField(
        label="Money (pt-BR)",
        widget=MoneyMaskWidget(
            decimal_attrs={
                "locales": "pt-BR",
                "format": {
                    "style": "currency",
                    "currency": "BRL",
                },
            },
        ),
        required=False,
        help_text="required=False",
    )
    money2 = forms.DecimalField(
        label="Money (widget)",
        widget=MoneyMaskWidget(),
    )
    money3 = forms.DecimalField(
        label="Money (widget)",
        widget=MoneyMaskWidget(),
        initial=Decimal("1234.9099992129"),
        help_text="initial=1234.9099992129",
    )
    percent = forms.DecimalField(
        label="Percent",
        widget=PercentMaskWidget(),
    )


def index(request):
    form = TestForm()
    return render(request, "index.html", {"form": form})
