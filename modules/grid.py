'''
  Grid Module
'''
# from modules.rover import Rover
from pprint import pprint
class Grid():
  def __init__(self, width: int, length: int):
    self.width = width
    self.length = length
    self.grid = self.initialize_grid(width, length)

  def __repr__(self):
    return str(self.grid)

  def initialize_grid(self, wide: int, long: int):
    '''Initalizes empty grid with sizes'''
    arr = [[0 for x in range(wide)] for y in range(long)]
    return arr

  def display(self):
    pprint(self.grid)

  # def insert_rover(self, locx: int, locy: int, direction: str):
  #   # Assumes initial locations are valid
  #   if self.is_location_available(locx, locy):
  #     self.grid[locx][locy] = direction
  #   else:
  #     # TODO:# log or throw exception
  #     raise Exception(f"Rover insertion failed for : {locx},{locy}")
  
  def insert_rover(self, rover):
    # Assumes initial locations are valid
    if self.is_location_available(rover.locx, rover.locy):
      self.grid[rover.locx][rover.locy] = rover
    else:
      # TODO:# log or throw exception
      raise Exception(f"Rover insertion failed for : {rover.locx},{rover.locy}")

  def is_location_available(self, locx: int, locy: int):
    return locx < self.width and locy < self.length and not self.grid[locx][locy] 