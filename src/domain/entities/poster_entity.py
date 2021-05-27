class PosterEnitity:
    url: str
    image: str
    type_poster: str

    def __init__(self, url: str, image: str, type_poster: str):
        self.url = url
        self.image = image
        # noqa: W292
        self.type_poster = type_poster