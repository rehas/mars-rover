# !/usr/local/bin/python3

# Unit Tests
import unittest
from modules.grid import Grid
from modules.rover import Rover
from modules.satellite_link import SatelliteLink


class TestGridMethods(unittest.TestCase):
  '''Grid Tests'''
  def test_grid_init_size1(self):
    test_grid = Grid(4, 5)
    self.assertEqual(len(test_grid.grid), 5)

  def test_grid_init_size2(self):
    test_grid = Grid(4, 5)
    self.assertEqual(len(test_grid.grid[0]), 4)

  def test_grid_placement(self):
    test_grid = Grid(4, 5)
    test_rover = Rover(test_grid, 2, 3, "S")
    test_grid.insert_rover(test_rover)
    self.assertEqual(test_grid.grid[3][2].direction, test_rover.direction)

class TestRoverMethods(unittest.TestCase):
  '''Rover Tests'''
  def test_rover_turns(self):
    test_grid = Grid(5, 5)
    test_rover = Rover(test_grid, 2, 3, "N")
    test_grid.insert_rover(test_rover)
    test_rover.execute_single_command("L")
    self.assertEqual(test_rover.direction, "W")
    test_rover.execute_single_command("L")
    self.assertEqual(test_rover.direction, "S")
    test_rover.execute_single_command("L")
    self.assertEqual(test_rover.direction, "E")
    test_rover.execute_single_command("L")
    self.assertEqual(test_rover.direction, "N")
    test_rover.execute_single_command("R")
    self.assertEqual(test_rover.direction, "E")
    test_rover.execute_single_command("R")
    self.assertEqual(test_rover.direction, "S")
    test_rover.execute_single_command("R")
    self.assertEqual(test_rover.direction, "W")
    test_rover.execute_single_command("R")
    self.assertEqual(test_rover.direction, "N")

  def test_rover_movement(self):
    test_grid = Grid(5, 5)
    test_rover = Rover(test_grid, 0, 0, "S")
    test_grid.insert_rover(test_rover)
    test_rover.get_commands("MMMMLMMMM")
    test_rover.execute_commands()
    self.assertEqual((test_rover.locx, test_rover.locy), (4, 4))

  def test_rover_fall_prevension(self):
    test_grid = Grid(3, 3)
    test_rover = Rover(test_grid, 0, 0, "N")
    test_grid.insert_rover(test_rover)
    self.assertFalse(test_rover.is_command_valid("M"))

  def test_rover_collision_prevension(self):
    test_grid = Grid(3, 3)
    test_rover1 = Rover(test_grid, 1, 1, "N")
    test_rover2 = Rover(test_grid, 1, 2, "N")
    test_grid.insert_rover(test_rover1)
    test_grid.insert_rover(test_rover2)
    test_grid.display()
    self.assertTrue(test_rover1.is_command_valid("M") and not test_rover2.is_command_valid("M"))


if __name__ == '__main__':
  unittest.main()
