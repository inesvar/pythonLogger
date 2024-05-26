from loglib import LogLevels
from colored import fore
import loglib
import re


def error(*objects, sep=' ', end='\n', file=None, flush=False):
    """
    Behaves like python's classic `print`, except
    - it adds a header with the filename, the line number (see `setHeader()`)
    - it uses an adapted color (bold underlined red, it can be changed in `setLogColors()`)
    The logs shown can be configured using `setLogLevel()`
    """
    LogLevels.ERROR.log(*objects, sep=sep, end=end,
                        file=file, flush=flush)


def warn(*objects, sep=' ', end='\n', file=None, flush=False):
    """
    Behaves like python's classic `print`, except
    - it adds a header with the filename, the line number (see `setHeader()`)
    - it uses an adapted color (bold orange, it can be changed in `setLogColors()`)
    The logs shown can be configured using `setLogLevel()`
    """
    LogLevels.WARN.log(*objects, sep=sep, end=end,
                       file=file, flush=flush)


def info(*objects, sep=' ', end='\n', file=None, flush=False):
    """
    Behaves like python's classic `print`, except
    - it adds a header with the filename, the line number (see `setHeader()`)
    - it uses an adapted color (underlined green, it can be changed in `setLogColors()`)
    The logs shown can be configured using `setLogLevel()`
    """
    LogLevels.INFO.log(*objects, sep=sep, end=end,
                       file=file, flush=flush)


def debug(*objects, sep=' ', end='\n', file=None, flush=False):
    """
    Behaves like python's classic `print`, except
    - it adds a header with the filename, the line number (see `setHeader()`)
    - it uses an adapted color (white, it can be changed in `setLogColors()`)
    The logs shown can be configured using `setLogLevel()`
    """
    LogLevels.DEBUG.log(*objects, sep=sep, end=end,
                        file=file, flush=flush)


def trace(*objects, sep=' ', end='\n', file=None, flush=False):
    """
    Behaves like python's classic `print`, except
    - it adds a header with the filename, the line number (see `setHeader()`)
    - it uses an adapted color (dimmed steel blue, it can be changed in `setLogColors()`)
    The logs shown can be configured using `setLogLevel()`
    """
    LogLevels.TRACE.log(*objects, sep=sep, end=end,
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
    if isinstance(new_log_level, LogLevels):
        loglib.log_level = new_log_level
    else:
        warn("'" + new_log_level + "'",
             "is not an instance of type `LogLevels`, log level is unchanged.")


def setHeader(header: str):
    """
    Change the header. Here's the default header for inspiration :
    "{secondary_color}{filename}:{lineno} ({function}){reset} {color}{log_name}: "

    `secondary color` (defaults to blue) can be set with `setSecondaryColor()`.
    `color` is the adapted log level color which will apply for the objects being
    printed after the header.
    """
    if not isinstance(header, str):
        warn("'" + str(header) + "'",
             "is not an instance of type `str`, header is unchanged.")
        return
    elif header.count("{") != header.count("}"):
        warn("'" + str(header) + "'",
             "doesn't contain the same number of '{' and '}', header is unchanged.")
        return
    elif all(placeholder in loglib.header_params for placeholder in re.findall(r"{(.*?)}", header)):
        loglib.default_header = header
    else:
        warn("'" + str(header) + "'",
             "contains some unknown params (known params are ", str(loglib.header_params) + "), header is unchanged.")
        return


def setSecondaryColor(color: str):
    """
    Set optional header color using `fore()` or/and `style()` from module `colored`.
    Consult list of all available colors and styles here : https://dslackw.gitlab.io/colored/tables/.
    """
    if not isinstance(color, str):
        warn("'" + str(color) + "'",
             "is not an instance of type `str`, header is unchanged.")
        return
    loglib.secondary_color = color


def setLogColors(colors: list[str]):
    """
    Set 5 log colors using `fore()` or/and `style()` from module `colored` for ERROR, WARN, INFO, DEBUG, TRACE in order.
    Consult list of all available colors and styles here : https://dslackw.gitlab.io/colored/tables/colors.
    """
    if len(colors) != 5:
        warn("'" + str(colors) + "'",
             "should contain 5 colors, log colors are unchanged.")
        return
    if not all(isinstance(color, str) for color in colors):
        warn("'" + str(colors) + "'",
             "contains instances that aren't of type `str`, header is unchanged.")
        return
    loglib.log_colors = colors


def reset():
    """
    Reset initial values for header, log colors, secondary color and log level.
    """
    loglib.init()
