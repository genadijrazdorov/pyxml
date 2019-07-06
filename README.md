# pyxml

a python ElementTree extension for declarative xml schema with validation.

* xml schema/model declaration (inspired by [SQLAlchemy](https://www.sqlalchemy.org/))
* Intuitive model to xml schema mapping
* build on top of [ElementTree](https://docs.python.org/3/library/xml.etree.elementtree.html)
* separation of model declaration from application logic

### A simple example

~~~python
>>> from pyxml import Element, Attribute
>>> import xml.etree.ElementTree as ET

~~~

#### Declaring a model

~~~python
>>> class Model(Element):
...     name = Attribute(required=True)
...
...     # nested submodel declaration
...     class Subelement(Element):
...         min = 1 # required element
...

~~~

#### Initializing

~~~python
>>> model = Model(name='The Model')

>>> print(ET.tostring(model))
<Model name="The Model">
    <Subelement />
</Model>

~~~

#### Working with a model

##### ElementTree way

~~~python
>>> model[0].get('name')
'The Model'

>>> mode[0].set('name', 'The New Model')

~~~

##### pyxml way

~~~python
>>> model.submodel.name
'The Model'

>>> mode.submodel.name = 'The New Model'

~~~


