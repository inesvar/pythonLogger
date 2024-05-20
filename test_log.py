import log


def main():
    log.log_level = log.LogLevels.TRACE

    # supports multiple arguments separated by commas like python's print
    log.error("lol", 5 + 4, "hey")

    # you can optionally specify `sep` and `end`
    log.warn("lol", 5, "hey", sep=", ")
    log.info("lol", 5, "hey", end="\n\n")

    # you can output to a file (without the colors)
    file = open("aha", "w")
    log.debug("lol", 5, "hey", file=file)

    # and of course you can specify the logs you want to see
    log.trace("lol", 5, "hey")
    log.log_level = log.LogLevels.INFO
    log.trace("should not be printed")


main()
