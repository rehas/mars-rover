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
    print("This initializes a satellite class")
    # self.commandfile = command_file if self.is_valid_command_file(command_file) else None
    self.grid = None
    # self.commands = None
    self.rovers_commands = []
    # pass
  
  def is_valid_command_file(self, file):
    commands = open(file, "r")
    for c_line in commands.readlines():
      print(c_line.strip())
    # TODO: Add validation logic
    return True
  
  def get_commands_file(self, commands_file):
    commands = open(commands_file, "r").readlines()

    if not self.is_valid_command_file(commands_file):
      #TODO: Log or throw exception
      return None
    grid_size = commands[0].split()
    self.grid = Grid(int(grid_size[0]), int(grid_size[1]))
    self.grid.display()

    # for i, command in enumerate(commands[1:]):
    for i in range(0, len(commands[1:]), 2):
      rover_location, rover_commands = [x.strip() for x in commands[1+i:3+i]]
      print(f"rover location  : {rover_location}")
      print(f"rover commands  : {rover_commands}")
      
      locx, locy, direction = [int(x) if x.isdigit() else x for x in rover_location.split()]
      rov = Rover(self.grid, locx, locy, direction )
      
      self.grid.insert_rover(rov)
      self.rovers_commands.append((rov, rover_commands))
    self.grid.display()

  def execute_commands(self):
    for rov_com in self.rovers_commands:
      rov, com = rov_com
      print(rov)
      print(com)
      rov.get_commands(com)
      rov.execute_commands()

  def send_results(self):
    pass
  
