#With python installed open powershell or cmd and execute before first use:
#pip install openpyxl paramiko pandas pathlib

#check if dependencies os, ast, json are being used
import paramiko
from pathlib import Path
import pandas as pd
import os, sys
import ast, json

paramiko.util.log_to_file("paramiko.log")

# Open a transport
host,port = "192.168.0.102",22
try:
    print("Trying connection")
    transport = paramiko.Transport((host,port))
    print("Connected")
except:
    print("Kan geen verbinding maken, ben je in de GR en verbonden met JvB 73 GR (niet 5G)?")
    sys.exit()
    
# Auth    
username,password = "pi","raspberry"
try:
    transport.connect(None,username,password)
    print("Ingelogd")
except:
    print("Access denied, check je inloggegevens")


# Go!    
sftp = paramiko.SFTPClient.from_transport(transport)

# Download
filepath = "/home/pi/Turfsysteem/lijst.txt"
localDir = Path(os.getcwd())
localpath = localDir / "lijst.txt"
print (localpath)
try:
    sftp.get(filepath,localpath)
    print("Turflijst opgehaald")
except:
    print("Kan de turflijst ff niet vinden, bel de helpdesk of probeer het nog eens")
    sys.exit()

# Upload, doen we niet
#filepath = "/home/Turfsysteem/foo"
#localpath = os.getcwd() + "/bar"
#sftp.put(localpath,filepath)

# Close
if sftp: sftp.close()
if transport: transport.close()

#translate to excel
excelpath = localDir / "lijst.xlsx"
print (excelpath)
df = pd.read_json(localpath)
print("file read")
try:
    df.to_excel(excelpath)
    print("Excel bestand aangemaakt")
except:
    print("Kan excel bestand niet aanmaken. Als het lijst.xlsx bestand geopend is, sluit deze en probeer het nog eens")
    sys.exit()
    
print("Zo dat was makkelijk he? Waar zouden we zijn zonder Job")

