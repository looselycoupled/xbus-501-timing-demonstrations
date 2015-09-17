Overview
--------

A collection of scripts to demonstrate very easy ways to benchmark code or time execution.  These scripts are presented as a starting off point to get you thinking about performance and measurement.

Example 1
---------

This example demonstrates the use of the `time` utility as found on most Unix like personal computers (may not be available on Windows).  For more information on how to use the command, consult the man file with `man time`.

For a quick explanation of real, user, and sys values please review [this](http://stackoverflow.com/questions/556405/what-do-real-user-and-sys-mean-in-the-output-of-time1#556411) Stack Overflow answer.

Usage:

    $ time python 1-example.py 10000


Example 2
---------

This example script provides the most straightforward method to provide the elapsed time for a piece of code.

Usage:

    $ python 2-example.py 10000

Example 3
---------

This example script uses a slightly more sophisticated method for timing a block of code through the use of Python context managers.  For more information on context managers and the "with" statement consult [PEP 343](https://www.python.org/dev/peps/pep-0343/).

Usage:

    $ python 3-example.py 10000

Example 4
---------

Finally, our last example uses the line_profiler library to provide line by line statistics into code execution and performance.  For more information, visit the Github repository page at [https://github.com/rkern/line_profiler](https://github.com/rkern/line_profiler).

Notice how much time this level of profiling adds to the overall execution.

Usage:

    $ kernprof -l -v 4-example.py 10000
