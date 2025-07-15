#ASYNCHRONOUS REQUEST

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
    	"source_id, "
        "designation, "
        "ra, "
        "dec, "
        "parallax, "
        "parallax_error, "
        "pm, "
        "pmra, "
        "pmdec, "
        "ruwe, "
        "phot_variable_flag, "
        "non_single_star, "
        "phot_g_mean_mag, "
        "phot_bp_mean_mag, "
        "phot_rp_mean_mag, "
        "bp_rp, "
        "bp_g, "
        "g_rp, "
        "teff_gspphot, "
        "teff_gspphot_lower, "
        "teff_gspphot_upper, " 
        "logg_gspphot, "
        "logg_gspphot_lower, "
        "logg_gspphot_upper, "
        "mh_gspphot, "
        "mh_gspphot_lower, "
        "mh_gspphot_upper, "
        "distance_gspphot, "
        "distance_gspphot_lower, "
        "distance_gspphot_upper, "
        "azero_gspphot, "
        "azero_gspphot_lower, "
        "azero_gspphot_upper, "
        "radial_velocity, "
        "radial_velocity_error "
        "FROM gaiadr3.gaia_source "
        "WHERE "
        "( "
        "parallax + 3 * parallax_error >= 50.0000 "
        ") "
        "or "
        "( "
        "designation = 'gaia DR3 6192187979961725952' or "
        "designation = 'gaia DR3 1166216253750406144' or "
        "designation = 'gaia DR3 4345775217221821312' or "
        "designation = 'gaia DR3 5943191236735787520' or "
        "designation = 'gaia DR3 4584639307993378432' "
		")")

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
outputFileName = "/home/lh/Documents/Biostar_Catalogue/Biostar_Catalogue/code/database/input_files/gaia.csv"
outputFile = open(outputFileName, "w")
outputFile.write(data)
outputFile.close()
connection.close()
print ("Data saved in: " + outputFileName)