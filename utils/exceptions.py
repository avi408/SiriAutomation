class FrameworkException(Exception):
    """Base exception for automation framework."""
    pass


class ElementNotFoundException(FrameworkException):
    """Raised when an element cannot be located."""
    pass


class DriverInitializationException(FrameworkException):
    """Raised when Appium driver initialization fails."""
    pass