import requests


ctrlx_plc_endpoint="http://192.168.0.234:9002/plc/engineering/api/v2"
# ctrlx_plc_endpoint="http://localhost:9002/plc/engineering/api/v2/devices/Device/PLC%20Logic/Application/PLC_PRG"
# STEP 1: Get plc device information using get()
response=requests.get(url=ctrlx_plc_endpoint)

data = response.json()
print(data)
# output: {'name': 'PLC_PRG', 'elementType': 'POU', 'id': 'f8443dd0-a6c5-46f1-ba97-4978e9ab4696', 'children': [], 'elementProperties': {'build': {'excludeFromBuild': False, 'external': False, 'enableSystemCall': False, 'linkAlways': False, 'compilerDefines': ''}}, 'language': 'ST', 'declaration': 'PROGRAM PLC_PRG\nVAR\nEND_VAR', 'implementation': 'POU_ModbusTCP_FBD();\nPOU_Motion();\nPOU_NodeRED();\nPOU_PLC_First_Example();\nPOU_CytroPac();\nPOU_Hydraulic_LD();\nPOU_MQTT();', 'level': 'Standard'}



# folder_parameters = {
#   "name": "MyFolder",
#   "elementType": "Folder",
#   "elementProperties": {
#     "build": {
#       "excludeFromBuild": False,
#       "external": False,
#       "enableSystemCall": False,
#       "linkAlways": False,
#       "compilerDefines": ""
#     }
#   }
# }


# STEP 2: Add a GVL to your Application using post()
# hint: gvl is defined as dictionaries. this corresponds to the JSON format.  
# add_gvl_parameters = {
#   "name": "GVL_Python",
#   "elementType": "GVL",
#   "elementProperties": {
#     "build": {
#       "excludeFromBuild": False,
#       "external": False,
#       "enableSystemCall": False,
#       "linkAlways": False,
#       "compilerDefines": ""
#     }
#   },
#   "declaration": "{attribute 'symbol' := 'readwrite'}\nVAR_GLOBAL\nEND_VAR"
# }
# response=requests.post(url=ctrlx_plc_endpoint, json=folder_parameters)


# STEP 3: Defines a variable in the GVL

# define_variable = {
#   "name": "GVL_PLC_First_Example",
#   "elementType": "GVL",
#   "elementProperties": {
#     "build": {
#       "excludeFromBuild": False,
#       "external": False,
#       "enableSystemCall": False,
#       "linkAlways": False,
#       "compilerDefines": ""
#     }
#   },
#   "declaration": "{attribute 'symbol' := 'readwrite'}\nVAR_GLOBAL\n AM_FROM_Python: BOOL := FALSE ; \n END_VAR"
# }

# response=requests.put(url=ctrlx_plc_endpoint, json=define_variable)