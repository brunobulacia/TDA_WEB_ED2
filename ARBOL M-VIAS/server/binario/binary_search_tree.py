from binary_node import Node
from collections import deque

class BinarySearchTree:
    """
    Clase que representa un Árbol de Búsqueda Binaria (BST).
    """

    def __init__(self):
        """
        Inicializa un árbol vacío.
        """
        self._root = None
        self._n = 0
        self._nivel = 0

    def insert(self, data):
        """
        Inserta un nuevo nodo en el árbol con el valor proporcionado.

        :param data: El valor a insertar en el árbol.
        """
        self._root = self.__insert(self._root, data, None)
        self._n += 1


    def __insert(self, node, data, father):
        """
        Método auxiliar recursivo para insertar un nuevo nodo en el árbol.

        :param node: El nodo actual en la recursión.
        :param data: El valor a insertar en el árbol.
        :param father: El nodo padre.
        :return: El nodo actualizado después de la inserción.
        """
        if node is None:
            new_node = Node(data)
            new_node._father = father
            return new_node
        if data < node._data:
            node._left = self.__insert(node._left, data, node)
        else:
            node._right = self.__insert(node._right, data, node)
        return node

    def is_empty(self):
        """
        Verifica si el árbol está vacío.

        :return: True si el árbol está vacío, False en caso contrario.
        """
        return self._root is None

    def search(self, data):
        """
        Busca un valor en el árbol.

        :param data: El valor a buscar.
        :return: El nodo que contiene el valor, o None si no se encuentra.
        """
        return self.__search(self._root, data)

    def __search(self, node, data):
        """
        Método auxiliar recursivo para buscar un valor en el árbol.

        :param node: El nodo actual en la recursión.
        :param data: El valor a buscar.
        :return: El nodo que contiene el valor, o None si no se encuentra.
        """
        if node is None:
            return None
        if node._data == data:
            return node
        elif data < node._data:
            return self.__search(node._left, data)
        else:
            return self.__search(node._right, data)

    def find_min(self):
        """
        Encuentra el valor mínimo en el árbol.

        :return: El valor mínimo en el árbol, o None si el árbol está vacío.
        """
        return self.__find_min(self._root)._data if self._root else None

    def __find_min(self, node):
        """
        Método auxiliar para encontrar el nodo con el valor mínimo.

        :param node: El nodo actual en la recursión.
        :return: El nodo con el valor mínimo.
        """
        current = node
        while current and current._left is not None:
            current = current._left
        return current

    def find_max(self):
        """
        Encuentra el valor máximo en el árbol.

        :return: El valor máximo en el árbol, o None si el árbol está vacío.
        """
        return self.__find_max(self._root)._data if self._root else None

    def __find_max(self, node):
        """
        Método auxiliar para encontrar el nodo con el valor máximo.

        :param node: El nodo actual en la recursión.
        :return: El nodo con el valor máximo.
        """
        current = node
        while current and current._right is not None:
            current = current._right
        return current

    def delete(self, data):
        """
        Elimina un nodo con el valor especificado del árbol.

        :param data: El valor del nodo a eliminar.
        """
        self._root = self.__delete(self._root, data)
        if self._root is not None:
            self._n -= 1

    def __delete(self, node, data):
        """
        Método auxiliar recursivo para eliminar un nodo del árbol.

        :param node: El nodo actual en la recursión.
        :param data: El valor del nodo a eliminar.
        :return: El nodo actualizado después de la eliminación.
        """
        if node is None:
            return node

        if data < node._data:
            node._left = self.__delete(node._left, data)
            if node._left:
                node._left._father = node
        elif data > node._data:
            node._right = self.__delete(node._right, data)
            if node._right:
                node._right._father = node
        else:
            if node._left is None and node._right is None:
                node = None
            elif node._left is None:
                node = node._right
                node._father = node._father._father
            elif node._right is None:
                node = node._left
                node._father = node._father._father
            else:
                temp = self.__find_min(node._right)
                node._data = temp._data
                node._right = self.__delete(node._right, temp._data)
                if node._right:
                    node._right._father = node
        return node

    def get_root(self):
        """
        Devuelve la raíz del árbol.

        :return: El nodo raíz del árbol.
        """
        return self._root

    def size(self):
        """
        Devuelve el número de nodos en el árbol.

        :return: El número total de nodos en el árbol.
        """
        return self._n

    def in_order(self):
        if self._root is None:
            return []  # Retorna una lista vacía si el árbol está vacío
        else:
            # Retorna la lista generada por la función __in_order()
            return self.__in_order(self._root)

    def __in_order(self, _node):
        if _node is None:
            return []
        else:
            result = []
            result.extend(self.__in_order(_node._left))
            result.append(_node._data)
            result.extend(self.__in_order(_node._right))
        return result

    def pre_order(self):
        if self._root is None:
            return []  # Retorna una lista vacía si el árbol está vacío
        else:
            return self.__pre_order(self._root)

    def __pre_order(self, _node):
        if _node is None:
            return []
        else:
            result = []
            result.append(_node._data)
            result.extend(self.__pre_order(_node._left))
            result.extend(self.__pre_order(_node._right))
        return result

    def post_order(self):
        if self._root is None:
            return []  # Retorna una lista vacía si el árbol está vacío
        else:
            return self.__post_order(self._root)

    def __post_order(self, _node):
        if _node is None:
            return []
        else:
            result = []
            result.extend(self.__post_order(_node._left))
            result.extend(self.__post_order(_node._right))
            result.append(_node._data)
        return result

    def __post_order(self, _node):
        if _node is None:
            return []
        else:
            result = []
            # Realiza un recorrido post-order en el subárbol izquierdo
            result.extend(self.__post_order(_node._left))
            # Realiza un recorrido post-order en el subárbol derecho
            result.extend(self.__post_order(_node._right))
            # Agrega el dato del nodo actual a la lista
            result.append(_node._data)
        return result


    def height(self):
        """
        Calcula la altura del árbol.

        :return: La altura del árbol (el número de niveles desde la raíz hasta la hoja más lejana).
        """
        return self.__height(self._root) + 1

    def __height(self, node):
        """
        Método auxiliar recursivo para calcular la altura de un nodo.

        :param node: El nodo actual.
        :return: La altura del nodo.
        """
        if node is None:
            return -1  # La altura de un árbol vacío es -1, ya que no hay niveles
        else:
            # Calcula la altura de los subárboles izquierdo y derecho
            left_height = self.__height(node._left)
            right_height = self.__height(node._right)
            # La altura del nodo es el máximo entre ambos subárboles más 1
            return max(left_height, right_height) + 1
        
    
    def depth(self, data):
        """
        Calcula la profundidad de un nodo con el valor dado.

        :param data: El valor del nodo para el cual calcular la profundidad.
        :return: La profundidad del nodo si se encuentra, o -1 si no se encuentra.
        """
        return self.__depth(self._root, data, 0)

    def __depth(self, node, data, depth_level):
        """
        Método auxiliar recursivo para calcular la profundidad de un nodo.

        :param node: El nodo actual en la recursión.
        :param data: El valor del nodo para el cual calcular la profundidad.
        :param depth_level: El nivel actual de profundidad.
        :return: La profundidad del nodo si se encuentra, o -1 si no se encuentra.
        """
        if node is None:
            return -1  # El nodo no se encontró

        if node._data == data:
            return depth_level

        if data < node._data:
            return self.__depth(node._left, data, depth_level + 1)
        else:
            return self.__depth(node._right, data, depth_level + 1)



    def level_order_traversal(self):
        result = []
        if self._root is None:
            return result

        queue = deque([self._root])
        while queue:
            # Extrae el primer nodo de la cola
            current_node = queue.popleft()
            
            # Si el nodo tiene padre, almacena su valor; si no, almacena None
            father_data = current_node._father._data if current_node._father else None
            result.append([current_node._data, father_data, self.depth(current_node._data)])
            
            # Agrega los hijos del nodo actual a la cola (primero el izquierdo, luego el derecho)
            if current_node._left:
                queue.append(current_node._left)
            if current_node._right:
                queue.append(current_node._right)
        
        return result
    
    def clear(self):
        """
        Elimina todos los nodos del árbol.
        """
        self._root = None
        self._n = 0