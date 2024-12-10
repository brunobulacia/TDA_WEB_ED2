from collections import deque #cola de doble extremo

from nodo_mvias import NodoMvias

class ArbolMVias:
    '''
    Esta clase crea un arbol m-vias
    '''
    def __init__(self, orden):
        self.__raiz = None
        self.__orden = orden

    def orden_arbol(self):
        '''
        Retorna:
            El valor orden del ArbolMvias.
        '''
        return self.__orden

    @property
    def raiz(self):
        '''
        Retorna:
            La referencia a la raiz del ArbolMvias.
        '''
        return self.__raiz

    @raiz.setter
    def raiz(self, link):
        '''
        Parametro:
            link (NodoMvias): Establece la referencia a la raiz para el ArbolMvias.
        '''
        self.__raiz = link

    def get_raiz(self):
        return self.raiz

    def arbol_vacio(self, nodo):
        '''
        Retorna:
            True si el nodo es None
            False caso contrario.
        Parametro:
            nodo (NodoMvias): referencia al nodo que se quiere verificar.
        '''
        return nodo is None

    def es_hoja(self, nodo):
        '''
        Retorna:
            True: si todos los hijos son nulos.
            False: caso contrario.
        '''
        for i in range(nodo.cantidad_datos + 1):
            if not nodo.hijo_vacio(i):
                return False
        return True

    def posicion_corresponde(self, nodo, dato):
        '''
        Retorna la posicion que le corresponde a un dato dentro de la Lista 
        de dicho nodo.
        Parametro:
            nodo (NodoMvias): Referencia al nodo en el cual se quiere buscar.
            dato (int): Valor cuya posicion se desea saber.
        '''
        posicion = 0
        for i in range(nodo.cantidad_datos):
            if dato < nodo.get_dato(i):
                return i
            posicion = i
        return posicion + 1

    def habilitar_posicion(self, nodo, posicion):
        '''
        Si la posicion esta ocupado los datos recorren una posicion
        a al derecha dejando un espacio libre correspondiente al dato.
        Parametro:
            nodo (NodoMvias): Referenciaa un nodo en el que se desea habilitar espacio.
            dato (int): valor pare el cual se quiere habilitar una posicion.
        Retorna:
            posicion (int): si la posicion esta libre.
            caso contrario los datos recorren una posicion para habilitar dicho espacio.
        '''
        if posicion == nodo.cantidad_datos:
            return posicion
        pos = nodo.cantidad_datos
        for i in range(pos, posicion, -1):
            valor = nodo.get_dato(i - 1)
            nodo.set_dato(i, valor)
        return posicion

    def existe_dato(self, dato):
        '''
        Verifica si un dato existe en el ArbolMvias.
        Retorna:
            True: si existe el dato.
            False caso contrario.
        Parametro: 
            dato (int): el valor a buscar en el ArbolMvias.
        '''
        return self.__existe(self.raiz, dato)

    def __existe(self, nodo, dato):
        '''
        metodo recursivo que verifica si el dato existe.
        Parametros:
            nodo (NodoArbol): referencia de un nodo que se quiere verificar.
            dato (int): valor a buscar en el arbol.
        Retorna:
            True si encuentra el dato.
            False caso contrario.
        '''
        if self.arbol_vacio(nodo):
            return False
        for i in range(nodo.cantidad_datos):
            print(nodo.cantidad_datos)
            print(nodo.get_dato(0))
            print(nodo.get_dato(2))
            print(nodo.get_dato(2))

            if dato == nodo.get_dato(i):
                return True
            if dato < nodo.get_dato(i):
                return self.__existe(nodo.get_hijo(i), dato)
        pos = nodo.cantidad_datos
        return self.__existe(nodo.get_hijo(pos), dato)

    def insertar_dato(self, dato):
        '''
        insertar un nuevo dato en el ArbolMvias.
        Si es arbol vacio: crea un nuevo nodo con el dato.
        caso contrario: llama al metodo __insertar
        Parametros:
            dato (): el elemento que se desea guardar.
        '''
        if self.raiz is None:
            new_nodo = NodoMvias(self.orden_arbol())
            new_nodo.set_dato(0, dato)
            new_nodo.cantidad_datos = 1
            self.raiz = new_nodo
            new_nodo.nodo_padre = None #la raiz no tiene padre
        else:
            if not self.existe_dato(dato):
                self.__insertar(self.raiz, dato)
            else:
                print("ya existe ese elemento")

    def __insertar(self, nodo, dato):
        if nodo.hay_espacio():
            #insertar en el nodo si tiene espacio
            posicion = self.posicion_corresponde(nodo, dato)
            self.habilitar_posicion(nodo, posicion)
            nodo.set_dato(posicion, dato)
            nodo.cantidad_datos = nodo.cantidad_datos + 1
        else:
            pos = self.posicion_corresponde(nodo, dato)
            if nodo.get_hijo(pos) is None:
                new_nodo = NodoMvias(self.orden_arbol())
                new_nodo.set_dato(0, dato)
                new_nodo.cantidad_datos = new_nodo.cantidad_datos + 1
                new_nodo.nodo_padre = nodo
                nodo.set_hijo(pos, new_nodo)
            else:
                self.__insertar(nodo.get_hijo(pos), dato)

