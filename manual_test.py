import requests
import time

# Set the parameters
endpoint = "http://example.com/api"
payload = {"key1": "value1", "key2": "value2"}
num_requests = 10
parallel = True  # set to True to send requests in parallel, False to send requests linearly

# Send requests
if parallel:
    start_time = time.time()
    responses = []
    with requests.Session() as session:
        session.mount(endpoint, requests.adapters.HTTPAdapter(pool_connections=100, pool_maxsize=100))
        for i in range(num_requests):
            response = session.post(endpoint, json=payload)
            responses.append(response)
    end_time = time.time()
else:
    start_time = time.time()
    for i in range(num_requests):
        response = requests.post(endpoint, json=payload)
    end_time = time.time()
    responses = [response] * num_requests

# Print the response times
print("Response times:")
for response in responses:
    print(response.elapsed.total_seconds())

# Print the total time taken
print("Total time taken: {} seconds".format(end_time - start_time))
