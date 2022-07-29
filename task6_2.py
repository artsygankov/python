# Program with class Road

class Road:
    def __init__(self, arg1=0, arg2=0):
        self.asf_length = arg1
        self.asf_width = arg2

    def asfalt_calculate(self):
        return self.asf_length * self.asf_width * 25 * 5


UsrRoad = Road(15,25)
print(UsrRoad.asfalt_calculate())
