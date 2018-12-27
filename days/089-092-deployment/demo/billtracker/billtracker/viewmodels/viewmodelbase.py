from pyramid.request import Request


class ViewModelBase:
    def __init__(self, request: Request):
        self.request = request
        self.error = None

    def to_dict(self) -> dict:
        return self.__dict__
