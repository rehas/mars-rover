'''
Rover module
'''
import logging
from modules.grid import Grid
class Rover():
  '''class to handle command executions on a rover'''
  def __init__(self, grid: Grid, locx, locy, direction):
    self.grid = grid
    self.locx = locx
    self.locy = locy
    self.direction = direction
    self.commands = None
    self.compass = ["N", "E", "S", "W"]

  def get_commands(self, commands):
    '''Get and set commands for rover'''
    logging.info("I'm rover at %s, %s", self.locx, self.locy)
    logging.info("I've got commands %s", commands)
    self.commands = commands

  def execute_commands(self):
    '''Executes command for the rover'''
    for cmd in self.commands:
      if not self.is_command_valid(cmd):
        logging.error("command not valid exiting execution command: %s", cmd)
        return
      self.execute_single_command(cmd)
    logging.info("Executed commands %s", self.commands)

  def execute_single_command(self, single_command):
    '''Execute Single Command for rotation or movement'''
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
    '''Validate single command'''
    if command in ["R", "L"]:
      return True
    do_i_stay_in_grid = self.do_i_stay_in_grid()
    if not do_i_stay_in_grid:
      print("Fall detected check logs")
      logging.warning("Fall detected for rover facing %s at location \
%s, %s", self.direction, self.locx, self.locy)
    is_path_clear = self.is_path_clear()
    if not is_path_clear:
      print("Collision detected check logs")
      logging.warning("Collision detected for rover facing %s at location \
%s, %s", self.direction, self.locx, self.locy)
    return  do_i_stay_in_grid and is_path_clear

  def calculate_next_position_on_move(self):
    '''Calculates the next position based on current location and intended move'''
    if self.direction == "N":
      return self.locx, self.locy -1
    if self.direction == "E":
      return self.locx +1, self.locy
    if self.direction == "S":
      return self.locx, self.locy + 1
    if self.direction == "W":
      return self.locx -1, self.locy

  def do_i_stay_in_grid(self):
    '''Fall detection'''
    target_posx, target_posy = self.calculate_next_position_on_move()
    return self.grid.length > target_posx > -1 and  self.grid.width > target_posy > -1

  def is_path_clear(self):
    '''Collision Detection'''
    target_posx, target_posy = self.calculate_next_position_on_move()
    return self.grid.is_location_available(target_posx, target_posy)

  def __repr__(self):
    return self.direction
