from formatter import MyFormatter
from logging import Logger, StreamHandler
import sys

logger = Logger("logger_name")

handler = StreamHandler(sys.stdout)
myformatter = MyFormatter()
handler.setFormatter(myformatter)

logger.addHandler(handler)


class Bid2(object):
    """
    """
    def bla(self):
        pass


class Bidon(object):

#    print """
#    >>> from bidon import Bidon
#    [Bidon] coucou
#    """
#    # basse prio
#    logger.warning("coucou")

    def __init__(self):
        print """==============================
>>> b = Bidon()
[Bidon] coucou
=============="""
        logger.warning("coucou")

    @classmethod
    def methode_bla(cls):
        print """==============================
>>> Bidon.methode_bla()
[Bidon] coucou
=============="""
        logger.warning("coucou")

    @staticmethod
    def methode_blaba():
        print """==============================
>>> Bidon.methode_blaba()
[Bidon] coucou
=============="""
        # basse prio
        logger.warning("coucou")


def pouet():
    print """==============================
>>> pouet()
[pouet] coucou
=============="""
    logger.warning("coucou")
