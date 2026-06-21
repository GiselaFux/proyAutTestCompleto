import pytest
from api.services import PostsService
from api.client import ApiClient

class DummyResponse:
    def __init__(self, json_data, status_code=200):
        self._json_data = json_data
        self.status_code = status_code

    def json(self):
        return self._json_data

    def raise_for_status(self):
        if not (200 <= self.status_code < 300):
            raise Exception("HTTP error")

class FakeClient(ApiClient):
    def __init__(self):
        super().__init__("http://fake")
        self.last_request = None

    def get(self, path, **kwargs):
        self.last_request = ("GET", path, kwargs)
        return DummyResponse([{"id": 1}, {"id": 2}])

    def post(self, path, json=None, **kwargs):
        self.last_request = ("POST", path, json, kwargs)
        return DummyResponse({**(json or {}), "id": 101}, 201)

    def delete(self, path, **kwargs):
        self.last_request = ("DELETE", path, kwargs)
        return DummyResponse({}, 200)

@pytest.mark.unit
def test_get_all_posts_unit():
    client = FakeClient()
    service = PostsService(client)
    posts = service.get_all_posts()

    assert len(posts) == 2
    assert client.last_request[0] == "GET"

@pytest.mark.unit
def test_create_post_unit():
    client = FakeClient()
    service = PostsService(client)
    result = service.create_post("foo", "bar", 1)

    assert result["title"] == "foo"
    assert result["id"] == 101
    assert client.last_request[0] == "POST"

@pytest.mark.unit
def test_delete_post_unit():
    client = FakeClient()
    service = PostsService(client)
    status = service.delete_post(1)

    assert status == 200
    assert client.last_request[0] == "DELETE"