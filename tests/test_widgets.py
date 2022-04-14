import json

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
