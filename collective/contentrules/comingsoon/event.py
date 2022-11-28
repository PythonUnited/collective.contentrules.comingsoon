from zope.interface import implementer
from zope.interface.interfaces import ObjectEvent
from collective.contentrules.comingsoon.interfaces import IComingSoon


@implementer(IComingSoon)
class ComingSoonEvent(ObjectEvent):
    """Zope Event to be notified when a plone content
       refers to a date that is coming soon.
    """

    pass
