'''
Rover module
'''
from modules.grid import Grid
class Rover():
  '''class to handle command executions on a rover'''
  def __init__(self, grid:Grid, locx, locy, direction):
    self.grid = grid
    self.locx = locx
    self.locy = locy
    self.direction = direction
    self.commands = None
    self.compass = ["N", "E", "S", "W"]

    print("This initializes a Rover class")
  def get_commands(self, commands):
    print(f"I'm rover at {self.locx}, {self.locy}")
    print(f"I've got commands {commands}")
    self.commands = commands
  
  def execute_commands(self):
    for c in self.commands:
      if not self.is_command_valid(c):
        print("command not valid exiting execution")
        return
      self.execute_single_command(c)
    print(f"Executed commands {self.commands}")

  def execute_single_command(self, single_command):
    if single_command == "L":
      direction_index = self.compass.index(self.direction) - 1
      direction_index = direction_index if direction_index > -1 else direction_index + 4
      self.direction = self.compass[direction_index]

  def is_command_valid(self, command):
    return True

  def __repr__(self):
    return self.direction
