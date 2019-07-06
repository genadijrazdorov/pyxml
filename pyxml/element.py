
import xml.etree.ElementTree as ET
import functools
import weakref


class Attribute:
    required = False
    value = None
    name = {}
    encode = str
    decode = str

    def __init__(self, required=None):
        if required is not None:
            self.required = required
        self.value = weakref.WeakKeyDictionary()

    def __get__(self, instance, owner):
        if instance is None:
            return self

        try:
            return self.value[instance]

        except KeyError:
            value = super(Element, instance).get(self.name[owner])
            if value is not None:
                value = self.decode(value)
            self.value[instance] = value
            return value

    def __set__(self, instance, value):
        self.value[instance] = value

        cls = instance.__class__
        super(Element, instance).set(self.name[cls], self.encode(value))

    def __delete__(self, instance):
        cls = instance.__class__
        super(Element, instance).set(self.name[cls], None)
        del self.value[instance]

    def __set_name__(self, owner, name):
        self.name[owner] = name


class Element(ET.Element):
    """
    """
    min = 0
    max = None

    def __init__(self, attrib=None, **extra):
        if attrib is None:
            attrib = {}

        if self.tag is not None:
            super().__init__(self.tag)

        else:
            super().__init__(self.__class__.__name__)

        for key, value in attrib.items():
            setattr(self, key, value)

        for key, value in extra.items():
            setattr(self, key, value)

        for Child in self.__class__.__dict__.values():
            if isinstance(Child, type) and issubclass(Child, Element):
                if Child.max is None or Child.max > Child.min:
                    for _ in range(Child.min):
                        self.append(Child())

    def get(self, attribute):
        return getattr(self, attribute)

    def set(self, attribute, value):
        setattr(self, attribute, value)

    def _append(self, cls, *args, **kwargs):
        el = cls(*args, **kwargs)
        self.append(el)
        return el

    def __getattr__(self, attr):
        if attr.startswith('append_'):
            attr = attr[len('append_'):]
            Attr = attr[0].upper() + attr[1:]
            return functools.partial(self._append, getattr(self, Attr))

        else:
            raise AttributeError


class Tree(Element):
    pass
