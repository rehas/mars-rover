'''
Satellite module
'''
class Satellite():
  '''class to handle communications between earth and mars,
  orbiting around mars to oversee rovers
  '''
  def __init__(self, command_file):
    print("This initializes a satellite class")
    self.commandfile = command_file if self.is_valid_command_file(command_file) else None
    pass
  
  def is_valid_command_file(self, file):
    commands = open(file, "r")
    for c_line in commands.readlines():
      print(c_line.strip())
  
  def get_commands(self):
    pass
  def send_results(self):
    pass
  
