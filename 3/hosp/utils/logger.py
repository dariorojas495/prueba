import logging

logging.basicConfig(level=logging.INFO, format="%(asctime)s - %(levelname)s - %(message)s")

def log_request(request):
    logging.info(f"Request: {request.method} {request.url}")

def log_response(response):
    logging.info(f"Response: {response.status_code} {response.body}")
