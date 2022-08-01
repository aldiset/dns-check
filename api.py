import json
import asyncio
from flask import Flask, request, jsonify

from dns_checker import CheckDNS

app = Flask(__name__)
dns = CheckDNS()

@app.route('/', methods=['GET'])
async def index():
    return jsonify({
        "message":"welcome !"
    })
    
@app.route('/', methods=['POST'])
async def post_domain():
    data = json.loads(request.data)
    data_dns = await dns.check(domain=data["domain"], dns_type=data["dns_type"])
    return jsonify({
        "data":data_dns
    })

asyncio.run(app.run(debug=True))