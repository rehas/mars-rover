# mars-rover
A mars rover command flow simulation

## Dependencies
- [Python3.7](https://www.python.org/downloads/release/python-370/)

## Getting started

### MacOs

- Clone repo
- On root folder run `python3 app.py` for default commandset.
- For a different set of commands add commands file (.txt format) to command_files folder
- Run `python app.py <new_command_file_name.txt>`

### Windows
- Clone repo
- On root folder run `<your_python3_folder/python.exe> app.py` for default commandset.
- For a different set of commands add commands file (.txt format) to command_files folder
- Run `python app.py <new_command_file_name.txt>`

### Tests
- `python3 -m unittest tests.tests -v`

### Captain's Logs
- For every command file, there will be a logfile generated
- These logs should reside under log_files

#

## Explanation

	                                               XXXXXXXXXXXXXXXX
	                                            XXX                XXXX
	                      +-----------+        XX                      XX
	                      | Satellite |       XX                         XX
	                      +--+----+---+      XX                           XX
	                         |    |         XX                      +----+ XX
	                         |    |        XX                       |    |  XX
	+------------+           |    |        XX                       |    |   XX
	|  Houston   |           |    |        XX            Mars       |Rov2|    X 
	+------------+           |    |        XX                       |    |    X
	                       +-+----+--+     XX                       |    |   X
	                       |         |     XX    +------------+     +----+  X
	                       +---------+      XX   | Rover1     |           XX
	                                        XX   +------------+          XX
	                                          XXXX                   XXX
	                                             XXXXXX          XXXXX
	                                                  XXXXXXXXXXX


### FLOW

- We want to send rovers to mars and we want to communicate our movement orders to the rovers
- We will send our commands in files containing 
	- Grid Size info -> 5 6 -> 5 width 6 length : Sent 1 per command batch
	- CommandsPerRover
		- Initial position of the rover on the grid -> 1 2 N : Rover is on location (x,y) 1,2 and facing North
			- This information is verified by another department so we will assume it is correct
			- (0,0) means the cell at top left corner
			- (3,4) means 4th row, 3rd column (with 0 based index)
		- Action commands -> LML -> turn Left - Move - turn Left 
			- Move means move 1 square on the grid towards the direction currently faced. 
			- Left / Right means -> counter clockwise and clockwise respectively when you're looking at the compass.
- In return we want:
	- The updated status of the grid
	- Whether or not our commands got executed as is
		- If not, a response with a reason
- We want our rovers to be aware of:
	- The edges on the grid
		- To prevent falling over the edge even if the command recieved directs
	- The other rovers on the grid
		- To prevent crashing other rovers on the same grid (even if the command recieved directs)

### ASSUMPTIONS:
	- We assume that our rovers operate far from the polar areas
		- Hence the grids are flat
		- So parallel moving rovers don't crash into each other
	- We assume that with each batch of commands there is only 1 command per rover
	- The order of the commands are executed in sequence 
		- If there's a possibility of of crash or fall over
			- That specific command does not get executed and will be skipped (with a response)
	- We assume that every batch of commands is independent from the previous or future commands
		- That the state of the grid between batches are independent
			- That there could be more or less rovers
			- The locations of the rovers could be different than previous batch
	- We assume that the rovers cover 1 square size on grid completely filling it
