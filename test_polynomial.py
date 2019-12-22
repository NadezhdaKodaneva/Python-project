import pytest
import random

from polynomial import Polynomial
#from polynomial import RealPolynomial
#from polynomial import QuadraticPolynomial


def test_init():
    poly_list = Polynomial([0, 1, 0, -2, 3, 0])
    assert str(poly_list) == '3x^4 - 2x^3 + x'
    assert repr(poly_list) == 'Polynomial [0, 1, 0, -2, 3]'

    poly_copy = Polynomial(poly_list)
    assert str(poly_copy) == '3x^4 - 2x^3 + x'
    assert repr(poly_copy) == 'Polynomial [0, 1, 0, -2, 3]'

    poly_dict = Polynomial({5: 3, 0: -1, 10: 7, 2: -4})
    assert str(poly_dict) == '7x^10 + 3x^5 - 4x^2 - 1'
    assert repr(poly_dict) == 'Polynomial [-1, 0, -4, 0, 0, 3, 0, 0, 0, 0, 7]'

    poly_args = Polynomial(1, 2, -3, 0, 5)
    assert str(poly_args) == '5x^4 - 3x^2 + 2x + 1'
    assert repr(poly_args) == 'Polynomial [1, 2, -3, 0, 5]'

    poly_const = Polynomial(10)
    assert str(poly_const) == '10'
    assert repr(poly_const) == 'Polynomial [10]'

def test_eq():
    poly_zero = Polynomial([0] * 100)
    assert poly_zero == Polynomial(0)

    poly_zero_tail = Polynomial([1, 2, 0, -3, 0, 0, 0, 0, 0])
    assert poly_zero_tail == Polynomial([1, 2, 0, -3])

def test_add():
    poly_lhs = Polynomial([2, 5, 0, 3, 2])
    poly_rhs = Polynomial(1, 3, 5, 0, 1, 0, 3)
    #poly_rhs = Polynomial(0, 0, 0, 0, 0, 0, 0)
    #poly_lhs = Polynomial([3, 0, 0, 0, 0])

    assert poly_lhs + poly_rhs == poly_rhs + poly_lhs
    assert str(poly_lhs + poly_rhs) == '3x^6 + 3x^4 + 3x^3 + 5x^2 + 8x + 3'
    assert str(14 + poly_lhs + 5) == '2x^4 + 3x^3 + 5x + 21'

    poly_lhs = Polynomial([2, 1, 2, 1])
    poly_rhs = Polynomial({3: 1, 1: 1, 0: 2, 2: 2}) #[2, 1, 2, 1]
    assert str(1 + poly_rhs + 2 + poly_lhs + 3) == '2x^3 + 4x^2 + 2x + 10'

    poly_lhs += poly_rhs
    assert str(poly_lhs) == '2x^3 + 4x^2 + 2x + 4'

def test_sub():
    poly_lhs = Polynomial([1, 4, 1, 3])
    poly_rhs = Polynomial([4, 5, 5, 3])

    assert str(poly_lhs - poly_rhs) == '-4x^2 - x - 3'
    assert str(50 - poly_lhs - 4) == '-3x^3 - x^2 - 4x + 45'

def test_deg():
    poly_list = Polynomial([0, 1, 0, -2, 3, 0, 0])
    assert poly_list.degree() == 4

    poly_dict = Polynomial({5: 3, 0: -1, 10: 7, 2: -4})
    assert poly_dict.degree() == 10

    poly_const = Polynomial(10)
    assert poly_const.degree() == 0

def test_call():
    poly = Polynomial([2, 1, 4, 1, 2, 5, 0])
    assert poly(0) == 2
    assert poly(1) == 15
    assert poly(2) == 220

def test_der():
    poly = Polynomial([0, 4, 2, 2, 2, 1, 5])
    assert str(poly.der(0)) == str(poly)
    assert str(poly.der()) == '30x^5 + 5x^4 + 8x^3 + 6x^2 + 4x + 4'
    assert str(poly.der(5)) == '3600x + 120'