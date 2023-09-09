import os
def scan():
	count = 0
	with open("http_proxies.txt","r") as f:
		servers = f.readlines()
	os.system("sudo echo \"HELLO, n0ct3m\"")
	for server in servers:
		if count !=475:
			count+=1
			continue
		cmd = "sudo nmap -p0-100 {IP} >> results.txt".format(IP=server.split(":")[0])
		os.system(cmd)
		os.system('echo "_______________________________________________" >> results.txt ')
		print("{IP} has been scanned!".format(IP=server.strip()))

def seek(num):
	count = 0
	with open("http_proxies.txt","r") as f:
		servers = f.readlines()
	for server in servers:
		null = server
		count+=1
		if count == num:
			print(server)

scan()