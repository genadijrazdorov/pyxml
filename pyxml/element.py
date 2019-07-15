import xml.etree.ElementTree as ET
import functools


class Element(ET.Element):
    """Extended `Element`:py:class: from `ElementTree`:py:module:

    Notes
    -----
    Should be subclassed to harness all the power of `pyxml`.

    Parameters
    ----------
    attrib : dict(key: value)
        Attributes
    **extra
        Extra attributes

    Attributes
    ----------
    min : `int`, default: 0
        Required number of `Element`:py:class: instances
    max : `int` or `None`, default: `None`
        Maximal number of `Element`:py:class: instances or unlimited
    encode : `callable`, default: `str`
        Returns encoded `value`:py:attr:
    decode : `callable`, default: `str`
        Returns decoded `text`:py:attr:

    """
    min = 0
    max = None

    encode = str
    decode = str

    @property
    def value(self):
        """obj: Value of Element.text"""
        return self.decode(self.text)

    @value.setter
    def value(self, value):
        self.text = self.encode(value)

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
            if isinstance(Child, type) and issubclass(Child, Element) and \
                    (Child.max is None or Child.max > Child.min):
                for _ in range(Child.min):
                    self.append(Child())

    def get(self, key, default=None):
        return getattr(self, key) or default

    get.__doc__ = ET.Element.get.__doc__

    def set(self, key, value):
        setattr(self, key, value)

    set.__doc__ = ET.Element.set.__doc__

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
