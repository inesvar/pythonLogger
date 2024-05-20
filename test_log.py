import log


def test():
    log.setLogLevel("TRACE")
    log.setLogLevel(log.LogLevels.TRACE)
    log.setSecondaryColor('gray')
    log.setSecondaryColor('dark_gray')
    log.setHeader("{filename}:{lineno}{reset} -> {color}{log_na")
    log.setHeader("{filename}:{lineno}{reset} -> {color}{log_na}")
    log.setHeader(
        "{secondary_color}{filename}:{lineno}{reset} -> {color}{log_name}: ")
    log.setLogColors(['red', 'orange', 'green', 'white'])
    log.setLogColors(['red', 'orange', 'green', 'white', 'gray'])


def main():
    log.setLogLevel(log.LogLevels.TRACE)
    # supports multiple arguments separated by commas like python's print
    log.error("lol", 5 + 4, "hey")

    # you can optionally specify `sep` and `end`
    log.warn("lol", 5, "hey", sep=", ")
    log.info("lol", 5, "hey", end="\n\n")

    # you can output to a file (without the colors)
    file = open("aha", "w")
    log.debug("lol", 5, "hey", file=file)
    log.debug("lol", 5, "hey")

    # and of course you can specify the logs you want to see
    log.trace("lol", 5, "hey")
    log.setLogLevel(log.LogLevels.INFO)
    log.trace("should not be printed")


# test()
main()
