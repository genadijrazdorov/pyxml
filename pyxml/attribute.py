from .element import Element
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
