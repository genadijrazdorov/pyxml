# from .element import Element
import xml.etree.ElementTree as ET
import weakref


class Attribute:
    """Data descriptor handling attributes for `Element`:py:class

    Parameters
    ----------
    required : `bool`, default: `Attribute.required`:py:attr:
        Attribute is required attribute
    encode : `callable`, default: `Attribute.encode`:py:attr:
        Returns encoded value of `Attribute`:py:class: instance
    decode: `callable`, default: `Attribute.decode`:py:attr:
        Returns decoded value of `Attribute`:py:class: instance

    Attributes
    ----------
    required : `bool`, default: `False`
        `Attribute` is required
    encode : `callable`, default: `str`:py:func:
        Returns encoded value of `Attribute`:py:class: instance
    decode : `callable`, default: `str`:py:func:
        Returns decoded value of `Attribute`:py:class: instance


    """
    required = False
    name = {}
    encode = str
    decode = str

    def __init__(self, required=None, encode=None, decode=None):
        if required is not None:
            self.required = required
        if encode is not None:
            self.encode = encode
        if decode is not None:
            self.decode = decode
        self.value = weakref.WeakKeyDictionary()

    def __get__(self, instance, owner):
        if instance is None:
            return self

        try:
            return self.value[instance]

        except KeyError:
            # value = super(Element, instance).get(self.name[owner])
            value = ET.Element.get(instance, self.name[owner])
            if value is not None:
                value = self.decode(value)
            self.value[instance] = value
            return value

    def __set__(self, instance, value):
        self.value[instance] = value

        cls = instance.__class__

        # FIXME: which is better?
        # super(Element, instance).set(self.name[cls], self.encode(value))
        ET.Element.set(instance, self.name[cls], self.encode(value))

    def __delete__(self, instance):
        cls = instance.__class__

        # FIXME: should delete not set to None
        # super(Element, instance).set(self.name[cls], None)
        ET.Element.set(instance, self.name[cls], None)
        del self.value[instance]

    def __set_name__(self, owner, name):
        self.name[owner] = name
