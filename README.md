# DNS-Resolver-Project
A simple DNS Resolver and DNS Server implementation in Python to find IP Adress. This project demonstrates how DNS queries and responses work using socket programming.
step 1: Clone the project: " "

step2: Go to the project folder:
Open PowerShell and move into your project directory:cd"your cloned repo folder"

step3: Install dependencies
Run this once: pip install -r requirements.txt

step4:Open Split Terminal
You need two terminals (side by side or two PowerShell tabs).
Left side → DNS Server (Receiver)
Right side → DNS Resolver (Sender / Client)

 step5:Start the DNS Server (Receiver)
In the left terminal, run: python dns_server.py
Output: DNS Server running at 0.0.0.0:53(port may vary)
This means your server is waiting for queries on port 53 (default DNS port).

step6: Run the DNS Resolver (Client / Sender)
In the right terminal, run: python dns_resolver.py
It will ask: Enter a domain name:
Type any domain, e.g.:google.com/facebook.com any website
IP address for google.com is 142.251.42.238

Repeat Queries
Every time you want to test a new domain, just run the client again: python dns_resolver.py
When asked: Enter a domain name:
you can type:facebook.com or any other

Don’t type facebook.com directly in PowerShell → it must be entered inside the program prompt, not as a command.


Left terminal (server):
(<img width="1455" height="482" alt="image" src="https://github.com/user-attachments/assets/3e0a5b97-586d-4462-a229-0a02d7dd057c" />
)

Right terminal (client):
<img width="1446" height="313" alt="image" src="https://github.com/user-attachments/assets/8603459e-358e-4d19-aa0a-5defcedb782b" />


