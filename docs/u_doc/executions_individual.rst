

Execution Steps - Separate Commands for each individual devices
==================================================================



Execution Steps - summary
----------------------------------------------

	#. Import project module
	#. Define Inputs
		* Authentication parameters
		* Dictionary of all eligible {devices : [list of commands to captures]}
		* Output path 
	#. execute

Execution Steps - Explained
----------------------------------------------

	#. Import the necessary module::

		from capture_it import capture_individual


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

		capture_individual(
			auth,           ## Authentication parameters (dict)
			devices,        ## Dictionary of devices of list of commands ( see above sample )
			op_path,        ## output path - to store the outputs. (optional, default =".")
			cumulative=True,        ## True/False/Both (store output in a single file, individual command file, both)
			forced_login=False,     ## True/False (True: try to ssh/login device even if ping responce fails. )
			parsed_output=False,    ## True/False (True: Evaluate and parse the command outputs to store device data in excel)
			concurrent_connections=100,    ## numeric value (default:100), number of simultaneous device connections in a group. 
		)

.. important::
	
	``Parameters``

	* *auth* = authentication Parameters
	* *devices* = dictionary of devices of list of commands to be captred for each individual device.  **Note since we are providing commands exclusively for each individual/set of device(s), Script will not auto check for device type.**
	* *op_path* = output path ( use "." for storing in same relative folder )
	* *cumulative* = (Options: True, False, 'Both') defines how to store each command output. True=Save all output in a single file. False=Save all command output in individual file. 'Both'=will generate both kinds of output.
	* *forced_login* = (Options: True, False) (Default: False)  Forced login to device even if device ping doesn't succeded.
	* *parsed_output* = (Options: True, False) (Default: False) Parse the command output and generates device database in excel file.  Each command output try to generate a pased detail tab.
	* *concurrent_connections* = (numeric) (Default: 100), change the number of simultaneous device connections as per link connection and your pc cpu processng performance. 

-----------------------

Watch out for the terminal if any errors and see your output in given output path.
