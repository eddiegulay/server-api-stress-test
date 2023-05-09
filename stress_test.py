import requests
import time
import argparse
import concurrent.futures

# Define command line arguments
parser = argparse.ArgumentParser()
parser.add_argument("url", help="API endpoint URL")
parser.add_argument("payload", help="Request payload as JSON string")
parser.add_argument("num_requests", type=int, help="Number of requests to send")
parser.add_argument("--parallel", action="store_true", help="Send requests in parallel")
args = parser.parse_args()

# Define function to send a single request
def send_request(url, payload):
    start_time = time.time()
    response = requests.post(url, json=payload)
    end_time = time.time()
    return (response.status_code, end_time - start_time)

# Send requests in parallel or linearly
if args.parallel:
    with concurrent.futures.ThreadPoolExecutor() as executor:
        futures = [executor.submit(send_request, args.url, args.payload) for _ in range(args.num_requests)]
        for future in concurrent.futures.as_completed(futures):
            status_code, time_taken = future.result()
            print(f"Request status code: {status_code}, Time taken: {time_taken}")
else:
    for i in range(args.num_requests):
        status_code, time_taken = send_request(args.url, args.payload)
        print(f"Request status code: {status_code}, Time taken: {time_taken}")
