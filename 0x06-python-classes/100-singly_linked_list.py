#!/usr/bin/python3
'''This is a module'''


class Node:
    '''A Node class'''
    def __init__(self, data, next_node=None):
        '''An init function'''
        self.data = data
        self.__next_node = next_node

    @property
    def data(self):
        '''A getter function for data'''
        return self.__data

    @data.setter
    def data(self, value):
        '''A setter function for data'''
        if not isinstance(value, int):
            raise TypeError('data must be an integer')
        self.__data = value

    @property
    def next_node(self):
        '''A getter function for next_node'''
        return self.__next_node

    @next_node.setter
    def next_node(self, value):
        '''A setter function for next_node'''
        if (not isinstance(value, Node) and value is not None):
            raise TypeError('next_node must be a Node object')
        self.__next_node = value


class SinglyLinkedList:
    '''A singly linked list'''
    def __init__(self):
        '''An init function'''
        self.__head = None

    def __str__(self):
        '''A str funtion'''
        temp = self.__head
        values = []
        while (temp is not None):
            values.append(str(temp.data))
            temp = temp.next_node
        return '\n'.join(values)

    def sorted_insert(self, value):
        '''A sort function'''
        temp = self.__head
        new_node = Node(value)
        if (temp is None):
            new_node.next_node = temp
            self.__head = new_node
        elif (temp.data >= new_node.data):
            new_node.next_node = temp
            self.__head = new_node
        else:
            while (temp.next_node is not None):
                if (temp.next_node.data < new_node.data):
                    temp = temp.next_node
                else:
                    break
            new_node.next_node = temp.next_node
            temp.next_node = new_node
