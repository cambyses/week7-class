class Car:

  def __init__(self):
    self.speed = 0
    self.odometer = 0
    self.vin = id(self)

  def set_speed(self, new_speed):
    self.speed = new_speed

  def drive_for(self, minutes):
    pass;


# Let's drive!

