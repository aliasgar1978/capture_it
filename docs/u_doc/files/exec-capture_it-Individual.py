
from capture_it import capture_individual
from nettoolkit import *
from pathlib import *
from pprint import pprint
import sys

"""
==============
TREE STRUCTURE
==============

Parent
|
| - + myPrograms
|   |	- exec-capture_it - Individual.py
|   |	- cred.py ( contains login username (un), password (pw) )
|
| - + captures
|   | - [ output files ]	
|
| - + commands
    | - devices_cmds.xlsx

"""

p = Path(".")
previous_path = p.resolve().parents[0]
sys.path.insert(len(sys.path), str(previous_path))
capture_folder = str(previous_path.joinpath('captures'))
commands_folder = str(previous_path.joinpath('commands'))

# --------------------------------------------
# ------ USAGE OF Capture tool (config)  ... (enable only one option)
# --------------------------------------------

# option 1 -------------
from cred import un, pw

# option 2 -------------
# un = get_username()
# pw = get_password()

# authentication Dictionary -----------
auth = { 'un':un , 'pw':pw , 'en':pw }


# ------------------------------------------------
#          devices/commands dictionary
# ------------------------------------------------
#
df_dict = read_xl(f'{commands_folder}/devices_cmds.xlsx')        ### file with ips and commands.
#
devices_command_dict = {}
for sht, df in df_dict:
	df = df.fillna('')
	ips = tuple(df['ips'][df['ips'] != ''])
	commands = tuple(df['commands'][df['commands'] != ''])
	if not devices_command_dict.get(ips):
		devices_command_dict[ips] = []
	devices_command_dict[ips].extend(commands)

# ------------------------------------------------
#                  Start capture 
# ------------------------------------------------
capture_individual(
	auth, 
	devices_command_dict,
	op_path=capture_folder, 
	cumulative=True, 		      # optional arg
	forced_login=True, 		# optional arg 
	parsed_output=True,		# optional arg
	concurrent_connections=30	# optional arg
)
print("THE END..")

# ------------------------------------------------