#--------AUXILIARES PARA ELIMINAR------------
    def get_nodo(self, nodo, valor):
        '''
        Retorna un nodo al cual pertenece un valor, el valor no debe ser None,
        es decir el valor debe existir en el ArbolMvias.
        Parametro:
            nodo (NodoMvias): Referencia al nodo raiz la primera vez.
            valor (int): El dato cuyo nodo se requiere saber.
        Retorna:
            El nodo (NodoMvias) al cual pertenece el dato.
        '''
        if self.arbol_vacio(nodo):
            return None
        for i in range(nodo.cantidad_datos):
            if valor == nodo.get_dato(i):
                return nodo
        pos = self.posicion_corresponde(nodo, valor)
        return self.get_nodo(nodo.get_hijo(pos), valor)

    def get_posicion(self, nodo, dato):
        '''
        Retorna la posicion que ocupa un dato dentro de la lista de dicho nodo.
        Parametro:
            nodo (NodoMvias): Referencia al nodo en el cual se quiere buscar.
            dato (int): Valor cuya posicion se desea saber.
        '''
        for i in range(nodo.cantidad_datos):
            if dato == nodo.get_dato(i):
                return i
        return None

    def reordenar_datos(self, posicion, nodo):
        '''
        Reordena los datos despues de eliminar un dato
        Parametro:
            posicion (int): la posicion cuyo dato fue eliminado.
            nodo (NodoMvias): Referencia al nodo que se desea reordenar.
        '''
        if posicion != nodo.datos_permitidos() - 1:
            i = posicion
            for i in range(nodo.datos_permitidos() - 1):
                valor = nodo.get_dato(i + 1)
                hijo = nodo.get_hijo(i + 1)
                if valor is not None:
                    nodo.set_dato(i, valor)
                    nodo.set_dato(i + 1, None)
                if hijo is not None:
                    nodo.set_hijo(i, hijo)
                    nodo.set_hijo(i + 1, None)
        #recorre una posicion si el hijo esta en la ultima posicion
        hijo = nodo.get_hijo(posicion + 1)
        if hijo is not None:
            nodo.set_hijo(posicion, hijo)
            nodo.set_hijo(posicion + 1, None)

    def eliminar_dato(self, valor):
        '''
        Elimina un dato existente en el ArbolMvias
        Parametro:
            valor (int): dato que se desea eliminar
        '''
        if self.raiz is not None and self.existe_dato(valor):
            nodo_del_valor = self.get_nodo(self.raiz, valor)
            if nodo_del_valor != self.raiz:
                self.__eliminar_recursivo(self.raiz, valor, nodo_del_valor)

    def __eliminar_recursivo(self, nodo, valor, nodo_del_valor):
        if nodo is None:
            return
        #HACE UN RECORRIDO POR TODOS LOS HIJOS
        for i in range(nodo.cantidad_datos + 1):
            sig_nodo = nodo.get_hijo(i)
            if sig_nodo == nodo_del_valor:

                posicion = self.get_posicion(sig_nodo, valor)
                if self.es_hoja(sig_nodo):
                    sig_nodo.set_dato(posicion, None)
                    sig_nodo.cantidad_datos = sig_nodo.cantidad_datos - 1
                    #---REORDENAR LOS DATOS----
                    if sig_nodo.cantidad_datos == 0:
                        nodo.set_hijo(i, None)
                    else:
                        self.reordenar_datos(posicion, sig_nodo)

                elif sig_nodo.hijos_validos() == 1:
                    sig_nodo.set_dato(posicion, None)
                    sig_nodo.cantidad_datos = sig_nodo.cantidad_datos - 1
                    #---REORDENAR LOS DATOS----
                    if sig_nodo.cantidad_datos == 0:
                        #conectar el unico hijo con el nodo padre
                        posicion_hijo = sig_nodo.pos_primer_hijo()
                        hijo = sig_nodo.get_hijo(posicion_hijo)

                        nodo.set_hijo(i, hijo)
                    else:
                        self.reordenar_datos(posicion, sig_nodo)
                    print("tiene un hijo valido")
                elif sig_nodo.hijos_validos > 1:
                    print("tiene varios hijos")
            else:
                self.__eliminar_recursivo(sig_nodo, valor, nodo_del_valor)

    def imprimir_datos_nodo(self, nodo):
        nodopos = nodo.get_hijo(0)
        padre = nodo.nodo_padre
        if padre is None:
            print("soy la raiz perro")
        else:
            print(padre.get_dato(0))
            print(nodopos.get_dato(0))

    def conv_a_dic(self, nodo , padre, visitados = None):
        '''
        Convierte los nodos del arbol a diccionario.
        Parametro:
            nodo (NodoBB): la referencia a la direccion de la raiz de arbol.
        Returna:
            diccionario (dict): Que representa el nodo y sus hijos, 
            None si el nodo es nulo.
        '''
        if nodo is None:
            return None
        # Inicializa el conjunto de visitados en la primera llamada
        if visitados is None:
            visitados = set()
        # Usar un identificador único para cada nodo
        if nodo in visitados:
            return None  # Si ya se ha visitado, no lo procesamos
        visitados.add(nodo)  # Marca este nodo como visitado
        children = [] # Inicializa la lista de hijos del nodo
        nodo_data = []  # Inicializa la lista de datos del nodo
        # Obtiene los datos de este nodo
        for j in range(nodo.cantidad_datos):
            dato = nodo.get_dato(j)
            if dato is not None:
                nodo_data.append(dato)  # Agrega cada dato a la lista
        
        padre_data = []
        if padre is not None:
            for j in range(padre.cantidad_datos):
                dato = padre.get_dato(j)
                if dato is not None:
                    padre_data.append(dato)
        # Crear un diccionario con todos los datos del nodo
        arbol_dict = {
            'name': nodo_data,
            'parent': padre_data,
            'children': children
        }
        # Obtienet los hijos de este nodo
        for i in range(nodo.cantidad_datos + 1): # los hijos son uno mas que los datos
            hijo = nodo.get_hijo(i)  # Obtiene el hijo en la posición i
            if hijo is not None:
                #si el nodo no es nulo se agrega a la lista
                hijo_dict = self.conv_a_dic(hijo, nodo ,visitados)
                if hijo_dict:
                    children.append(hijo_dict)
        
        return arbol_dict

    def get_diccionario(self):
        '''
        Retorna:
            diccionario (dict): Que representa al arbol binario completo.
        '''
        return self.conv_a_dic(self.raiz, None)
    


    """ def recorrido_por_niveles(self):
        '''
        Realiza el recorrido por niveles del árbol y devuelve los nodos junto con sus padres.

        Retorna:
            List[List]: Lista de pares [NODO ACTUAL], [PADRE].
        '''
        if self.__raiz is None:
            return []

        resultado = []
        cola = [(self.__raiz, None)]  # Cola para el recorrido: (Nodo, Padre)

        while cola:
            nodo_actual, nodo_padre = cola.pop(0)
            
            # Obtener los datos del nodo actual y el padre
            datos_actuales = [nodo_actual.get_dato(i) for i in range(nodo_actual.cantidad_datos)]
            datos_padre = []
            if nodo_padre:
                datos_padre = [nodo_padre.get_dato(i) for i in range(nodo_padre.cantidad_datos)]

            resultado.append([datos_actuales, datos_padre])

            # Añadir los hijos del nodo actual a la cola
            for i in range(nodo_actual.hijos_permitidos()):
                hijo = nodo_actual.get_hijo(i)
                if hijo is not None:
                    cola.append((hijo, nodo_actual))

        return resultado """
    def recorrido_por_niveles(self):
        '''
        Realiza el recorrido por niveles del árbol y devuelve los nodos junto con sus padres y niveles.

        Retorna:
            List[List]: Lista de listas con formato [[NODO ACTUAL], [PADRE], NIVEL].
        '''
        if self.__raiz is None:
            return []

        resultado = []
        cola = [(self.__raiz, None, 0)]  # Cola para el recorrido: (Nodo, Padre, Nivel)

        while cola:
            nodo_actual, nodo_padre, nivel = cola.pop(0)
            
            # Obtener los datos del nodo actual y el padre
            datos_actuales = [nodo_actual.get_dato(i) for i in range(nodo_actual.cantidad_datos)]
            datos_padre = []
            if nodo_padre:
                datos_padre = [nodo_padre.get_dato(i) for i in range(nodo_padre.cantidad_datos)]

            # Agregar el nodo actual al resultado con su nivel
            resultado.append([[datos_actuales, datos_padre, nivel]])

            # Añadir los hijos del nodo actual a la cola con su nivel incrementado
            for i in range(nodo_actual.hijos_permitidos()):
                hijo = nodo_actual.get_hijo(i)
                if hijo is not None:
                    cola.append((hijo, nodo_actual, nivel + 1))

        return resultado




    def get_datos(self):
        for i in range(0, self.raiz.cantidad_datos):
            if self.raiz.get_dato(i) is not None:
                print(self.raiz.get_dato(i))


if __name__ == '__main__':
    tree = ArbolMVias(4)
    tree.insertar_dato(300)
    tree.insertar_dato(150)
    tree.insertar_dato(400)
    tree.insertar_dato(100)
    tree.insertar_dato(110)
    tree.insertar_dato(180)
    tree.insertar_dato(210)
    tree.insertar_dato(200)
    tree.insertar_dato(190)
    print(tree.recorrido_por_niveles())