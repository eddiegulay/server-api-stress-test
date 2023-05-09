import requests
import time

url = "http://127.0.0.1:5000/api/home"
payload = {"uid":1515}

# number of requests to send
num_requests = 100

# function to send requests
def send_request(url, payload):
    start_time = time.time()
    r = requests.post(url, json=payload)
    end_time = time.time()

    total_time = end_time - start_time
    request_time = r.elapsed.total_seconds()
    processing_time = request_time - total_time
    response_time = total_time - processing_time

    return request_time, processing_time, response_time

# send requests and measure time
for i in range(num_requests):
    request_time, processing_time, response_time = send_request(url, payload)
    print(f"Request {i+1} - Request time: {request_time}, Processing time: {processing_time}, Response time: {response_time}")
