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


log_level = LogLevels.INFO


def error(*objects, sep=' ', end='\n', file=None, flush=False):
    if log_level <= LogLevels.ERROR:
        color = (fore('red'), style('reset')) if file is None else ("", "")
        print(color[0] + "ERROR:", end=" ", file=file, flush=flush)
        print(*objects, color[1],
              sep=sep, end=end, file=file, flush=flush)


def warn(*objects, sep=' ', end='\n', file=None, flush=False):
    if log_level <= LogLevels.WARN:
        color = (fore('orange_1'), style('reset')) if file is None else ("", "")
        print(color[0] + "WARN:", end=" ", file=file, flush=flush)
        print(*objects, color[1],
              sep=sep, end=end, file=file, flush=flush)


def info(*objects, sep=' ', end='\n', file=None, flush=False):
    if log_level <= LogLevels.INFO:
        color = (fore('green'), style('reset')) if file is None else ("", "")
        print(color[0] + "INFO:", end=" ", file=file, flush=flush)
        print(*objects, color[1],
              sep=sep, end=end, file=file, flush=flush)


def debug(*objects, sep=' ', end='\n', file=None, flush=False):
    if log_level <= LogLevels.DEBUG:
        color = (fore('white'), style('reset')) if file is None else ("", "")
        print(color[0] + "DEBUG:", end=" ", file=file, flush=flush)
        print(*objects, color[1],
              sep=sep, end=end, file=file, flush=flush)


def trace(*objects, sep=' ', end='\n', file=None, flush=False):
    if log_level <= LogLevels.TRACE:
        color = (fore('dark_gray'), style('reset')) if file is None else ("", "")
        print(color[0] + "TRACE:", end=" ", file=file, flush=flush)
        print(*objects, color[1],
              sep=sep, end=end, file=file, flush=flush)
