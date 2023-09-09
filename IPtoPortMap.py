# This program maps IPs to the ports open on them

with open("results.txt",'r') as f:
    lines = f.readlines()
count = 0
mapping = {}
for line in lines:
    
    if "Nmap scan report for" in line:
        target = count
        ports = []
        while("_____" not in lines[target]):
            if "/" in lines[target] and "open" in lines[target]:
                ports.append(lines[target].split()[2])
            target+=1
        if "(" in line:
            mapping[line.split("(")[1].strip(")\n")] = ports
print(mapping)
print(count)

    
