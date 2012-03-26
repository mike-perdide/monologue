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

    # basse prio
    logger.warning("coucou")

    def __init__(self):
        print """==============================
>>> b = Bidon()
[Bidon] coucou
=============="""
        logger.warning("coucou")

    @classmethod
    def class_method(cls):
        print """==============================
>>> Bidon.class_method()
[Bidon] coucou
=============="""
        logger.warning("coucou")

    @staticmethod
    def static_method():
        print """==============================
>>> Bidon.static_method()
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
