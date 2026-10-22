from collections import defaultdict
class Solution(object):
    def subdomainVisits(self, cpdomains):
        domains=defaultdict(int)
        for el in cpdomains:
            times,splits=el.split(" ")
            times=int(times)
            address=splits.split(".")
            n=len(address)
            for i in range(n):
                sub_domain=".".join(address[i:])
                if sub_domain in domains:
                    domains[sub_domain]+=times
                else:
                    domains[sub_domain]=times
        result=[]
        for key in domains:
            result.append(str(domains[key])+" "+key)
        return result
