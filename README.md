# ProxyAnalysis
Just a little project to play with proxy servers

# Overview
The http_proxies file contains about 800 Proxy Servers sourced from the Internet. The goal is to scan these IPs and see what we can find out using passive enumeration **(Do not hack into systems that you don't own)**. For this purpose, scanner.py is used to scan the first 100 ports of each of the IP and store them. Then we can use IPtoPortMap.py to create a mapping between IP and the ports open on them, which can be easily used in further programs. Finally, protocolFinder.py can be used to search for a single open port across all the results. Have fun!

# Usage:
- Clone the repository
- Run scanner.py to get the resultant results.txt file
- Proceed as you like with the provided scripts or make your own and play around


