"""
Clase Nodo para implementar el ADT BinarySearchTree
Author: Bruno Bulacia
Date: 08/27/2024
"""
class Node:
    def __init__(self, data):
        """Inicializa el nodo con un dato"""
        self._father = None
        self._left = None
        self._right = None
        self._data = data

    def get_father(self):
        """Retorna el padre del nodo"""
        return self._father
    def set_father(self, father):
        """Asigna un padre al nodo"""
        self._father = father
    def get_data(self):
        """Retorna el dato del nodo"""
        return self._data

    def get_left(self):
        """Retorna el nodo izquierdo"""
        return self._left

    def get_right(self):
        """Retorna el nodo derecho"""
        return self._right

    def set_data(self, data):
        """Asigna valor al atributo data"""
        self._data = data

    def set_right(self, left):
        """Asigna un nodo al atributo left"""
        self._left = left

    def set_right(self, right):
        """Asigna un nodo al atributo right"""
        self._right = right
