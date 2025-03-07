#ASYNCHRONOUS REQUEST

#Python 2
#import httplib
#import urllib

#Python 3
import http.client as httplib
import urllib.parse as urllib
import time
from xml.dom.minidom import parseString

host = "gea.esac.esa.int"
port = 443
pathinfo = "/tap-server/tap/async"


#-------------------------------------
#Create job
query = ("SELECT "
    	"hip, "
        "hd, "
        "bd, "
        "cod, "
        "cpd, "
        "vmag, "
        "ra, "
        "de, "
        "rahms, "
        "dedms, "
        "plx, "
        "e_plx, "
        "pmra, "
        "pmde, "
        "btmag, "
        "e_btmag, "
        "vtmag, "
        "e_vtmag, "
        "b_v, "
        "e_b_v, " 
        "sptype, "
        "r_sptype "
        "FROM public.hipparcos "
		"ORDER BY hip")

params = urllib.urlencode({\
	"REQUEST": "doQuery", \
	"LANG":    "ADQL", \
	"FORMAT":  "csv", \
	"PHASE":  "RUN", \
	"JOBNAME":  "Any name (optional)", \
	"JOBDESCRIPTION":  "Any description (optional)", \
	"QUERY":   query
	})

headers = {\
	"Content-type": "application/x-www-form-urlencoded", \
	"Accept":       "text/plain" \
	}

connection = httplib.HTTPSConnection(host, port)
connection.request("POST",pathinfo,params,headers)

#Status
response = connection.getresponse()
print ("Status: " +str(response.status), "Reason: " + str(response.reason))

#Server job location (URL)
location = response.getheader("location")
print ("Location: " + location)

#Jobid
jobid = location[location.rfind('/')+1:]
print ("Job id: " + jobid)

connection.close()

#-------------------------------------
#Check job status, wait until finished

while True:
	connection = httplib.HTTPSConnection(host, port)
	connection.request("GET",pathinfo+"/"+jobid)
	response = connection.getresponse()
	data = response.read()
	#XML response: parse it to obtain the current status
	#(you may use pathinfo/jobid/phase entry point to avoid XML parsing)
	dom = parseString(data)
	phaseElement = dom.getElementsByTagName('uws:phase')[0]
	phaseValueElement = phaseElement.firstChild
	phase = phaseValueElement.toxml()
	print ("Status: " + phase)
	#Check finished
	if phase == 'COMPLETED': break
	#wait and repeat
	time.sleep(0.2)

connection.close()

#-------------------------------------
#Get results
connection = httplib.HTTPSConnection(host, port)
connection.request("GET",pathinfo+"/"+jobid+"/results/result")
response = connection.getresponse()
data = response.read().decode('iso-8859-1')
#print(type(data))
#print(data)
outputFileName = "/home/lh/Desktop/Biostar_Catalogue/Biostar_Catalogue/code/database/input_files/public_hipparcos.csv"
outputFile = open(outputFileName, "w")
outputFile.write(data)
outputFile.close()
connection.close()
print ("Data saved in: " + outputFileName)