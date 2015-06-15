from opencog.type_constructors import types
from blender_b.chooser.base_chooser import BaseChooser
from util_b.blending_util import sti_value_dict
from util_b.general_util import BlAtomConfig

__author__ = 'DongMin Kim'


class ChooseInSTIRange(BaseChooser):
    def __init__(self, atomspace):
        super(self.__class__, self).__init__(atomspace)

    def __str__(self):
        return self.__class__.__name__

    def make_default_config(self):
        super(self.__class__, self).make_default_config()
        BlAtomConfig().update(self.a, "choose-sti-min", "IMPORTANT")
        BlAtomConfig().update(self.a, "choose-sti-max", "NONE")

    def __get_atoms_in_sti_range(
            self, focus_atoms, atom_type, least_count, sti_min, sti_max
    ):
        """
        Choose atoms within proper STI range.
        :param Type atom_type: type of atoms to choose.
        :param int least_count: minimum number of atoms to choose.
        :param float sti_min: min value of sti to choose.
        :param float sti_max: max value of sti to choose.
        """
        atoms = self.a.get_atoms_by_av(sti_min, sti_max)

        if len(atoms) < least_count:
            self.last_status = self.Status.NOT_ENOUGH_ATOMS
            raise UserWarning('Size of atom list is too small.')

        self.ret = filter(lambda atom: atom.is_a(atom_type), atoms)
        if len(self.ret) < least_count:
            self.last_status = self.Status.NOT_ENOUGH_ATOMS
            raise UserWarning('Size of atom list is too small.')

    def atom_choose_impl(self, focus_atoms, config_base):
        atom_type = BlAtomConfig().get_str(self.a, "choose-atom-type", config_base)
        least_count = BlAtomConfig().get_int(self.a, "choose-least-count", config_base)
        sti_min = BlAtomConfig().get_str(self.a, "choose-sti-min", config_base)
        sti_max = BlAtomConfig().get_str(self.a, "choose-sti-max", config_base)

        try:
            atom_type = types.__dict__[atom_type]
        except KeyError:
            atom_type = types.Node
        try:
            least_count = int(least_count)
            if least_count < 0:
                raise ValueError('Least count of atom list is too small.')
        except (TypeError, ValueError):
            least_count = 0
        try:
            sti_min = sti_value_dict[sti_min]
            sti_min = int(sti_min)
        except (KeyError, TypeError):
            sti_min = 1
        try:
            sti_max = sti_value_dict[sti_max]
        except KeyError:
            sti_max = None

        return self.__get_atoms_in_sti_range(
            focus_atoms, atom_type, least_count, sti_min, sti_max
        )
