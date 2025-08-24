import socket
from dnslib import DNSRecord, RR, QTYPE, A

LISTEN_IP = "0.0.0.0"
LISTEN_PORT = 53

FAKE_IP = "192.168.1.100"

sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
sock.bind((LISTEN_IP, LISTEN_PORT))

print(f"DNS Server running at {LISTEN_IP}:{LISTEN_PORT}")

while True:
    data, addr = sock.recvfrom(512)
    request = DNSRecord.parse(data)
    print(f"Received query for: {request.q.qname}")

    reply = request.reply()
    reply.add_answer(RR(request.q.qname, QTYPE.A, rdata=A(FAKE_IP), ttl=60))

    sock.sendto(reply.pack(), addr)
    print(f"Replied with IP: {FAKE_IP} to {addr}")
