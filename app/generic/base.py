class BaseSuccessResponse:
    def __init__(self, success, message):
        self.message = message
        self.success = success

