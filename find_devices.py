import os
import subprocess
import re

urlRegex = "([\w_-]+(?:(?:\.[\w_-]+)+))([\w.,@?^=%&:\/~+#-]*[\w@?^=%&\/~+#-])"
ip = "10.59.209"

a = []

for i in range(0, 256):
    newIP = f"{ip}.{i}"
    #cmd = f"nslookup {newIP}"
    
    proc = subprocess.Popen(["nslookup", newIP], stdout=subprocess.PIPE, shell=False)
    (result, err) = proc.communicate()
    #print("program output:", result, err)
    result = str(result)

    if "Name:" in result: pass
    else: continue

    computerName = result.split("Name:    ")[1].split("\\r\\n")[0]
    
    #print(result)
    #a.append(computerServer)
    a.append(computerName)

print(a, len(a))