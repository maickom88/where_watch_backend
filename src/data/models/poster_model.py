
from src.domain.entities.poster_entity import PosterEntity


class PosterModel(PosterEntity):
    url: str
    image: str
    type_poster: str

    def __init__(self, url: str, image: str, type_poster: str):
        self.url = url
        self.image = image
        self.type_poster = type_poster
        # noqa: W292

    def toString(self):
        print(
            f'''
            URL: {self.url}\n
            IMAGE: {self.image}\n
            TYPE: {self.type_poster}''')
