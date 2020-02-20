from twisted.internet import reactor
from twisted.internet.defer import Deferred
from twisted.logger import Logger
from twisted.python.url import URL
from twisted.web.http_headers import Headers
from twisted.web.resource import Resource


class Root(Resource):
    """Root."""

    log = Logger()
    isLeaf = True  # noqa: N815

    def render_GET(self, request):  # noqa: N802
        """Respond to a GET request."""
        self.log.debug('prepath: {prepath:}', prepath=request.prepath)
        self.log.debug('postpath: {postpath:}', postpath=request.postpath)

        return b'OK'
