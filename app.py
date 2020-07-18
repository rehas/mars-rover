# !/usr/local/bin/python3
"""Main App Module"""
import sys, os
from modules.satellite_link import SatelliteLink

if "mars-rover" in os.listdir():
  os.chdir("mars-rover")

print("Hello Mars Rover")

COMMAND_FILE_PATH = "./command_files/command1.txt"

mySat = SatelliteLink()

mySat.get_commands_file(COMMAND_FILE_PATH)
mySat.send_status().display()
mySat.execute_commands()
mySat.send_status().display()
