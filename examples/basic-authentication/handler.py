"""Example of a handler that enforces basic authentication."""

import hashlib

from zope.interface import implementer

from twisted.cred.checkers import FilePasswordDB
from twisted.cred.portal import IRealm
from twisted.cred.portal import Portal
from twisted.internet.defer import succeed
from twisted.logger import Logger
from twisted.web.guard import BasicCredentialFactory
from twisted.web.guard import HTTPAuthSessionWrapper
from twisted.web.resource import IResource
from twisted.web.resource import Resource


def hash(username, provided_password, stored_password):
    """Hash the password."""
    stored_password = bytes.fromhex(stored_password.decode('us-ascii'))
    salt = stored_password[:64]
    stored_password = stored_password[64:]
    hashed_password = hashlib.scrypt(provided_password, salt=salt, n=16384, r=8, p=1, dklen=64)
    return (salt + hashed_password).hex().encode('us-ascii')


@implementer(IRealm)
class SimpleRealm(object):
    """Simple Realm."""

    log = Logger()

    def __init__(self, resource):
        """Initialize."""
        self.resource = resource

    def requestAvatar(self, avatarId, mind, *interfaces):  # noqa: N802,N803
        """Request Avatar."""
        if IResource in interfaces:
            return succeed((IResource, self.resource, lambda: None))
        raise NotImplementedError()


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


realm = SimpleRealm(Root())
checker = FilePasswordDB('/var/openfaas/secrets/passwords', hash=hash)
portal = Portal(realm, [checker])
credential_factory = BasicCredentialFactory(b'authentication test')
root = HTTPAuthSessionWrapper(portal, [credential_factory])
