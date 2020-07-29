port1 = {21 : "FTP" , 22 : "SSH" , 23 : "telenet" , 80 : "http"}

port2 = {value : key
         for key,value in port1.items()}

print(port2)
