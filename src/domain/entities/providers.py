# type: ignore

class ProviderEntity:
    ulr: str
    image: str

    def __init__(self,
                 url: str,
                 image: str
                 ):
        self.url = url,
        self.image = image
        # noqa: W292
