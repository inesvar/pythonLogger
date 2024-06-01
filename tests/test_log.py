from stupidlogger import log
from colored import fore, style
from colorama import Fore


def test_all_error_messages():
    # incorrect, `log.LogLevels` should be used as input
    log.setLogLevel("TRACE")
    log.setLogLevel(log.LogLevels.TRACE)
    # this function expects a str
    # an escape sequence representing a color is the expected usage
    # for example you can used return values of `fore()` or `style()` from module `colored`
    # but you can also use other modules
    log.setSecondaryColor(45)
    log.setSecondaryColor(Fore.GREEN + style('underline'))
    # the header string has to be formattable
    log.setHeader("{filename}:{lineno}{reset} -> {color}{log_na")
    log.setHeader("{filename}:{lineno}{reset} -> {color}{log_na}")
    log.setHeader(
        "{secondary_color}({function}){reset} {filename}:{lineno} -> {color}{log_name}: ")
    # this function expects a list of 5 str
    log.setLogColors(['red', 'orange', 'green', 'white'])
    log.setLogColors([fore('red') + style('bold'), fore('orange_1') + style('bold'), fore(
        'green') + style('bold'), fore('white'), fore('dark_gray')])
    log.reset()
    print()


def test_all_levels():
    # supports multiple arguments separated by commas like python's print
    log.error("Division of", 54 % 27, "by", 2 - 2, "is not allowed")

    # you can optionally specify `sep` and `end`
    log.warn(*["fruit", "vegetable", "fish", "meat"],
             sep=", ", end=" weren't found in the fridge\n")
    log.info("OPERATION SUCCESS", end="\n\n")

    # you can filter the logs you want to see
    log.debug("This will not be printed")
    # default log level is `INFO`
    log.setLogLevel(log.LogLevels.TRACE)
    i = 254
    log.debug("i =", i)

    # you can output to a file (without the colors)
    file = open("log", "w")
    log.debug("This will be printed to a file", file=file)

    log.trace("Entire content of a list :", list(range(15)), end="\n\n")


def test_encapsulation():
    assert log.loglib.logger


test_all_error_messages()
test_all_levels()
test_encapsulation()
