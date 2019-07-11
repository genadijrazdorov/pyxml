from pyxml.element import Element, Tree
from pyxml.attribute import Attribute

import pytest


class Simple(Tree):
    name = Attribute(required=True)

    class Subelement(Element):
        min = 1


@pytest.fixture
def simple():
    return Simple(name='Name')


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

    def test_get(self, simple):
        assert simple.get('name') == 'Name'

    def test_set(self, simple):
        simple.set('name', 'New Name')
        assert simple.get('name') == 'New Name'


class TestElementNew:
    def test_append_x(self, simple):
        subelement = simple.append_subelement(proba='Proba')
        assert subelement.get('proba') == 'Proba'
        assert simple[-1] is subelement

class TestAttribute:
    def test__init__(self, simple):
        assert simple in simple.__class__.name.value

    def test_class__get__(self):
        assert isinstance(Simple.name, Attribute)

    def test__get__(self, simple):
        assert simple.name == 'Name'

    def test__set__(self, simple):
        simple.name = 'The New Name'
        assert simple.name == 'The New Name'

    def test__del__(self, simple):
        del simple.name
        assert simple.name is None
