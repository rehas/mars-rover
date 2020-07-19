# !/usr/local/bin/python3
"""Main App Module"""
import sys
import os
import logging
import datetime
from modules.satellite_link import SatelliteLink

if "mars-rover" in os.listdir():
  os.chdir("mars-rover")

print("Hello Mars Rover")

if __name__ == "__main__":
  print("main")
  print(sys.argv)
  FILE_NAME = "command1.txt"
  if sys.argv[1:]:
    FILE_NAME = sys.argv[1]

  COMMAND_FILE_PATH = f"./command_files/{FILE_NAME}"

  logging.basicConfig(filename=f'./log_files/{FILE_NAME}.log', level=logging.INFO, filemode="w")
  logging.info("Started Captain's Log on %s", datetime.datetime.now())

  mySat = SatelliteLink()

  mySat.get_commands_file(COMMAND_FILE_PATH)
  mySat.send_status().display()
  mySat.execute_commands()
  mySat.send_status().display()
  logging.info('Finished')
