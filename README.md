# StupidLogger

This logger is as simple as it can be with the following features :

- **5 logging levels** : error, warn, info, debug, trace
- an intuitive **python-style syntax**
- **easy customization** for the colors and header info
- with **documentation** for easy use

It's based on package [colored](https://pypi.org/project/colored/) for the default log colors and styles, but you can also use [colorama](https://pypi.org/project/colorama/) or custom escape sequences to set your own colors.

Here's a usage example :

```python
import stupidlogger as log

def test_all_levels():
    # supports multiple arguments separated by commas like print
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
    file = open("stupidlog", "w")
    log.debug("This will be printed to a file", file=file)

    log.trace("Entire content of a list :", list(range(9)), end="\n\n")

test_all_levels()
```

![](https://github.com/inesvar/pythonLogger/raw/main/pictures/log_colors.png)

# 5 logging levels : error, warn, info, debug, trace<a name="one"></a>

You can filter out logs by using `setLogLevel`. The default level is `LogLevels.INFO`.

```python
from stupidlogger import *

setLogLevel(LogLevels.DEBUG)
```

# It uses Python's `print` syntax<a name="two"></a>

Contrary to the `logging` module, you can print multiple arguments separated by commas.

```python
info("This is a useful message with data", 54 + 25,
     "and other stuff", list(range(1)), end="\n\n")
```
![](https://github.com/inesvar/pythonLogger/raw/main/pictures/info_example.png)

Actually the log functions' signatures are exactly the same as for `print` (you can also print to a file!).

```python
info(*objects, sep=' ', end='\n', file=None, flush=False)
```

# The colors and header info are entirely customizable<a name="three"></a>

The log outputs are made of two parts : the header and the message.

You can change the information in the header using `setHeader`, and its color using `setSecondaryColor`.

You can also change the 5 colors associated with the log levels using `setLogColors`.

Here's an example script using colorama and its output :
```python
from stupidlogger import *
from colorama import Fore

setLogLevel(LogLevels.TRACE)
setHeader("{color}{filename}:{lineno} ({function}) {log_name}:{reset} ")
setLogColors([Fore.BLUE, Fore.CYAN, Fore.GREEN, Fore.YELLOW, Fore.BLACK])
error("error")
warn("warn")
info("info")
debug("debug")
trace("trace")
```

![](https://github.com/inesvar/pythonLogger/raw/main/pictures/colorama_example.png)

# If you have questions<a name="four"></a>

`log.py` contains the interface. It's well documented and should provide the answers about how to use the code. The structure itself is in `loglib.py` and should provide the answers about how it works.