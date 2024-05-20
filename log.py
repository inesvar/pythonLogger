from inspect import getframeinfo, stack
from colored import fore, style
from enum import Enum
import os


class LogLevels(Enum):
    ERROR = 4
    WARN = 3
    INFO = 2
    DEBUG = 1
    TRACE = 0

    def __le__(self, other):
        if self.__class__ is other.__class__:
            return self.value <= other.value
        return NotImplemented

    def __color(self):
        match self:
            case LogLevels.ERROR:
                return fore('red')
            case LogLevels.WARN:
                return fore('orange_1')
            case LogLevels.INFO:
                return fore('green')
            case LogLevels.DEBUG:
                return fore('white')
            case LogLevels.TRACE:
                return fore('dark_gray')
            case _:
                error("unreachable")

    def __print_header(self, file, flush):
        # filename, lineno, function, code_context, index
        info = getframeinfo(stack()[3][0])
        color = self.__color() if file is None else ""
        reset = style('reset') if file is None else ""
        blue = secondary_color if file is None else ""
        header = default_header.format(secondary_color=blue, filename=os.path.basename(
            info.filename), lineno=info.lineno, function=info.function, reset=reset, color=color, log_name=self.name)
        print(header, end="", file=file, flush=flush)
        return reset

    def log(self, *objects, sep=' ', end='\n', file=None, flush=False):
        if log_level <= self:
            reset_color = self.__print_header(file, flush)
            print(*objects, reset_color,
                  sep=sep, end=end, file=file, flush=flush)


default_header = "{secondary_color}{filename}:{lineno} ({function}){reset} {color}{log_name}: "
secondary_color = fore('blue')
log_level = LogLevels.INFO


def error(*objects, sep=' ', end='\n', file=None, flush=False):
    LogLevels.ERROR.log(*objects, sep=sep, end=end,
                        file=file, flush=flush)


def warn(*objects, sep=' ', end='\n', file=None, flush=False):
    LogLevels.WARN.log(*objects, sep=sep, end=end,
                       file=file, flush=flush)


def info(*objects, sep=' ', end='\n', file=None, flush=False):
    LogLevels.INFO.log(*objects, sep=sep, end=end,
                       file=file, flush=flush)


def debug(*objects, sep=' ', end='\n', file=None, flush=False):
    LogLevels.DEBUG.log(*objects, sep=sep, end=end,
                        file=file, flush=flush)


def trace(*objects, sep=' ', end='\n', file=None, flush=False):
    LogLevels.TRACE.log(*objects, sep=sep, end=end,
                        file=file, flush=flush)
