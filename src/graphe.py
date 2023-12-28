#
# Class Graphe, taking a set of arguments and attack relations
#

class Graphe:
    def __init__(self, arguments, atk):
        self.__arguments=arguments
        self.__atk=atk

    def __get_arguments(self):
        return self.__arguments
    def __get_atk(self):
        return self.__atk
    
    def __set_arguments(self, arguments):
        self.__arguments = arguments
    def __set_atk(self, atk):
        self.__atk = atk

    arguments = property(__get_arguments, __set_arguments)
    atk = property(__get_atk, __set_atk)

