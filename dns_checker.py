from dns import resolver
import logging

class CheckDNS:
    dns_record ={
        'a':'A',
        'aaaa':'AAAA',
        'ns':'NS',
        'cname':'CNAME',
        'mx':'MX',
        'ptr':'PTR',
        'soa':'SOA',
        'srv':'SRV',
        'txt':'TXT'
    }

    @classmethod
    async def check(cls, domain: str, dns_type: str):
        data = []
        dns_type = cls.dns_record[dns_type]
        result = resolver.resolve(domain,dns_type)

        try:
            for r in result:
                if r.to_text() not in data:
                    data.append(r.to_text())
        except:
            logging.error(msg="error")
            pass

        return data
