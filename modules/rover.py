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
    # TODO: test me
    if single_command == "L":
      direction_index = self.compass.index(self.direction) - 1
      direction_index = direction_index if direction_index > -1 else direction_index + 4
      self.direction = self.compass[direction_index]
    elif single_command == "R":
      direction_index = self.compass.index(self.direction) + 1
      direction_index = direction_index if direction_index < 4 else direction_index % 4
      self.direction = self.compass[direction_index]
    elif single_command == "M":
      target_posx, target_posy = self.calculate_next_position_on_move()
      cur_posx, cur_posy = self.locx, self.locy
      self.locx = target_posx
      self.locy = target_posy
      self.grid.update_location(self, cur_posx, cur_posy)
      


  def is_command_valid(self, command):
    # TODO: test me
    if command in ["R", "L"]:
      return True
    else:
      return  self.do_i_stay_in_grid() and self.is_path_clear()

  def calculate_next_position_on_move(self):
    if self.direction == "N":
      return self.locx, self.locy -1
    if self.direction == "E":
      return self.locx +1, self.locy
    if self.direction == "S":
      return self.locx, self.locy + 1
    if self.direction == "W":
      return self.locx -1, self.locy
  
  def do_i_stay_in_grid(self):
    target_posx, target_posy = self.calculate_next_position_on_move()
    return self.grid.length > target_posx > -1 and  self.grid.width > target_posy > -1
  
  def is_path_clear(self):
    target_posx, target_posy = self.calculate_next_position_on_move()
    return self.grid.is_location_available(target_posx, target_posy)
  
  def __repr__(self):
    return self.direction
