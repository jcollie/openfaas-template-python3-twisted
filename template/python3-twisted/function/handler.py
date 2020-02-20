"""Sample Twisted OpenFAAS handler code."""

from twisted.logger import Logger
from twisted.web.resource import Resource


class Root(Resource):
    """Root."""

    log = Logger()
    isLeaf = True  # noqa: N815

    def render_GET(self, request):  # noqa: N802
        """Respond to a GET request."""

        return b'OK'

    def render_POST(self, request):  # noqa: N802
        """Respond to a POST request."""

        return b'OK'


root = Root()
