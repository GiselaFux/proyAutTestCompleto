from .client import ApiClient

class PostsService:
    def __init__(self, client: ApiClient):
        self.client = client

    def get_all_posts(self):
        response = self.client.get("/posts")
        response.raise_for_status()
        return response.json()

    def create_post(self, title: str, body: str, user_id: int):
        payload = {"title": title, "body": body, "userId": user_id}
        response = self.client.post("/posts", json=payload)
        response.raise_for_status()
        return response.json()

    def delete_post(self, post_id: int) -> int:
        response = self.client.delete(f"/posts/{post_id}")
        response.raise_for_status()
        return response.status_code