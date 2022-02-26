class Mejora:

    def __init__(self, mejora):
        self.__mejora = mejora

    def promedio(self):
        if len(self.__mejora) > 0:
            return sum(self.__mejora) / len(self.__mejora)
        else:
            return None