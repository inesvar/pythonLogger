from loglib import LogLevels
from colored import fore
import loglib
import re


def error(*objects, sep=' ', end='\n', file=None, flush=False):
    """
    Behaves like python's classic `print`, except
    - it adds a header with the filename, the line number (see `setHeader()`)
    - it uses an adapted color (red, it can be changed in `setLogColors()`)
    The logs shown can be configured using `setLogLevel()`
    """
    LogLevels.ERROR.log(*objects, sep=sep, end=end,
                        file=file, flush=flush)


def warn(*objects, sep=' ', end='\n', file=None, flush=False):
    """
    Behaves like python's classic `print`, except
    - it adds a header with the filename, the line number (see `setHeader()`)
    - it uses an adapted color (orange, it can be changed in `setLogColors()`)
    The logs shown can be configured using `setLogLevel()`
    """
    LogLevels.WARN.log(*objects, sep=sep, end=end,
                       file=file, flush=flush)


def info(*objects, sep=' ', end='\n', file=None, flush=False):
    """
    Behaves like python's classic `print`, except
    - it adds a header with the filename, the line number (see `setHeader()`)
    - it uses an adapted color (green, it can be changed in `setLogColors()`)
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
    - it uses an adapted color (gray, it can be changed in `setLogColors()`)
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
        trace("Log level changed to", new_log_level)
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
        trace("Header changed to ", "'" + str(header) + "'")
    else:
        warn("'" + str(header) + "'",
             "contains some unknown params (known params are ", str(loglib.header_params) + "), header is unchanged.")
        return


def setSecondaryColor(color: str | int):
    """
    Set optional header color using `fore()` from module `colored`.
    Consult list of all available colors here : https://dslackw.gitlab.io/colored/tables/colors.
    """
    try:
        loglib.secondary_color = fore(color)
        trace("Secondary color changed to", color)
    except:
        warn("'" + str(color) + "'",
             "isn't available in function `fore()` from module `colored`, secondary color is unchanged.")
        return


def setLogColors(colors: list[str | int]):
    """
    Set 5 log color using `fore()` from module `colored` for ERROR, WARN, INFO, DEBUG, TRACE in order.
    Consult list of all available colors here : https://dslackw.gitlab.io/colored/tables/colors.
    """
    if len(colors) != 5:
        warn("'" + str(colors) + "'",
             "should contain 5 colors, log colors are unchanged.")
        return
    try:
        loglib.log_colors = [fore(color) for color in colors]
        trace("Log colors changed to", colors)
    except:
        warn("Some color from '" + str(colors) + "'",
             "isn't available in function `fore()` from module `colored`, log colors are unchanged.")
        return


def reset():
    """
    Reset initial values for header, log colors, secondary color and log level.
    """
    loglib.default_header = "{secondary_color}{filename}:{lineno} ({function}){reset} {color}{log_name}: "
    loglib.log_colors = [fore('red'), fore('dark_orange'), fore(
        'green_3a'), fore('white'), fore('steel_blue')]
    loglib.secondary_color = fore('blue')
    loglib.log_level = LogLevels.INFO
