import requests
from flask import Flask, app, Response
from prometheus_client import CollectorRegistry,Gauge,generate_latest
urls = ["https://httpstat.us/503","https://httpstat.us/200"]
app = Flask(__name__)

def check_site(site):
    site = site.strip()
    response = requests.get(site)
    if response.status_code == 200:
        status = 1
    else:
        status = 0
    responsetime = response.elapsed.total_seconds()*1000
    return status, responsetime

def prom_metrics():
    registry = CollectorRegistry()
    g = Gauge("sample_external_url_up","checks if url is up by checking if status is 200",['site'],registry=registry)
    m = Gauge("sample_external_url_response_ms","url response time in ms",['site'],registry=registry)
    for site in urls:
        status, time = check_site(site)
        if status == 1:
            g.labels(site).set(status)
            m.labels(site).set(time)
        else:
            g.labels(site).set(status)
            m.labels(site).set(time)
    return registry

@app.route("/metrics")
def metric():
    return Response(generate_latest(prom_metrics()), mimetype="text/plain")

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=8000)