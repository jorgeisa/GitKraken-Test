from NodeABB import NodeABB


class ABB:
    InOrder = []

    def __init__(self):
        self.__root = None

    # Metodos Para Agregar Nodos Al Arbol
    def addNode(self, value):
        if self.__root is None:
            self.__root = NodeABB(value, None, None)
        else:
            self.__addNode(value, self.__root)

    def __addNode(self, value, root):
        if value < root.get_value() and root.get_left() is None:
            root.set_left(NodeABB(value, None, None))
        elif root.get_value() < value and root.get_right() is None:
            root.set_right(NodeABB(value, None, None))
        elif value < root.get_value():
            self.__addNode(value, root.get_left())
        elif root.get_value() < value:
            self.__addNode(value, root.get_right())

    # Metodos Para Recorrer Los Arboles
    def RecPreOrder(self, root):
        if root is not None:
            print(root.get_value(), end=" ")
            self.RecPreOrder(root.get_left())
            self.RecPreOrder(root.get_right())

    def RecSym(self, root):
        if root is not None:
            self.RecSym(root.get_left())
            print(root.get_value(), end=" ")
            self.InOrder.append(root.get_value())
            self.RecSym(root.get_right())

    def RecPostOrder(self, root):
        if root is not None:
            self.RecPostOrder(root.get_left())
            self.RecPostOrder(root.get_right())
            print(root.get_value(), end=" ")

    # Metodos Para Buscar Datos En El Arbol
    def Search(self, value):
        if self.__root is None:
            print("No Hay Datos Almacenados")
        else:
            return self.__Search(value, self.__root, 1)

    def __Search(self, value, root, level):
        if root.get_value() == value:
            print()
            print("\nEl Valor " + str(value) + " Se Encuentra En El Nivel " + str(level))
            return root
        else:
            if value < root.get_value():
                level += 1
                return self.__Search(value, root.get_left(), level)
            elif root.get_value() < value:
                level += 1
                return self.__Search(value, root.get_right(), level)

    def _SearchDelete(self, value, root):
        if root is None:
            print("Error El Dato A Eliminar No Existe")
        else:
            if root.get_right().get_value() == value:
                aux = root.get_right()
                root.set_right(None)
                return aux
            elif root.get_left().get_value() == value:
                aux = root.get_left()
                root.set_left(None)
                return aux
            elif value < root.get_value():
                return self._SearchDelete(value, root.get_left())
            elif root.get_value() < value:
                return self._SearchDelete(value, root.get_right())

    # Metodos Para Eliminar Un Nodo Del Arbol
    def Delete(self, value):
        if self.__root is None:
            print("No Hay Datos Almacenados")
        else:
            self.RecSym(self.__root)
            self.__Delete(value, self.__root)

    def __Delete(self, value, root):
        if (root.get_right() is not None) and (root.get_right().get_value() == value):
            if (root.get_right().get_left() is None) and (root.get_right().get_right() is None):
                root.set_right(None)
            elif (root.get_right().get_left() is not None) and (root.get_right().get_right() is None):
                root.set_right(root.get_right().get_left())
            elif (root.get_right().get_left() is None) and (root.get_right().get_right() is not None):
                root.set_right(root.get_right().get_right())
            elif (root.get_right().get_left() is not None) and (root.get_right().get_right() is not None):
                suc = self.InOrder.index(value)
                aux = self._SearchDelete(self.InOrder[suc + 1], self.__root)
                aux.set_left(root.get_right().get_left())
                aux.set_right(root.get_right().get_right())
                root.set_right(aux)
        elif (root.get_left() is not None) and (root.get_left().get_value() == value):
            if (root.get_left().get_left() is None) and (root.get_left().get_right() is None):
                root.set_left(None)
            elif (root.get_left().get_right() is not None) and (root.get_left().get_right() is None):
                root.set_left(root.get_left().get_right())
            elif (root.get_leftt().get_left() is None) and (root.get_left().get_right() is not None):
                root.set_left(root.get_left().get_left())
            elif (root.get_left().get_left() is not None) and (root.get_left().get_right() is not None):
                suc = self.InOrder.index(value)
                aux = self._SearchDelete(self.InOrder[suc + 1], self.__root)
                aux.set_left(root.get_left().get_left())
                aux.set_right(root.get_left().get_right())
                root.set_left(None)
        else:
            if value < root.get_value():
                self.__Delete(value, root.get_left())
            elif root.get_value() < value:
                self.__Delete(value, root.get_right())

    # Get De La Raiz Del Arbol
    def get_root(self):
        return self.__root
