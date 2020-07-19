'''
  Grid Module
'''
# from modules.rover import Rover
from pprint import pprint, pformat
class Grid():
  def __init__(self, width: int, length: int):
    self.width = width
    self.length = length
    self.grid = self.initialize_grid(width, length)

  def __repr__(self):
    return str(pformat(self.grid))

  def initialize_grid(self, wide: int, long: int):
    '''Initalizes empty grid with sizes'''
    arr = [[0 for x in range(wide)] for y in range(long)]
    return arr

  def display(self):
    pprint(self.grid)

  def update_location(self, rover, old_locx, old_locy):
    self.grid[old_locy][old_locx] = 0
    self.insert_rover(rover)
  
  def insert_rover(self, rover):
    # Assumes initial locations are valid
    if self.is_location_available(rover.locx, rover.locy):
      self.grid[rover.locy][rover.locx] = rover
    else:
      # TODO:# log or throw exception
      raise Exception(f"Rover insertion failed for : {rover.locx},{rover.locy}")

  def is_location_available(self, locx: int, locy: int):
    # print(f"availability checking locations locx:{locx} , locy:{locy} ")
    # print(f" width: {self.width} , length {self.length}")
    return locx < self.width and locy < self.length and not self.grid[locy][locx]
