import json
from decimal import Decimal

from django import forms

from decimal_mask.widgets import (
    DecimalMaskWidget,
    MoneyMaskWidget,
    PercentMaskWidget,
)


def test_decimal_widget():
    w = DecimalMaskWidget()
    assert "decimal_mask/DecimalMask.js" in str(w.media)
    assert "decimal_mask/init.js" in str(w.media)
    assert w.input_type == "tel"
    attrs = w.build_attrs({})
    expected = {
        "locales": "en-US",
        "decimalPlaces": 2,
    }
    assert "data-decimal-mask" in attrs
    assert json.dumps(expected) == attrs["data-decimal-options"]


def test_money_widget():
    w = MoneyMaskWidget()
    assert "decimal_mask/DecimalMask.js" in str(w.media)
    assert "decimal_mask/init.js" in str(w.media)
    assert w.input_type == "tel"
    attrs = w.build_attrs({})
    expected = {
        "locales": "en-US",
        "decimalPlaces": 2,
        "format": {
            "style": "currency",
            "currency": "USD",
        },
    }
    assert "data-decimal-mask" in attrs
    assert json.dumps(expected) == attrs["data-decimal-options"]


def test_percent_widget():
    w = PercentMaskWidget()
    assert "decimal_mask/DecimalMask.js" in str(w.media)
    assert "decimal_mask/init.js" in str(w.media)
    assert w.input_type == "tel"
    attrs = w.build_attrs({})
    expected = {
        "locales": "en-US",
        "decimalPlaces": 2,
        "format": {
            "style": "percent",
        },
    }
    assert "data-decimal-mask" in attrs
    assert json.dumps(expected) == attrs["data-decimal-options"]


def test_remove_mask():
    class TestForm1(forms.Form):
        value = forms.DecimalField(
            max_digits=15,
            widget=DecimalMaskWidget(),
            required=False,
        )

    class TestForm2(forms.Form):
        value = forms.DecimalField(
            max_digits=15,
            widget=DecimalMaskWidget({"decimalPlaces": 3}),
        )

    form = TestForm1({"value": "$ 100.99"})
    assert form.is_valid() is True
    assert form.cleaned_data["value"] == Decimal("100.99")

    form = TestForm2({"value": "$ 100.999"})
    assert form.is_valid() is True
    assert form.cleaned_data["value"] == Decimal("100.999")

    form = TestForm1({"value": ""})
    assert form.is_valid() is True
    assert form.cleaned_data["value"] is None
