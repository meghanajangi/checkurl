# checkurl
Python program to check the status of url using status codes

- The service queries 2 urls (https://httpstat.us/503 & https://httpstat.us/200)
- The service checks the external urls (https://httpstat.us/503 & https://httpstat.us/200 ) are up (based on http status code 200) and response time in milliseconds
- The service will runs simple http service that produces metrics using appropriate Prometheus libraries and outputs on /metrics

Expected response format:
- sample_external_url_up{url="https://httpstat.us/503 "}  = 0
- sample_external_url_response_ms{url="https://httpstat.us/503 "}  = [value]
- sample_external_url_up{url="https://httpstat.us/200 "}  = 1
- sample_external_url_response_ms{url="https://httpstat.us/200 "}  = [value]
