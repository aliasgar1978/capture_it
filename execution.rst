

Execution Steps
=================================================



Execution Steps - High Level
----------------------------------------------

	#. Import project module
	#. Provide auth para
	#. List eligible devices
	#. List commands to be captured
	#. provide output path
	#. execute

Execution Steps - Detailed
----------------------------------------------

	#. Import the necessary module::

		from capture_it import capture

	#. Authentication Parameters::

		auth = {
			'un':'provide username' , 
			'pw':'provide login password', 
			'en':'provide enable password'  }

	#. List of devices::

		devices = [
			'192.168.1.1',
			'10.10.10.1',
			# ... list down all ip addresses for which output to be captured  ]

	#. Output path::

		op_path = './captures/'

	#. Commands to be captured::

		CISCO_IOS_CMDS = 	[
			'sh run', 
			'sh int status', 
			'sh lldp nei',
			# .. edit as need  ]
		JUNIPER_JUNOS_CMDS = [
			# 'show configuration | no-more',
			'show lldp neighbors | no-more',
			'show interfaces descriptions | no-more',
			# .. edit as need ]
		cmds = {
			'cisco_ios'  : CISCO_IOS_CMDS,
			'juniper_junos': JUNIPER_JUNOS_CMDS, }

	#. Start Capturing::

		capture(devices, auth, cmds, op_path, cumulative='Both', forced_login=True)

	Parameters:

		devices = list of ip addresses
		auth = authentication Parameters
		cmds = dictionary of list of commands to be captred (cisco, juniper, arista).
		op_path = output path ( use "." for storing in same relative folder )
		cumulative = (Options: True, False, 'Both') defines how to store each command output. True=Save all output in a single file. False=Save all command output in individual file. 'Both'=will generate both kinds of output.
		forced_login=(Options: True, False) (Default: False)  Forced login to device even if device ping doesn't succeded.

-----------------------

Watch out for the terminal if any errors and see your output in given output path.