from blender_b.maker.make_simple import MakeSimple
from util_b.general_util import BlAtomConfig

__author__ = 'DongMin Kim'


class MakerFinder(object):
    def __init__(self, a):
        self.a = a

        self.makers = {
            MakeSimple.__name__: MakeSimple
        }

    def __str__(self):
        return self.__class__.__name__

    def get_maker(self, id_or_name=None):
        if id_or_name is None:
            id_or_name = BlAtomConfig().get_str(self.a, "link-connector")

        maker = self.makers.get(str(id_or_name))
        if maker is not None:
            return maker(self.a)
        else:
            raise UserWarning('Maker not found.')
