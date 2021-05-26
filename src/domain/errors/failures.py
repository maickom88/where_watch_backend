class Failure(Exception):
    pass

class DomainFailure(Failure):
    def __init__(self, message:str = "Error de dominio"):
        self.message = message

    def get_message_error(self) -> str:
        return self.message
    

class NotFoundFailure(Failure):
    def __init__(self, message:str = "Nada encontrado!"):
        self.message = message

    def get_message_error(self) -> str:
        return self.message
    