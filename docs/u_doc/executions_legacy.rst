

Execution Steps - Common Commands for all devices
=================================================



Execution Steps - summary (common)
----------------------------------------------

	#. Import project module
	#. Define Inputs
		* Authentication parameters
		* List of all eligible devices
		* List of all commands to be captured (model wise)
		* Output path
	#. execute

Execution Steps - Explained (common)
----------------------------------------------

	#. Import the necessary module::

		from capture_it import capture


	#. Authentication Parameters::

		# Provide Authentication Parameters in a dictionary as below.
		auth = {
			'un':'provide username' , 
			'pw':'provide login password', 
			'en':'provide enable password'  
		}
		## Make sure to use static passwords. Refrain using OTP, as ID may get locked due to multiple simultaneous login.


	#. List of devices::

		# Option 1:  Provide the list of devices as below.
		devices = [
			'192.168.1.1',
			'10.10.10.1',
			# ... list down all ip addresses for which output to be captured  
		]

		# Option 2:  Store list of devices IP in a text file and get from that file.
		with open('devices.txt', 'r') as f:
			lns = f.readlines()
		devices = [_.strip() for _ in lns]


	#. Output path::

		op_path = './captures/'

	#. Commands to be captured::

		# Option 1:  Provide the list of Commands as below.
		CISCO_IOS_CMDS = 	[
			'sh run', 
			'sh int status', 
			'sh lldp nei',
			# .. edit as need  
		]
		JUNIPER_JUNOS_CMDS = [
			'show configuration | no-more',
			'show lldp neighbors | no-more',
			'show interfaces descriptions | no-more',
			# .. edit as need 
		]

		# Option 2:  Store list of commands in a text file and get from that file.
		with open('cisco_commands.txt', 'r') as f:
			lns = f.readlines()
		CISCO_IOS_CMDS = [_.strip() for _ in lns]
		with open('juniper_commands.txt', 'r') as f:
			lns = f.readlines()
		JUNIPER_JUNOS_CMDS = [_.strip() for _ in lns]

		# After commands lists available, add it to a dictionary as below..
		cmds = {
			'cisco_ios'  : CISCO_IOS_CMDS,
			'juniper_junos': JUNIPER_JUNOS_CMDS, 
		}


		Note: ``arista_eos`` key for the Arista switches commands list to be added to dictionary.



	#. Start Capturing::

		capture(
			## mandatory arguments ##
			devices,    ## list of device ips
			auth,       ## Authentication parameters (dict)
			cmds,       ## Dictionary of list of commands ( see above example )
			op_path,    ## output path - to store the outputs. 

			## optional arguments ##
			cumulative=True,        ## True/False/Both/None (store output in a single file, individual command file, both kinds of file, No file)
			forced_login=False,     ## True/False (True: try to ssh/login device even if ping responce fails. )
			parsed_output=False,    ## True/False (True: Evaluate and parse the command outputs to store device data in excel)
			visual_progress=10,     ## display visual progress on console (default level: 3)
			log_type='individual',  ## available options = ('common', individual', 'both', None) ( default: None)
			common_log_file='common-debug.log',  ## provide if log_type is individual (default: None)
			concurrent_connections=100,          ## numeric value (default:100), number of simultaneous device connections in a group. 
		)


	.. important::
		
		**Parameters**

		* ``devices``  list of ip addresses
		* ``auth``  authentication Parameters
		* ``cmds``  dictionary of list of commands to be captred (cisco, juniper, arista).
		* ``op_path``  output path ( use "." for storing in same relative folder )
		* ``cumulative``  (Options: True, False, 'Both', None) defines how to store each command output. True=Save all output in a single file. False=Save all command output in individual file. 'Both'=will generate both kinds of output.. None=will not save text log outout to any file, but display it on screen
		* ``forced_login``  (Options: True, False) (Default: False)  Forced login to device even if device ping doesn't succeded.
		* ``parsed_output``  (Options: True, False) (Default: False) Parse the command output and generates device database in excel file.  Each command output try to generate a pased detail tab.
		* ``visual_progress`` (int, optional): 0 will show least progress, 10 will show all progress (default=3).
		* ``log_type`` (str): what type of log output requires. choices are = common, individual, both
		* ``common_log_file`` (str): output file name of a common log file
		* ``concurrent_connections``  (numeric) (Default: 100), change the number of simultaneous device connections as per link connection and your pc cpu processng performance.


	.. important::
		
			Since we are providing all commands at a time for all devices, Script will automatically identifies whether device is ``Cisco/Juniper/Arista`` and push respective commands to the system without needing to mention explicitly.



A Sample Execution File
----------------------------------------------


:download:`Sample Execution File - Common <files/exec-capture_it-Common.py>`. A sample execution file will look similar to this

:download:`List of CISCO Commands <files/cisco_cmds_txtfsm.txt>`. A sample command list file for cisco.

:download:`List of JUNIPER Commands <files/juniper_cmds_txtfsm.txt>`. A sample command list file for juniper.


Folder Tree Structure
----------------------------------------------

	#. Either maintain the tree structure as mentioned in file or modify the code as per your requirement::

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


-----------------------

Watch out for the terminal if any errors and see your output in given output path.
