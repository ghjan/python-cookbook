# Example of managed attributes via properties

class Person:
    def __init__(self, name):
        self.name = name

    # Getter function
    @property
    def name(self):
        return self._name

    # Setter function
    @name.setter
    def name(self, value):
        if not isinstance(value, str):
            raise TypeError('Expected a string')
        self._name = value

    @name.deleter
    def name(self):
        raise AttributeError("Can't delete attribute")


class SubPerson(Person):
    @property
    def name(self):
        print('Getting name(SubPerson)')
        return super().name

    @name.setter
    def name(self, value):
        print('Setting name to(SubPerson)', value)
        super(SubPerson, SubPerson).name.__set__(self, value)

    @name.deleter
    def name(self):
        print('Deleting name(SubPerson)')
        super(SubPerson, SubPerson).name.__delete__(self)


class SubPerson2(Person):
    @Person.name.setter
    def name(self, value):
        print('Setting name to(SubPerson2)', value)
        super(SubPerson2, SubPerson2).name.__set__(self, value)


class SubPerson3(Person):
    @property
    # @Person.name.getter
    def name(self):
        print('Getting name(SubPerson3)')
        return super().name


if __name__ == '__main__':
    a = Person('Guido')
    print(a.name)
    a.name = 'Dave'
    print(a.name)
    try:
        a.name = 42
    except TypeError as e:
        print(e)

    print("-----SubPersion")
    s = SubPerson('Guido')
    print(s.name)
    s.name = 'Larry'
    try:
        s.name = 42
    except TypeError as e:
        print(e)
    print("-----SubPerson2")
    s = SubPerson2('Guido')
    print(s.name)
    s.name = 'Larry'
    try:
        s.name = 42
    except TypeError as e:
        print(e)
    print("-----SubPerson3")
    try:
        s = SubPerson3('Guido')
    except AttributeError as e:
        print(e)
    print(s.name)
    s.name = 'Larry'
    try:
        s.name = 42
    except TypeError as e:
        print(e)
