# pip install dnspython
import dns.resolver

def get_subdomains(domain, file_name, search ='l', method="A"):
    """you shode insert url without protocol \n
    method : A==justSubDomains, B==subDomains+ips
    """
    max = 0
    subdomains = []
    subdomains_and_ips = []
    with open(file_name) as file:     
        if search  == 'l':
            max = 100
        elif search  == 'm':
            max = 5000
        elif search  == 'h':
            max == 20000
        else:
            max == 100
            
        for item in file:
            if max <= 0:
                break
            subdomain = item.strip()
            try:
                answers = dns.resolver.resolve(subdomain + "." + domain, "A")
                for ip in answers:
                    subdomains_and_ips.append(subdomain + "." + domain + " - " + str(ip))
                    subdomains.append(subdomain + "." + domain)
            except:
                pass
            max -= 1
            
    if method == "A":
        subdomains = list(set(subdomains))
        return subdomains
    elif method == "B":
        return subdomains_and_ips


