# type: ignore
from typing import Optional


class PosterEntity:
    url: str
    image: str
    type_poster: Optional[str] = None

    def __init__(self,
                 url: str,
                 image: str,
                 type_poster: Optional[str] = None):
        self.url = url
        self.image = image
        self.type_poster = type_poster
        # noqa: W292
