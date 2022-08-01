# dns-check

## what is dns-check ?
dns-check is tools open source to check dns record domain

### how to use it ?
```curl
    curl --request POST \
      --url http://127.0.0.1:5000/ \
      --header 'Content-Type: application/json' \
      --data '{
      "domain":"google.com",
      "dns_type":"ns"
    }'
```

### response
```curl
    {
	"data": [
		"ns4.google.com.",
		"ns2.google.com.",
		"ns3.google.com.",
		"ns1.google.com."
        ]
    }
```
