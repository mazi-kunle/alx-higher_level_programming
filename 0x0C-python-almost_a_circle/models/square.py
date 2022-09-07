#!/usr/bin/python3
'''This is a module'''


from models.rectangle import Rectangle


class Square(Rectangle):
    '''A class that inherits from Rectangle class.'''
    def __init__(self, size, x=0, y=0, id=None):
        super().__init__(size, size, x, y, id)

    def __str__(self):
        '''A magic method'''
        return ('[Square] ({}) {}/{} - {}'.format(
            self.id, self.x, self.y, self.width))

    @property
    def size(self):
        '''A getter function for size'''
        return self.width

    @size.setter
    def size(self, value):
        '''A setter function for size'''
        self.width = value
        self.height = value

    def update(self, *args, **kwargs):
        '''Update method for square'''
        if len(args) != 0:
            try:
                self.id = args[0]
                self.size = args[1]
                self.x = args[2]
                self.y = args[3]

            except IndexError:
                pass
        else:
            for key, val in kwargs.items():
                setattr(self, key, val)

    def to_dictionary(self):
        '''Returns the dictionary representation of the sqaure'''
        d = {}
        d['id'] = self.id
        d['x'] = self.x
        d['size'] = self.size
        d['y'] = self.y

        return d
