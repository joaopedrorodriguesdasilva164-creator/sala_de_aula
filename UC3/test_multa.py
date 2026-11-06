from multa import multa
import pytest

def test_sem_atraso():
    assert multa(0) == 0

def test_um_dia():
    assert multa(1) == 0

def test_fronteira():
    assert multa(3) ==15

def test_cinco_dias():
    assert multa(5) == 25
"""
minimundo classe 
"""
