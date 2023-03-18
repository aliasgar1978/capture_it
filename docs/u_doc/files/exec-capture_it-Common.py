
from capture_it import capture
from nettoolkit import *
from pathlib import *
import sys

p = Path(".")
previous_path = p.resolve().parents[0]
sys.path.insert(len(sys.path), str(previous_path))
capture_folder = str(previous_path.joinpath('captures'))
commands_folder = str(previous_path.joinpath('commands'))

"""
==============
TREE STRUCTURE
==============

Parent
|
| - + myPrograms
|   | - exec-capture_it-Common.py
|   | - cred.py ( contains login username (un), password (pw) )
|
| - + captures
|   | - [ output files ]  
|
| - + commands
    | - devices.txt (list of device ip addresses)
    | - cisco_cmds_txtfsm.txt (LIST OF CISCO COMMANDS TO BE CAPTURED)
    | - juniper_cmds_txtfsm.txt (LIST OF JUNIPER COMMANDS TO BE CAPTURED)


"""


# --------------------------------------------
# ------ USAGE OF Capture tool (config)  ...
# --------------------------------------------
#
from cred import un, pw
# un = get_username()   ## alternative
# pw = get_password()
#
auth = {
    'un':un ,
    'pw':pw ,
    'en':pw , 
}


# #------------------------------------------------
# List of devices

with open(f"{commands_folder}/devices.txt", 'r') as f:         #### LIST OF DEVICES IP ADDRESESSES
  lns = f.readlines() 
devices = [ _.strip() for _ in lns]

# #------------------------------------------------
# Commands 

cisco_cmds = f"{commands_folder}/cisco_cmds_txtfsm.txt"       #### LIST OF CISCO COMMANDS TO BE CAPTURED.
with open(cisco_cmds, 'r') as f:
  lns = f.readlines() 
CISCO_IOS_CMDS = [ _.strip() for _ in lns]

# #------------------------------------------------
# Commands 

juniper_cmds = f'{commands_folder}/juniper_cmds_txtfsm.txt'   #### LIST OF JUNIPER COMMANDS TO BE CAPTURED.
with open(juniper_cmds, 'r') as f:
  lns = f.readlines() 
JUNIPER_JUNOS_CMDS = [ _.strip() for _ in lns]
# #------------------------------------------------


# ---- DEFINE COMMANDS LISTS PER DEVICE TYPES ----
cmds = {
  'cisco_ios'  : CISCO_IOS_CMDS,
  'juniper_junos': JUNIPER_JUNOS_CMDS,
  'arista_eos': CISCO_IOS_CMDS,
}
# ---- START CAPTURE ----
capture(
  devices, 
  auth, 
  cmds, 
  path=capture_folder, 
  cumulative=True,        # optional arg
  forced_login=True,      # optional arg 
  parsed_output=True,     # optional arg (def: False )
  concurrent_connections=100,    # optional arg (def: 100)
)

# # #------------------------------------------------

print("Capture Task(s) Complete..")
# # #------------------------------------------------


