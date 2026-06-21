import requests

class ApiClient:
    def __init__(self, base_url: str):
        self.base_url = base_url.rstrip("/")

    def get(self, path: str, **kwargs):
        url = f"{self.base_url}/{path.lstrip('/')}"
        return requests.get(url, **kwargs)

    def post(self, path: str, json=None, **kwargs):
        url = f"{self.base_url}/{path.lstrip('/')}"
        return requests.post(url, json=json, **kwargs)

    def delete(self, path: str, **kwargs):
        url = f"{self.base_url}/{path.lstrip('/')}"
        return requests.delete(url, **kwargs)