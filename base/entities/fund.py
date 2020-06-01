from base.utils.utils import Utils


class Fund:
    def __init__(self, name="Default_Fund"):
        self.name = name
        self.quantity_allocated = 0.0
        self.quantity_unallocated = 100.0

    def get_name(self):
        return self.name

    def set_name(self, name):
        if Utils.validate_text(name):
            self.name = name
            return self

    def __repr__(self):
        return "{}({})".format(self.__class__.__name__,
                               ', '.join("{k}={v}".format(k=k, v=self.__dict__[k])
                                         for k in sorted(self.__dict__.keys())))
