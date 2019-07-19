# pyxml

[![GitHub](https://img.shields.io/github/license/genadijrazdorov/pyxml.svg)](LICENSE)
[![GitHub All Releases](https://img.shields.io/github/downloads/genadijrazdorov/pyxml/total.svg)](https://github.com/genadijrazdorov/pyxml/releases)
[![Contributor
Covenant](https://img.shields.io/badge/Contributor%20Covenant-v1.4%20adopted-ff69b4.svg)](code-of-conduct.md)

A python ElementTree extension for declarative xml schema with validation.

~~~python
>>> class Model(Element):
...     name = Attribute(required=True)
...
...     class Subelement(Element):
...         min = 1
...

>>> model = Model(name='The Model')

>>> print(ET.tostring(model))
<Model name="The Model">
    <Subelement />
</Model>

~~~

## Features

* xml schema/model declaration (inspired by [SQLAlchemy](https://www.sqlalchemy.org/))
* Intuitive model to xml schema mapping
* build on top of [ElementTree](https://docs.python.org/3/library/xml.etree.elementtree.html)
* separation of model declaration from application logic
* native typing of attributes and text attribute

## Getting Started

These instructions will get you a copy of the project up and running on your
local machine.

### Prerequisites

FIXME

``` Give examples ```

### Installing

Download [distribution](https://github.com/genadijrazdorov/pyxml/releases)
and install:

~~~bash
$ python setup.py install

~~~

#### Short demostration

~~~python
$ python
Python ...
Type "help", ...
>>> from pyxml import Element, Attribute
>>> import xml.etree.ElementTree as ET

>>> # model declaration

>>> class Model(Element):
...     name = Attribute(required=True)
...
...     # nested submodel declaration
...     class Subelement(Element):
...	    min = 1 # required element
...	    rank = Attribute(decode=int)
...

>>> # model initialization

>>> model = Model(name='The Model')

>>> print(ET.tostring(model))
<Model name="The Model">
    <Subelement />
</Model>

>>> # working with model

>>> model.name = 'The New Model'
>>> model.name
'The New Model'

>>> model.subelement.rank = 0
>>> model.subelement.rank
0

>>> print(ET.tostring(model))
<Model name="The New Model">
    <Subelement rank="0"/>
</Model>

~~~


## Running the tests

~~~bash
$ python setup.py test

~~~

## Contributing

Please read
[CONTRIBUTING.md](CONTRIBUTING.md) for the process for submitting pull requests
to us.

Please note that this project is released with a [Contributor Code of
Conduct](CODE_OF_CONDUCT.md). By participating in this project you agree to
abide by its terms.

## Versioning

We use [SemVer](http://semver.org/) for versioning. For the versions available,
see the [tags on this
repository](https://github.com/genadijrazdorov/pyxml/tags). 

## Authors

* Genadij Razdorov - [genadijrazdorov](https://github.com/genadijrazdorov)

See also the list of
[contributors](https://github.com/genadijrazdorov/pyxml/contributors) who
participated in this project.

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE)
file for details

## Acknowledgments

* Hat tip to anyone whose code was used
* This README is build on top of the
  [PurpleBooth](https://gist.github.com/PurpleBooth/109311bb0361f32d87a2)
  template
* pyxml was inspired by [SQLAlchemy]()
* etc


