class NodeABB:

    def __init__(self, value, right, left):
        self.__value = value
        self.__right = right
        self.__left = left

    def get_value(self):
        return self.__value

    def get_right(self):
        return self.__right

    def get_left(self):
        return self.__left

    def set_value(self, value):
        self.__value = value

    def set_right(self, right):
        self.__right = right

    def set_left(self, left):
        self.__left = left
