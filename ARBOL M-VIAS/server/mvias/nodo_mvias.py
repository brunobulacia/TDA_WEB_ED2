class NodoMvias:
    '''
    Representa un Nodo en el arbol m_vias.

    Atributos:

        __orden (Int): Almacena el orden de un nodo, decir cuantos hijos tendra.
        __lista_datos (Lista): Lista de (orden-1) espacios para almacenar datos.
        __lista_hijos (Lista): Lista de (orden) espacios para almacenar referencia a hijos.
        __cantidad_dato (Int): Almacena la cantidad de datos en la lista (lista_datos), inicia en 0.
    '''
    def __init__(self, orden):
        self.__orden = orden
        self.__lista_datos =[]
        self.__lista_hijos = []
        self.__cantidad = 0
        self.__padre = None

        for i in range(orden-1):
            self.__lista_datos.insert(i, None)
            self.__lista_hijos.insert(i, None)

        self.__lista_hijos.append(None)

    @property
    def cantidad_datos(self):
        '''
        Retorna:
            La cantidad de datos validos en la lista_datos
        '''
        return self.__cantidad

    @cantidad_datos.setter
    def cantidad_datos(self, cantidad):
        '''
        Parametro:

            cantidad (int): El nuevo valor que hace referencia a 
            la cantidad de datos de la lista_datos.
        '''
        self.__cantidad = cantidad

    @property
    def nodo_padre(self):
        '''
        Retorna:

            El padre de dicho nodo.
        '''
        return self.__padre

    @nodo_padre.setter
    def nodo_padre(self, padre):
        '''
        Establece el padre para un nodo.

        Parametro:

            padre (NodoMvias): Referencia al nodo el cual sera el padre.
        '''
        self.__padre = padre

    def datos_permitidos(self):
        '''
        Retorna:
        
            La lista completa de datos incluido las posiciones sin dato.
        '''
        return self.orden_nodo() - 1

    def hijos_permitidos(self):
        '''
        Retorna:
        
            La lista completa de hijos incluido las posiciones sin dato
        '''
        return self.orden_nodo()

    def orden_nodo(self):
        '''
        Retorna:
        
            El orden de dicho nodo, es decir cuantos hijos puede tener.
        '''
        return self.__orden

    def hay_espacio(self):
        '''
        booleano que devuelve True o False si hay espacio.

        Retorna:

            True: si hay espacio en el nodo.
            False: caso contrario.
        '''
        if self.cantidad_datos == self.datos_permitidos():
            return False
        return True

    def get_dato(self, posicion):
        '''
        Devuelve un dato de una determinada posicion
        
        Parametro:

            posicion (int): La referencia a la posicion dentro de la lista_datos
        '''
        if posicion < self.datos_permitidos():
            return self.__lista_datos[posicion]
        return -1

    def set_dato(self, posicion, dato):
        '''
        Paramentro:
        
            posicion (int): Referencia a la posicion dentro de la lista_datos.
            dato (int): valor que se desea almacenar.
        '''
        self.__lista_datos[posicion] = dato

    def get_hijo(self, posicion):
        '''
        Devuelve un dato de una determinada posicion
        
        Parametro:

            posicion (int): La referencia a la posicion dentro de la lista_datos
        '''
        return self.__lista_hijos[posicion]

    def set_hijo(self, posicion, nodo):
        '''
        Paramentro:
        
            posicion (int): Referencia a la posicion dentro de la lista_datos.
            dato (int): valor que se desea almacenar.
        '''
        self.__lista_hijos[posicion] = nodo

    def hijo_vacio(self, posicion):
        '''
        Retorna:
        
            True: si la posicion es None.
            False: caso contrario.
        '''
        if self.get_hijo(posicion) is None:
            return True
        return False

    def hijos_validos(self):
        '''
        Retorna:
        
            True: Si tiene un solo hijo.
            False: Caso contrario.
        '''
        contador = 0
        for i in range(self.cantidad_datos + 1):
            #print(i)
            if not self.hijo_vacio(i):
                contador += 1
        return contador

    def pos_primer_hijo(self):
        '''
        Retorna:
        
            La posicion de su primer hijo en el nodo.
        '''
        for i in range(self.cantidad_datos + 1):
            if not self.hijo_vacio(i):
                return i
        return None



def main():
    pass 

if __name__ == '__main__':
    main()





""" tree.insertar_dato(150)
tree.insertar_dato(300)
tree.insertar_dato(400)
tree.insertar_dato(100)
tree.insertar_dato(110)
tree.insertar_dato(180)
tree.insertar_dato(190)
tree.insertar_dato(200)
tree.insertar_dato(120)


[
 [[NODO ACTUAL], [PADRE], NIVEL]
]


[
    [[150,300,400], [],0]
    [[100, 110], [150,300,400],1],
    [[180,200,210],[150,300,400],1],
    [[190], [180,200,210],2]
] """