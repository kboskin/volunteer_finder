class BaseSuccessResponse:
    def __init__(self, data):
        self.message = "success"
        self.data = data


def object_as_dict(self):
    return self.__dict__
