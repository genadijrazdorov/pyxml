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


# Project Title

One Paragraph of project description goes here

## Getting Started

These instructions will get you a copy of the project up and running on your local machine for development and testing purposes. See deployment for notes on how to deploy the project on a live system.

### Prerequisites

What things you need to install the software and how to install them

```
Give examples
```

### Installing

A step by step series of examples that tell you how to get a development env running

Say what the step will be

```
Give the example
```

And repeat

```
until finished
```

End with an example of getting some data out of the system or using it for a little demo

## Running the tests

Explain how to run the automated tests for this system

### Break down into end to end tests

Explain what these tests test and why

```
Give an example
```

### And coding style tests

Explain what these tests test and why

```
Give an example
```

## Deployment

Add additional notes about how to deploy this on a live system

## Built With

* [Dropwizard](http://www.dropwizard.io/1.0.2/docs/) - The web framework used
* [Maven](https://maven.apache.org/) - Dependency Management
* [ROME](https://rometools.github.io/rome/) - Used to generate RSS Feeds

## Contributing

Please read [CONTRIBUTING.md](https://gist.github.com/PurpleBooth/b24679402957c63ec426) for details on our code of conduct, and the process for submitting pull requests to us.

## Versioning

We use [SemVer](http://semver.org/) for versioning. For the versions available, see the [tags on this repository](https://github.com/your/project/tags). 

## Authors

* **Billie Thompson** - *Initial work* - [PurpleBooth](https://github.com/PurpleBooth)

See also the list of [contributors](https://github.com/your/project/contributors) who participated in this project.

## License

This project is licensed under the MIT License - see the [LICENSE.md](LICENSE.md) file for details

## Acknowledgments

* Hat tip to anyone whose code was used
* This README is build on top of the [PurpleBooth](https://gist.github.com/PurpleBooth/109311bb0361f32d87a2) template
* pyxml was inspired by [SQLAlchemy]()
* etc


