from inspect import getframeinfo, stack
from colored import fore, style
from enum import Enum
import os
import re


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


class Logger():
    __secondary_color = None
    __default_header = None
    __header_params = None
    __log_colors = None
    __log_level = None

    def __init__(self):
        self.reset()

    def __get_level_color(self, log_level):
        return self.__log_colors[log_level.value]

    def __print_level_header(self, log_level, file, flush):
        # filename, lineno, function, code_context, index
        info = getframeinfo(stack()[3][0])
        color = self.__get_level_color(log_level) if file is None else ""
        reset = style('reset') if file is None else ""
        second_color = self.__secondary_color if file is None else ""
        header = self.__default_header.format(secondary_color=second_color, filename=os.path.basename(
            info.filename), lineno=info.lineno, function=info.function, reset=reset, color=color, log_name=log_level.name)
        print(header, end="", file=file, flush=flush)
        return reset

    def log(self, *objects, log_level=LogLevels.TRACE, sep=' ', end='\n', file=None, flush=False):
        if self.__log_level <= log_level:
            reset_color = self.__print_level_header(file, flush)
            print(*objects,
                  sep=sep, end=end + reset_color, file=file, flush=flush)

    def setLogLevel(self, new_log_level):
        if not isinstance(new_log_level, LogLevels):
            self.log("'" + new_log_level + "'",
                     "is not an instance of type `LogLevels`,",
                     "log level is unchanged.", log_level=LogLevels.WARN)
            return
        self.__log_level = new_log_level

    def setHeader(self, header):
        if not isinstance(header, str):
            self.log("'" + str(header) + "'",
                     "is not an instance of type `str`,",
                     "header is unchanged.", log_level=LogLevels.WARN)
            return
        if header.count("{") != header.count("}"):
            self.log("'" + str(header) + "'",
                     "doesn't contain the same number of '{' and '}',",
                     "header is unchanged.", log_level=LogLevels.WARN)
            return
        if any(placeholder not in self.__header_params
               for placeholder in re.findall(r"{(.*?)}", header)):
            self.log("'" + str(header) + "'",
                     "contains some unknown params (known params are ",
                     str(self.__header_params) + "), header is unchanged.")
            return
        self.__default_header = header

    def setSecondaryColor(self, color):
        if not isinstance(color, str):
            self.log("'" + str(color) + "'",
                     "is not an instance of type `str`, header is unchanged.",
                     log_level=LogLevels.WARN)
            return
        self.__secondary_color = color

    def setLogColors(self, colors):
        if len(colors) != 5:
            self.log("'" + str(colors) + "'",
                     "should contain 5 colors, log colors are unchanged.",
                     log_level=LogLevels.WARN)
            return
        if not all(isinstance(color, str) for color in colors):
            self.log("'" + str(colors) + "'",
                     "contains instances that aren't of type `str`,",
                     "header is unchanged.", log_level=LogLevels.WARN)
            return
        self.__log_colors = colors

    def reset(self):
        self.__default_header = "{secondary_color}{filename}:{lineno} ({function}){reset} {color}{log_name}: "
        self.__log_colors = [fore('red') + style('bold') + style('underline'), fore('dark_orange') + style('bold'), fore(
            'green_3a') + style('underline'), fore('white'), fore('steel_blue') + style('dim')]
        self.__secondary_color = fore('blue') + style('italic')
        self.__log_level = LogLevels.INFO
        self.__header_params = ["secondary_color", "filename",
                                "lineno", "function", "reset", "color", "log_name"]


logger = Logger()
