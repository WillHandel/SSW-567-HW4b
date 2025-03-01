import pytest
from triagleClassification import classify_triangle

def test_equilateral_triangle():
    assert classify_triangle(3, 3, 3) == "Equilateral"

def test_isosceles_triangle():
    assert classify_triangle(3, 3, 4) == "Isosceles"

def test_scalene_triangle():
    assert classify_triangle(5, 6, 7) == "Scalene"

def test_right_triangle():
    assert classify_triangle(3, 4, 5) == "Scalene and Right"

test_equilateral_triangle()
test_isosceles_triangle()
test_scalene_triangle()
test_right_triangle()