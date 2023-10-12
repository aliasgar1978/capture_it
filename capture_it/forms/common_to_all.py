
import PySimpleGUI as sg
from nettoolkit.forms.formitems import *
from capture_it import capture, quick_display, LogSummary


def cit_common_exec(i):
	devices = i['device_ips']
	devices = [d.split() for d in devices]
	auth = {'un': i['cred_un'] ,'pw': i['cred_pw'], 'en': i['cred_en']}
	cmds = {
		'cisco_ios': i['cisco_cmds'].split("\n"),
		'juniper_junos': i['juniper_cmds'].split("\n"),
	}
	path = i['op_folder']
	if i['cred_cumulative'] == 'cumulative':
		cumulative = True
	elif i['cred_cumulative'] == 'non-cumulative':
		cumulative = False
	else:
		cumulative = i['cred_cumulative']
	forced_login = i['forced_login']
	parsed_output = i['parsed_output']
	visual_progress = i['visual_progress']
	concurrent_connections = i['concurrent_connections'] if i['concurrent_connections'].isnumeric() else 100
	log_print = i['print']
	append_to = f"{path}/{i['append_to']}"


	c = capture(
		devices,
		auth,
		cmds,
		path=path,
		cumulative=cumulative, 
		forced_login=forced_login,
		parsed_output=parsed_output,
		visual_progress=visual_progress,
		concurrent_connections=concurrent_connections,
		# CustomClass=CiscoBgp,
	)
	LogSummary(c, 
		print=log_print, 
		append_to=append_to, 
	)
	print("Capture Task(s) Complete..")



def device_ip_list_file_exec(obj, i):
	"""executor function

	Args:
		obj (object): frame object 
		i (itemobject): item object of frame

	Returns:
		bool: wheter executor success or not.
	"""	
	try:
		if i['device_ip_list_file'] != '':
			obj.event_update_element(device_ips={'value': "calculating..."})
			with open(i['device_ip_list_file'], 'r') as f:
				lns = f.readlines()
			lns = ''.join(lns)
			obj.event_update_element(device_ips={'value': lns})
			return True
	except:
		return None

def cisco_cmd_list_file_exec(obj, i):
	"""executor function

	Args:
		obj (object): frame object 
		i (itemobject): item object of frame

	Returns:
		bool: wheter executor success or not.
	"""	
	try:
		if i['cisco_cmd_list_file'] != '':
			obj.event_update_element(cisco_cmds={'value': "calculating..."})
			with open(i['cisco_cmd_list_file'], 'r') as f:
				lns = f.readlines()
			lns = ''.join(lns)
			obj.event_update_element(cisco_cmds={'value': lns})
			return True
	except:
		return None

def juniper_cmd_list_file_exec(obj, i):
	"""executor function

	Args:
		obj (object): frame object 
		i (itemobject): item object of frame

	Returns:
		bool: wheter executor success or not.
	"""	
	try:
		if i['juniper_cmd_list_file'] != '':
			obj.event_update_element(juniper_cmds={'value': "calculating..."})
			with open(i['juniper_cmd_list_file'], 'r') as f:
				lns = f.readlines()
			lns = ''.join(lns)
			obj.event_update_element(juniper_cmds={'value': lns})
			return True
	except:
		return None





def exec_common_to_all_frame():
	"""tab display - Credential inputs

	Returns:
		sg.Frame: Frame with filter selection components
	"""    		
	return sg.Frame(title=None, 
					relief=sg.RELIEF_SUNKEN, 
					layout=[

		[sg.Text('Same commands Output for All', font='Bold', text_color="black") ],


		[sg.Text('List of device IPs:', text_color="yellow"),
		sg.Multiline("", key='device_ips', autoscroll=True, size=(15,5), disabled=False),
		],
		[sg.Text('Device IPs list-file:', text_color="yellow"), 
			sg.InputText('', key='device_ip_list_file', change_submits=True,),
			sg.FileBrowse(),
		],
		under_line(80),

		[sg.Text('List of cisco show commands:', text_color="yellow"),
		sg.Multiline("", key='cisco_cmds', autoscroll=True, size=(50,5), disabled=False),
		],
		[sg.Text('Cisco commands list-file:', text_color="yellow"), 
			sg.InputText('', key='cisco_cmd_list_file', change_submits=True,),
			sg.FileBrowse(),
		],
		under_line(80),

		[sg.Text('List of juniper show commands:', text_color="yellow"),
		sg.Multiline("", key='juniper_cmds', autoscroll=True, size=(50,5), disabled=False),
		],
		[sg.Text('Juniper commands list-file:', text_color="yellow"), 
			sg.InputText('', key='juniper_cmd_list_file', change_submits=True,),
			sg.FileBrowse(),
		],
		under_line(80),

		[sg.Button("Capture-it", change_submits=True, key='cit_common')],

		])
