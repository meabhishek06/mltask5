import re 
file1 = open('/root/mltask5/ip.txt', 'r') 
count = 0

ipaddr = re.compile(r'^\d+.\d+.\d+.\d+') 
datetime = re.compile(r"\[([A-Za-z0-9+\:\/ ]+)\]") 
status = re.compile(r"\"([A-Za-z0-9+\:\/.:_; ]+)\"") 
ip = []


for line in file1: 
    count += 1
    ipaddress = ipaddr.findall(line)
    dt = datetime.findall(line)
    st = status.findall(line)
    if len(ipaddress) == 0:
        pass
    else:
        ipaddress.append(dt[0])
        ipaddress.append(st[0])
        ip.append(ipaddress)
        
file1.close() 

import pandas as pd    

df = pd.DataFrame(ip, columns=['IP', 'DATE', 'URL'])
csv_data = df.to_csv(index=False)
df.to_csv('/root/mltask5/ip.csv', index=False)
