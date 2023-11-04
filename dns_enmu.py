import dns.resolver

print("Enter the IP address or domain name you want DNS information for:")
target_domain = input()

search_types = ["A", "SOA", "NS", "MX", "ptr"]

resolver = dns.resolver.Resolver()

for search_type in search_types:
    try:
        answers = resolver.query(target_domain, search_type)
    except dns.resolver.NoAnswer:
        continue

    print(f"{search_type} record for {target_domain}:")
    
    for rdata in answers:
        print(f"{rdata}")

        