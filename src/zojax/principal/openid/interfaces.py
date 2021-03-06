##############################################################################
#
# Copyright (c) 2009 Zope Foundation and Contributors.
# All Rights Reserved.
#
# This software is subject to the provisions of the Zope Public License,
# Version 2.1 (ZPL).  A copy of the ZPL should accompany this distribution.
# THIS SOFTWARE IS PROVIDED "AS IS" AND ANY AND ALL EXPRESS OR IMPLIED
# WARRANTIES ARE DISCLAIMED, INCLUDING, BUT NOT LIMITED TO, THE IMPLIED
# WARRANTIES OF TITLE, MERCHANTABILITY, AGAINST INFRINGEMENT, AND FITNESS
# FOR A PARTICULAR PURPOSE.
#
##############################################################################
""" zojax.principal.openid interfaces

$Id$
"""
from zope import interface, schema
from zope.i18nmessageid.message import MessageFactory
from zope.app.authentication.interfaces import IPrincipalInfo
from zope.app.authentication.interfaces import IAuthenticatorPlugin

_ = MessageFactory("zojax.principal.openid")


class IOpenIdPrincipal(interface.Interface):
    """ openid principal """

    title = schema.TextLine(
        title = _('Title'),
        required = True)

    identifier = interface.Attribute('OpenID Identifier')


class IOpenIdPrincipalInfo(IPrincipalInfo):
    """ principal info """


class IOpenIdPrincipalMarker(interface.Interface):
    """ openId principal marker """


class IOpenIdAuthenticator(interface.Interface):

    store = interface.Attribute(u"store")

    def getPrincipalByOpenIdIdentifier(identifier):
        """ Get principal id by her OpenID identifier. Return None if
        principal with given identifier does not exist. """


class IOpenIdCredentials(interface.Interface):
    """ open id credentials info """

    request = interface.Attribute(u"request")

    failed = interface.Attribute(u'Credentials failed')

    principalInfo = interface.Attribute('Principal info')

    parameters = schema.Dict(title=_(u"Query parameters"))


class IOpenIdUsersPlugin(IOpenIdAuthenticator, IAuthenticatorPlugin):
    """A container that contains openid principals."""

    title = schema.TextLine(
        title = _('Title'),
        required = False)

    prefix = schema.TextLine(
        title=_("Prefix"),
        description=_("Prefix to be added to all principal ids to assure "
                      "that all ids are unique within the authentication service"),
        missing_value=u"",
        default=u'',
        readonly=True)

    def getPrincipalByLogin(login):
        """ return principal info by login """
