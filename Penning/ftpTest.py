import paramiko
import os

paramiko.util.log_to_file("paramiko.log")

# Open a transport
host,port = "192.168.0.102",22
transport = paramiko.Transport((host,port))

# Auth    
username,password = "pi","raspberry"
transport.connect(None,username,password)

# Go!    
sftp = paramiko.SFTPClient.from_transport(transport)

# Download
filepath = "/home/pi/Turfsysteem/lijst.txt"
localDir = os.getcwd()
localpath = localDir + "\lijst.txt"
print (localpath)
sftp.get(filepath,localpath)

# Upload
#filepath = "/home/Turfsysteem/foo"
#localpath = os.getcwd() + "/bar"
#sftp.put(localpath,filepath)

# Close
if sftp: sftp.close()
if transport: transport.close()
