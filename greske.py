class OLXException(Exception):
    ''' Default value '''

class ServerUnavailableError(OLXException):
    def __init__(self):
        super().__init__("Server je nedostupan. :/")

class UnknownError(OLXException):
    def __init__(self):
        super().__init__("Desila se nepoznata greška.")

class UndefinedError(OLXException):
    def __init__(self):
        super().__init__("Nisu unešeni svi podaci")