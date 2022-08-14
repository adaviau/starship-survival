

class Machine:
    def __init__(self, function):
        self.function = function
        self.__operational = True
        self.__powered = False
        self.__running = False

    def is_operational(self):
        return self.__operational

    def is_powered(self):
        return self.__powered

    def is_running(self):
        return self.__running

    def state_information(self):
        output = self.function + " machine is "
        if ( self.is_operational() == False ):
            output = output + " not "
        output = output + " operational, "
        if ( self.is_powered() == False ):
            output = output + " un"
        output = output + "powered"

class AirCleaner(Machine):
    def __init__(self):
        Machine.__init__(self, "Air Cleaner")

class Heating(Machine):
    def __init__(self):
        Machine.__init__(self, "Heating")

class Cooling(Machine):
    def __init__(self):
        Machine.__init__(self, "Cooling")

class Fan(Machine):
    def __init__(self):
        Machine.__init__(self, "Fan")

class Power(Machine):
    def __init__(self):
        Machine.__init__(self, "Power")

class Light(Machine):
    def __init__(self):
        Machine.__init__(self, "Light")