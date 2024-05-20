from colored import fore, style
from enum import Enum


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

    def _color(self):
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

    def _print_header(self, file, flush):
        color = (self._color(), style('reset')) if file is None else ("", "")
        print(color[0] + self.name + ": ", end="", file=file, flush=flush)
        return color[1]

    def log(self, *objects, sep=' ', end='\n', file=None, flush=False):
        if log_level <= self:
            reset_color = self._print_header(file, flush)
            print(*objects, reset_color,
                  sep=sep, end=end, file=file, flush=flush)


log_level = LogLevels.INFO


def error(*objects, sep=' ', end='\n', file=None, flush=False):
    LogLevels.ERROR.log(*objects, sep=sep, end=end, file=file, flush=flush)


def warn(*objects, sep=' ', end='\n', file=None, flush=False):
    LogLevels.WARN.log(*objects, sep=sep, end=end, file=file, flush=flush)


def info(*objects, sep=' ', end='\n', file=None, flush=False):
    LogLevels.INFO.log(*objects, sep=sep, end=end, file=file, flush=flush)


def debug(*objects, sep=' ', end='\n', file=None, flush=False):
    LogLevels.DEBUG.log(*objects, sep=sep, end=end, file=file, flush=flush)


def trace(*objects, sep=' ', end='\n', file=None, flush=False):
    LogLevels.TRACE.log(*objects, sep=sep, end=end, file=file, flush=flush)
