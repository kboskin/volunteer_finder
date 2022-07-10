class AuthException(Exception):
    pass


class CredentialsException(AuthException):
    pass


class CodeExpiredError(AuthException):

    def __init__(self, message, status):
        self.message = message
        self.status = status


class CodeMismatchError(AuthException):

    def __init__(self, message, status):
        self.message = message
        self.status = status


class NumberIssueError(AuthException):

    def __init__(self, message, status):
        self.message = message
        self.status = status
