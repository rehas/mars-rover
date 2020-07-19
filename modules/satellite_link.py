'''
Satellite module
'''
import logging
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
    '''Checks if the command file is in valid format'''
    commands = open(file, "r")
    commands_array = [x.strip() for x in commands.readlines()]
    # First line should be grid size of 2 ints
    coordx, coordy = commands_array[0].strip().split()
    if not(coordx.isdigit() and coordy.isdigit()):
      # Log or print
      print("Size not parsed")
      logging.error("Size not parsed %s %s", coordx, coordy)
      return False
    for i, c_line in enumerate(commands_array[1:]):
      if i%2 == 0:
        # Must be a location initializer
        locx, locy, direction = c_line.split()
        if not (locx.isdigit() and locy.isdigit() and direction.isalpha()):
          print("Location initalizer not parsed")
          logging.error("Location initalizer not parsed %s %s %s", locx, locy, direction)
          return False
      else:
        # Must be a movement command
        if not set(c_line).issubset(set("MLR")):
          print("Movement commands not parsed")
          logging.error("Movement commands not parsed %s", c_line)
          return False
    logging.info("Command File Valid %s", file)
    return True

  def get_commands_file(self, commands_file):
    '''Receives and validates command file, generates the grid and prepares rovers for commands'''
    commands = open(commands_file, "r").readlines()

    if not self.is_valid_command_file(commands_file):
      print("Command File Not Valid")
      logging.error("Command Not File Valid %s", commands_file)
      raise Exception("Command File Error, check logs")
    grid_size = commands[0].split()
    self.grid = Grid(int(grid_size[0]), int(grid_size[1]))

    for i in range(0, len(commands[1:]), 2):
      rover_location, rover_commands = [x.strip() for x in commands[1+i:3+i]]

      locx, locy, direction = [int(x) if x.isdigit() else x for x in rover_location.split()]
      rov = Rover(self.grid, locx, locy, direction)

      self.grid.insert_rover(rov)
      self.rovers_commands.append((rov, rover_commands))
    logging.info("Command file parsed and grid initialized")
    logging.info("Initial Grid \n %s", self.grid)

  def execute_commands(self):
    '''For the Rovers under this satellite sends the respective commands for execution'''
    for rov_com in self.rovers_commands:
      rov, com = rov_com
      rov.get_commands(com)
      rov.execute_commands()

  def send_status(self):
    '''Returns the current status of the grid'''
    return self.grid
