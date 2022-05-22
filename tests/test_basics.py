import pytest
from gannswing import GannSwing

def test_class_exists():
    gs = GannSwing()
    assert gs != None