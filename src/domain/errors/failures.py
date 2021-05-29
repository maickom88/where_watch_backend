# type: ignore
class Failure(Exception):
    def get_message_error(self) -> str:
        pass


class DomainFailure(Failure):
    def __init__(self, message: str = "Error de dominio"):
        self.message = message

    def get_message_error(self) -> str:
        return self.message


class NotFoundFailure(Failure):
    def __init__(self, message: str = "Nada encontrado!"):
        self.message = message

    def get_message_error(self) -> str:
        return self.message


class ScrapingFailure(Failure):
    def __init__(self, message: str = "Error ao tentar fazer scraping!"):
        self.message = message

    def get_message_error(self) -> str:
        return self.message


class ResponseFailure(Failure):
    def __init__(self, message: str = "Error ao tentar obter conteúdo!"):
        self.message = message

    def get_message_error(self) -> str:
        return self.message
