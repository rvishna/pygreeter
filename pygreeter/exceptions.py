class PyGreeterError(Exception):
    """Base class for exceptions raised by pygreeter."""


class MissingNameError(PyGreeterError):
    """Raised when pygreeter is called without a name."""

    def __str__(self):
        return "A name is required for greeting."
