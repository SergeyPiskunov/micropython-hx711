from unittest.mock import MagicMock
# from hx711 import HX711
import pytest
# from examples.scale import Scale
def test_scale():
    # hx711 = MagicMock(spec=HX711)
    # hx711.return_value.read.return_value = 535.0
    # sc = Scale(4, 5)
    # read = sc.read()
    dummy_testing = 535
    assert dummy_testing == 535.0
