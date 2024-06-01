from inspect import getframeinfo, stack
from colored import fore, style
from enum import Enum
import os

default_header = None
log_colors = None
secondary_color = None
log_level = None
header_params = None


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
                return log_colors[0]
            case LogLevels.WARN:
                return log_colors[1]
            case LogLevels.INFO:
                return log_colors[2]
            case LogLevels.DEBUG:
                return log_colors[3]
            case LogLevels.TRACE:
                return log_colors[4]
            case _:
                pass

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
            print(*objects,
                  sep=sep, end=end + reset_color, file=file, flush=flush)


def init():
    global default_header, log_colors, secondary_color, log_level, header_params
    default_header = "{secondary_color}{filename}:{lineno} ({function}){reset} {color}{log_name}: "
    log_colors = [fore('red') + style('bold') + style('underline'), fore('dark_orange') + style('bold'), fore(
        'green_3a') + style('underline'), fore('white'), fore('steel_blue') + style('dim')]
    secondary_color = fore('blue') + style('italic')
    log_level = LogLevels.INFO
    header_params = ["secondary_color", "filename",
                     "lineno", "function", "reset", "color", "log_name"]


init()
