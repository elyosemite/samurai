class Pen:
    def __init__(self, brand) -> None:
        self.__brand = brand

    @property
    def brand(self):
        return self.__brand

    def write(self):
        print(f"Pen is writing ...")