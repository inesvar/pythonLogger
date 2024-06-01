from .loglib import LogLevels, logger


def error(*objects, sep=' ', end='\n', file=None, flush=False):
    """
    Behaves like python's classic `print`, except
    - it adds a header with the filename, the line number (see `setHeader()`)
    - it uses an adapted color (bold underlined red, it can be changed in `setLogColors()`)
    The logs shown can be configured using `setLogLevel()`
    """
    logger.log(*objects, log_level=LogLevels.ERROR, sep=sep, end=end,
               file=file, flush=flush)


def warn(*objects, sep=' ', end='\n', file=None, flush=False):
    """
    Behaves like python's classic `print`, except
    - it adds a header with the filename, the line number (see `setHeader()`)
    - it uses an adapted color (bold orange, it can be changed in `setLogColors()`)
    The logs shown can be configured using `setLogLevel()`
    """
    logger.log(*objects, log_level=LogLevels.WARN, sep=sep, end=end,
               file=file, flush=flush)


def info(*objects, sep=' ', end='\n', file=None, flush=False):
    """
    Behaves like python's classic `print`, except
    - it adds a header with the filename, the line number (see `setHeader()`)
    - it uses an adapted color (underlined green, it can be changed in `setLogColors()`)
    The logs shown can be configured using `setLogLevel()`
    """
    logger.log(*objects, log_level=LogLevels.INFO, sep=sep, end=end,
               file=file, flush=flush)


def debug(*objects, sep=' ', end='\n', file=None, flush=False):
    """
    Behaves like python's classic `print`, except
    - it adds a header with the filename, the line number (see `setHeader()`)
    - it uses an adapted color (white, it can be changed in `setLogColors()`)
    The logs shown can be configured using `setLogLevel()`
    """
    logger.log(*objects, log_level=LogLevels.DEBUG, sep=sep, end=end,
               file=file, flush=flush)


def trace(*objects, sep=' ', end='\n', file=None, flush=False):
    """
    Behaves like python's classic `print`, except
    - it adds a header with the filename, the line number (see `setHeader()`)
    - it uses an adapted color (dimmed steel blue, it can be changed in `setLogColors()`)
    The logs shown can be configured using `setLogLevel()`
    """
    logger.log(*objects, log_level=LogLevels.TRACE, sep=sep, end=end,
               file=file, flush=flush)


def setLogLevel(new_log_level: LogLevels):
    """
    Set the log level to either
    - log.LogLevels.TRACE (see all logs)
    - log.LogLevels.DEBUG (see all logs except trace logs)
    - log.LogLevels.INFO (see all info, warn and error logs)
    - log.LogLevels.WARN (see warn and error logs)
    - log.LogLevels.ERROR (only see error logs)
    """
    logger.setLogLevel(new_log_level)


def setHeader(header: str):
    """
    Change the header. Here's the default header for inspiration :
    "{secondary_color}{filename}:{lineno} ({function}){reset} {color}{log_name}: "

    `secondary color` (defaults to blue) can be set with `setSecondaryColor()`.
    `color` is the adapted log level color which will apply for the objects being
    printed after the header.
    """
    logger.setHeader(header)


def setSecondaryColor(color: str):
    """
    Set optional header color using `fore()` or/and `style()` from module `colored`.
    Consult list of all available colors and styles here : https://dslackw.gitlab.io/colored/tables/.
    """
    logger.setSecondaryColor(color)


def setLogColors(colors: list[str]):
    """
    Set 5 log colors using `fore()` or/and `style()` from module `colored` for ERROR, WARN, INFO, DEBUG, TRACE in order.
    Consult list of all available colors and styles here : https://dslackw.gitlab.io/colored/tables/colors.
    """
    logger.setLogColors(colors)


def reset():
    """
    Reset initial values for header, log colors, secondary color and log level.
    """
    logger.reset()
