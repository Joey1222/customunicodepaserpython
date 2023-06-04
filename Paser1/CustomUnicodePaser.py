from colormap import rgb2hex


class CustomUnicodePaser():
    def __init__(self):
        self.colorRed = 0
        self.colorGreen = 0
        self.colorBlue = 0
        self.colornormal = "white"
        self.bitlist = []

    def AddRGBValsToList(self, Red: int, Green: int, Blue: int):
        try:
            self.colorRed = int(Red)
            self.colorGreen = int(Green)
            self.colorBlue = int(Blue)
        except ValueError as e:
            print("Error: " + e)
            print("Please only use numbers!")
            exit()

        self.bitlist.append(
            rgb2hex(self.colorRed, self.colorGreen, self.colorBlue))
