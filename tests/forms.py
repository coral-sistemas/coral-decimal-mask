from decimal import Decimal

from django import forms

from decimal_mask.widgets import (
    DecimalMaskWidget,
    MoneyMaskWidget,
    PercentMaskWidget,
)


class TestForm(forms.Form):
    decimal1 = forms.DecimalField(
        label="Decimal1 (en-US)",
        widget=DecimalMaskWidget(),
    )
    decimal2 = forms.DecimalField(
        label="Decimal2 (pt-BR)",
        widget=DecimalMaskWidget(
            decimal_attrs={
                "locales": "pt-BR",
                "decimalPlaces": 3,
            },
        ),
    )
    result = forms.DecimalField(
        label="Sum Decimal1 + Decimal2",
        widget=DecimalMaskWidget(
            decimal_attrs={
                "decimalPlaces": 3,
            },
            attrs={'readonly': True}
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
