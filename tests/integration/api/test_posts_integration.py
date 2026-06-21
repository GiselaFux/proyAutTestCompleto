import yaml
import yaml
import pytest
from api.client import ApiClient
from api.services import PostsService

def get_config():
    with open("config/config.yaml") as f:
        return yaml.safe_load(f)

@pytest.mark.api
@pytest.mark.integration
def test_get_all_posts_integration():
    cfg = get_config()
    client = ApiClient(cfg["api_base_url"])
    service = PostsService(client)

    posts = service.get_all_posts()

    assert len(posts) > 0
    assert "id" in posts[0]

@pytest.mark.api
@pytest.mark.integration
def test_create_post_integration():
    cfg = get_config()
    client = ApiClient(cfg["api_base_url"])
    service = PostsService(client)

    result = service.create_post("foo", "bar", 1)

    assert result["title"] == "foo"
    assert "id" in result