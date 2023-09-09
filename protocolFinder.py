#This program returns the IPs having a particular port open
protocol = input("[+] Enter the required protocol:")

with open("results.txt") as f:
    lines = f.readlines()
count = 0
IP = dict()
for line in lines:
    if "Nmap scan report for" in line:
        if '(' in line:
            IP[count] = line.split("(")[1].strip(')\n')
        else:
            IP[count] = line.split("for")[1].strip()
    count+=1
count = 0
print(f"The following IPs have {protocol} open:")
for line in lines:
    if "open" in line and protocol in line:
        target = count
        while(1):
            if(target in IP.keys()):
                print(IP[target])
                break   
            target-=1
    count+=1

    