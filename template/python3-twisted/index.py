"""main."""

import sys

from function.handler import root

from twisted.internet import endpoints
from twisted.internet import reactor
from twisted.logger import FilteringLogObserver
from twisted.logger import LogLevel
from twisted.logger import LogLevelFilterPredicate
from twisted.logger import globalLogBeginner
from twisted.logger import textFileLogObserver
from twisted.web.server import Site


def main():
    """main."""
    site = Site(root)

    http_endpoint = endpoints.serverFromString(reactor, 'tcp:port=5000')
    http_endpoint.listen(site)


if __name__ == '__main__':
    log_filter = LogLevelFilterPredicate(LogLevel.debug)
    output = textFileLogObserver(sys.stderr)
    log_observer = FilteringLogObserver(observer=output,
                                        predicates=[log_filter])
    globalLogBeginner.beginLoggingTo([log_observer])

    reactor.callWhenRunning(main)
    reactor.run()
