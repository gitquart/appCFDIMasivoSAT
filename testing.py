from suds.client import Client
import requests

#Example: How to send a WSDL request with body (XML)

url = "https://httpbin.org/post"

headers = {"content-type" : "application/soap+xml"}
body = """
<soapenv:Envelope xmlns:soapenv="http://schemas.xmlsoap.org/soap/envelope/" xmlns:req="https://httpbin.org/post">
   <soapenv:Header/>
   <soapenv:Body/>
</soapenv:Envelope>
"""

response = requests.post(url, data = body, headers = headers)
print(response)