# Example 1 Get Device from Python
import requests

#The base URL that you can find in the API Reference
CTRLX_URL_Basic="http://localhost:9002/plc/engineering/api/v2"

#Send devices
r=requests.get(CTRLX_URL_Basic+"%s"%("/devices"))

#Get Status Code
print("Status Code=%s"%(r.status_code))

#Get json Data
data=r.json()

#Output
print("—-Data—-")
for k,v in data.items():
    print("key:%s , value:%s"%(k,v))

# Output:
# Status Code=200
# —-Data—-
# key:name , value:Devices root node
# key:elementType , value:DevicesTopLevel
# key:id , value:None
# key:children , value:['Device']


# Example 2 Create Folder
import requests

#The base URL that you can find in the API Reference
CTRLX_URL_Basic="http://localhost:9002/plc/engineering/api/v2"

#Post Content
postData = "
{
    "name": "%s",
    "elementType": "Folder",
    "elementProperties": {
        "build": {
            "excludeFromBuild": False,
            "external": False,
            "enableSystemCall": False,
            "linkAlways": False,
            "compilerDefines": ""
            },
            "documentation": "Folder Documentation @123"
            }
}
"%("FolderFromAPI")

#Send devices
r=requests.post(CTRLX_URL_Basic+"%s"%("/devices"),data=postData)

#Get Status Code
print("Status Code=%s"%(r.status_code))

#Get json Data
data=r.json()

#Output
print("—-Data—-")
for k,v in data.items():
    print("key:%s , value:%s"%(k,v))