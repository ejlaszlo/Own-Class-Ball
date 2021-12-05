# Emma Laszlo, November 28 2021
# Assignment 10.1: Your Own Class
#required to submit a script that includes your implementation 
# of a custom class that is based on a real-world object.

# set Ball as class 
class Ball: 
   # set variables / class variables 
    type = ""
    pressure = 0
    lb_moles = 0
    volume = 0
    temperature = 527.67      # room temperature in Rankine
    gas_constant = 10.73159
    atm_psi = 14.5            # atmosferic pressure in PSI
    diameter = {}
    diameter["basketball"] = 9.5
    diameter["soccer"] = 8.66
    diameter["waterpolo"] = 8.5
    pi = 3.1415
    
    # define __init__ functions 
    def __init__(self, ball_type, pressure): 
        # set type, pressure, volume, and lb moles 
        self.type = ball_type 
        self.pressure = pressure
        self.volume = self.get_volume()
        self.lb_moles = self.get_moles()
   
    # define get_moles 
    def get_moles(self):
        # return formula to get moles
        return (self.pressure + self.atm_psi) * self.volume / (self.gas_constant * self.temperature)

    # define get for volume 
    def get_volume(self):
        # set diamater and radius 
        diam = self.diameter [self.type]
        radius = diam / 2 / 12
        # return the volume 
        return (4/3 * self.pi * (radius**3))

    # define inflate function, other method
    def inflate(self, liters):
        # calculate moles
        moles = liters / 24
        # calculate pound moles
        self.lb_moles = self.lb_moles + moles * 0.00220462
        # calculate pressure
        self.pressure = (self.lb_moles * self.gas_constant * self.temperature) / self.volume - self.atm_psi

    # define deflate function, other method
    def deflate(self, liters):
        # calculate moles 
        moles = liters / 24
        # calculate pound moles 
        self.lb_moles = self.lb_moles - moles * 0.00220462
        # calculate pressure 
        self.pressure = (self.lb_moles * self.gas_constant * self.temperature) / self.volume - self.atm_psi

    # define ball type 
    def set_type(self, type):
        # set type 
        self.type = type
        #set volume and moles 
        self.volume = self.get_volume()
        self.lb_moles = self.get_moles()

    # define get pressure function 
    def set_pressure(self, pres):
        # if pressure is less then 0 error 
        if pres < 0: 
            print("pressure cannot be less than zero.")
            raise ValueError
        else:
            self.pressure = pres
            self.lb_moles = self.get_moles()

    # define get type of ball function 
    def get_type(self):
        return self.type

    # def get_pressure function 
    def get_pressure(self):
        return self.pressure
    

# define main function with demo program 
def main():
    # inflated basketball 
    bb = Ball("basketball", 4)
    bb.inflate(1)
    print(bb.get_pressure())
    bb.inflate(1)
    print(bb.get_pressure())
    #inflated soccer ball 
    s = Ball("soccer", 8)
    s.inflate(1)
    print(s.get_pressure())
    s.inflate(1)
    print(s.get_pressure())
    # inflated water polo ball 
    w = Ball("waterpolo", 5)
    w.inflate(1)
    print(s.get_pressure())
    w.inflate(1)
    print(w.get_pressure())

    w = Ball("waterpolo", 5)
    w.deflate(1)
    print(s.get_pressure())
    w.deflate(1)
    print(w.get_pressure())



if __name__ == "__main__" :
    main()