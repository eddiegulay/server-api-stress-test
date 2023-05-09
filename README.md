# server-api-stress-test
Sending multiple API requests to server for processing speed test and payload stress test

## Usage

For the CLI Client 
```bash
python stress_test.py https://example.com/api '{"key": "value"}' 100 --parallel
```

For Manual config update these variables in the script 'manual_test.py'
```python
# Set the parameters
endpoint = "http://example.com/api"
payload = {"key1": "value1", "key2": "value2"}
num_requests = 10
parallel = True  # set to True to send requests in parallel, False to send requests linearly
```