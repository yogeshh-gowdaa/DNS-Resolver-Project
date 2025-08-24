import dns.resolver

def simple_dns_resolver(domain):
    result = dns.resolver.resolve(domain, 'A')
    for ipval in result:
        print(f'IP address for {domain} is {ipval.to_text()}')

domain_name = input("Enter a domain name: ")
simple_dns_resolver(domain_name)
