'''
Satellite module
'''
from modules.grid import Grid
from modules.rover import Rover
class SatelliteLink():
  '''class to handle communications between earth and mars,
  orbiting around mars to oversee rovers
  '''
  def __init__(self):
    self.grid = None
    self.rovers_commands = []

  def is_valid_command_file(self, file):
    commands = open(file, "r")
    commands_array = [x.strip() for x in commands.readlines()]
    # First line should be grid size of 2 ints
    coordx, coordy = commands_array[0].strip().split()
    if not(coordx.isdigit() and coordy.isdigit()):
      # Log or print
      print("Size not parsed")
      return False
    for i, c_line in enumerate(commands_array[1:]):
      if i%2 == 0:
        # Must be a location initializer
        locx, locy, direction = c_line.split()
        if not (locx.isdigit() and locy.isdigit() and direction.isalpha()):
          print("Location initalizer not parsed")
          return False
      else:
        # Must be a movement command
        if not set(c_line).issubset(set("MLR")):
          print("Movement commands not parsed")
          return False
    print("Command File Valid")
    return True

  def get_commands_file(self, commands_file):
    commands = open(commands_file, "r").readlines()

    if not self.is_valid_command_file(commands_file):
      #TODO: Log or throw exception
      print("Command File Not Valid")
      return None
    grid_size = commands[0].split()
    self.grid = Grid(int(grid_size[0]), int(grid_size[1]))
    # for i, command in enumerate(commands[1:]):
    for i in range(0, len(commands[1:]), 2):
      rover_location, rover_commands = [x.strip() for x in commands[1+i:3+i]]

      locx, locy, direction = [int(x) if x.isdigit() else x for x in rover_location.split()]
      rov = Rover(self.grid, locx, locy, direction )

      self.grid.insert_rover(rov)
      self.rovers_commands.append((rov, rover_commands))

  def execute_commands(self):
    for rov_com in self.rovers_commands:
      rov, com = rov_com
      rov.get_commands(com)
      rov.execute_commands()

  def send_status(self):
    return self.grid
