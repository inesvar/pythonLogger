import log


def test():
    # incorrect, `log.LogLevels` should be used as input
    log.setLogLevel("TRACE")
    log.setLogLevel(log.LogLevels.TRACE)
    # the color has to exist in https://dslackw.gitlab.io/colored/tables/colors
    log.setSecondaryColor('gray')
    log.setSecondaryColor('red')
    # the header string has to be formattable
    log.setHeader("{filename}:{lineno}{reset} -> {color}{log_na")
    log.setHeader("{filename}:{lineno}{reset} -> {color}{log_na}")
    log.setHeader(
        "{secondary_color}{filename}:{lineno}{reset} -> {color}{log_name}: ")
    # there has to be 5 valid colors from the table mentioned above
    log.setLogColors(['red', 'orange', 'green', 'white'])
    log.setLogColors(['red', 'orange', 'green', 'white', 'gray'])
    log.reset()
    print()


def main():
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

    log.trace("Entire content of a list :", list(range(15)))


test()
main()
