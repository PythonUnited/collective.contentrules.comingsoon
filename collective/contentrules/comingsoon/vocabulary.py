from zope.schema.interfaces import IVocabularyFactory
from zope.schema.vocabulary import SimpleVocabulary
from zope.interface import implementer


@implementer(IVocabularyFactory)
class DelayVocabulary(object):
    """Vocabulary for delay - integers between 0 and 31"""
    #xrok.name("DelayVocabulary")

    def __call__(self, context):
        l = range(0, 32)
        items = zip(l, l)
        return SimpleVocabulary.fromItems(items)

DelayVocabularyFactory = DelayVocabulary()

