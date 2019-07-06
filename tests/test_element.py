from pyxml.element import Element, Tree

import pytest


class Simple(Tree):
    class Subelement(Element):
        min = 1


@pytest.fixture
def simple():
    return Simple()


class TestElementBasic:
    def test__init__(self):
        simple = Simple()

    def test__getitem__(self, simple):
        assert isinstance(simple[0], Simple.Subelement)

    def test__setitem__(self, simple):
        empty = Element()
        simple[0] = empty
        assert simple[0] is empty

    def test__delitem__(self, simple):
        del simple[0]
        assert len(simple) == 0

    def test__len__(self, simple):
        assert len(simple) == 1

    def test_insert(self, simple):
        empty = Element()
        simple.insert(0, empty)
        assert simple[0] is empty


class TestElementNew:
    def test_append_x(self, simple):
        subelement = simple.append_subelement(proba='Proba')
        assert subelement.get('proba') == 'Proba'
        assert simple[-1] is subelement
