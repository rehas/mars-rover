'''
  Grid Module
'''
# from modules.rover import Rover
import logging
from pprint import pprint, pformat
class Grid():
  '''Grid class, responsible for generating, displaying and updating grid information'''
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
    '''Displays grid status'''
    pprint(self.grid)

  def update_location(self, rover, old_locx, old_locy):
    '''Moves rover to next position'''
    self.insert_rover(rover)
    self.grid[old_locy][old_locx] = 0

  def insert_rover(self, rover):
    '''Inserts rovers into the grid'''
    # Assumes initial locations are valid
    if self.is_location_available(rover.locx, rover.locy):
      self.grid[rover.locy][rover.locx] = rover
    else:
      logging.error("Rover insertion failed for : %s , %s", rover.locx, rover.locy)
      raise Exception(f"Rover insertion failed for : {rover.locx},{rover.locy}")

  def is_location_available(self, locx: int, locy: int):
    '''Check if the location is occupied and within limits of the grids'''
    logging.info("availability check for locations locx:%s, locy:%s \
on the grid width: %s, length %s", locx, locy, self.width, self.length)
    return locx < self.width and locy < self.length and not self.grid[locy][locx]
