import pytest
from searching import linear_search, binary_search

# -------- LINEAR SEARCH TESTS --------

def test_linear_found_middle():
    assert linear_search([1, 2, 3, 4, 5], 3) == 2

def test_linear_found_first():
    assert linear_search([10, 20, 30], 10) == 0

def test_linear_found_last():
    assert linear_search([10, 20, 30], 30) == 2

def test_linear_not_found():
    assert linear_search([1, 2, 3], 99) == -1

def test_linear_empty():
    assert linear_search([], 5) == -1


# -------- BINARY SEARCH TESTS --------

def test_binary_found():
    assert binary_search([1, 2, 3, 4, 5], 4) == 3

def test_binary_not_found():
    assert binary_search([1, 2, 3, 4, 5], 10) == -1

def test_binary_single_element_found():
    assert binary_search([7], 7) == 0

def test_binary_single_element_not_found():
    assert binary_search([7], 3) == -1

def test_binary_empty():
    assert binary_search([], 1) == -1