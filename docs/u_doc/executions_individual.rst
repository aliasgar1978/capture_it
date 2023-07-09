

Execution Steps - Separate Commands for each individual devices
==================================================================



Execution Steps - summary (individual)
----------------------------------------------

	#. Import project module
	#. Define Inputs
		* Authentication parameters
		* Dictionary of all eligible {devices : [list of commands to captures]}
		* Output path 
	#. execute
	#. write/print capture log summary (optional)

Execution Steps - Explained (individual)
----------------------------------------------

	#. Import the necessary module::

		from capture_it import capture_individual, LogSummary


	#. Authentication Parameters::

		# Provide Authentication Parameters in a dictionary as below.
		auth = {
			'un':'provide username' , 
			'pw':'provide login password', 
			'en':'provide enable password'  
		}
		## Make sure to use static passwords. Refrain using OTP, as ID may get locked due to multiple simultaneous login.


	#. Dictionary of all eligible devices v/s commands::

		# Option 1:  Provide the dictionary of devices v/s commands as sample given below.

		devices = {
			'10.10.10.1': [show_cmd_1, show_cmd_2, ..],
			'10.10.10.2': [show_cmd_3, show_cmd_4, ..], 
			('10.10.10.3', '10.10.10.4', '10.10.10.1'): [show_cmd_5, show_cmd_6, ..],
		}


	.. Tip::

		#. Multiple devices can be inserted as a tuple for dictionary keys.
		#. One device can appear on multiple keys ( as stated in above example: 10.10.10.1).  List of commands from both  entries will be clubbed together to form a single list.
		#. Grouping
			#. Create a separate group of commands based on device functionality (example: separate set of commands for each - access layers, core layers ). 
			#. Create group of devices as a tuple based on device functionality.  
			#. Using these above two - create a simple readable dictionary. 



	#. Output path::

		op_path = './captures/'


	#. Start Capturing::

		c = capture_individual(
			## mandatory arguments ##
			auth,           ## Authentication parameters (dict)
			devices,        ## Dictionary of devices of list of commands ( see above sample )
			op_path,        ## output path - to store the outputs. (optional, default =".")

			## optional arguments ##
			cumulative=True,        ## True/False/Both/None (store output in a single file, individual command file, both, No file)
			forced_login=False,     ## True/False (True: try to ssh/login device even if ping responce fails. )
			parsed_output=False,    ## True/False (True: Evaluate and parse the command outputs to store device data in excel)
			visual_progress=10,     ## display visual progress on console (default level: 3)
			log_type='individual',  ## available options = ('common', individual', 'both', None) ( default: None)
			common_log_file='common-debug.log',  ## provide if log_type is individual (default: None)
			concurrent_connections=100,    ## numeric value (default:100), number of simultaneous device connections in a group. 
		)
		LS = LogSummary(c, print=True, write_to=f'cmds_log_summary.log')  # optional - raw commands log summary


	.. important::
		**Parameters for capture_individual**
			
			* ``auth``  authentication Parameters
			* ``devices``  dictionary of devices of list of commands to be captred for each individual device.  **Note since we are providing commands exclusively for each individual/set of device(s), Script will not auto check for device type.**
			* ``op_path``  output path ( use "." for storing in same relative folder )
			* ``cumulative``  (Options: True, False, 'Both', None) defines how to store each command output. True=Save all output in a single file. False=Save all command output in individual file. 'Both'=will generate both kinds of output. None=will not save text log outout to any file, but display it on screen
			* ``forced_login``  (Options: True, False) (Default: False)  Forced login to device even if device ping doesn't succeded.
			* ``parsed_output``  (Options: True, False) (Default: False) Parse the command output and generates device database in excel file.  Each command output try to generate a pased detail tab.
			* ``visual_progress`` (int, optional): 0 will show least progress, 10 will show all progress (default=3).
			* ``log_type`` (str): what type of log output requires. choices are = common, individual, both
			* ``common_log_file`` (str): output file name of a common log file
			* ``concurrent_connections``  (numeric) (Default: 100), change the number of simultaneous device connections as per link connection and your pc cpu processng performance. 

		**Parameters for LogSummary**
			* ``c`` (capture_individual): capture_individual object instance
			* ``print`` (bool): displays result summary on screen. Defaults to False.
			* ``write_to`` (str): filename, writes result summary to file. Defaults to None (i.e. no file write out).



	.. important::
		
			Since we are providing individual commands for each device, pay attention on device type  ``Cisco/Juniper/Arista`` and apply respective commands to the system appropriatly.



A Sample Execution File
----------------------------------------------


:download:`Sample Execution File - Individual <files/exec-capture_it-Individual.py>`. A sample execution file will look similar to this


Folder Tree Structure
----------------------------------------------

	#. Either maintain the tree structure as mentioned in file or modify the code as per your requirement::

		Parent
		|
		| - + myPrograms
		|   | - exec-capture_it - Individual.py
		|   | - cred.py ( contains login username (un), password (pw) )
		|
		| - + captures
		|   | - [ output files ]	
		|
		| - + commands
		    | - devices_cmds.xlsx




-----------------------

Watch out for the terminal if any errors and see your output in given output path.
