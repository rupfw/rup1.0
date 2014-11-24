

from socket import *
import os.path
import json
import sys

serverIP = '127.0.0.1'
blksz = 1024 #Bulk size for receiving file in chunks
filePathDict = {} #Dictionary for path, size pairs


if len(sys.argv) < 2:
	print 'Server Port No. missing in command line arguments'
	serverPort = raw_input('Enter Server Port No.: ')
else:
	serverPort = sys.argv[1]

serverPort= int (serverPort)

#Creating server socket for control connection
serverSocket = socket(AF_INET,SOCK_STREAM) 
serverSocket.bind((serverIP,serverPort)) 
serverSocket.listen(10)

print 'FTP Server Started successfully.\n' 

def SendFile (filename,ClientIP, DataConPort):
	try:
		file = open(filename, 'rb')
		while True:
			bytes = file.read(blksz) # read/send 1K at a time
			if not bytes: break # until file totally sent
			sent = connectionSocket.send(bytes)
			assert sent == len(bytes)
	except:
		print('Error downloading file on server:', filename)

while 1:
	print 'The server is Waiting for a connection.'
	filePathDict.clear()
	try:
		connectionSocket, addr = serverSocket.accept() 
		clientIP = addr[0] 
		filename = connectionSocket.recv(1024) 
		
		connectionSocket.send("500") #500: Syntax error; unrecognized command
		connectionSocket.close()
		
	except:
		print 'Error: Connection lost.'
		connectionSocket.close()
	
