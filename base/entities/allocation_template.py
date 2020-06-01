from base.entities.fund import Fund
from base.stubs import stubs
from base.utils.utils import Utils
from base.utils.temp_logger import TempLogger


class AllocationTemplate:
    def __init__(self, name="Default_Template", status: str = "Enabled", total: float = 100.0):
        self.name = name
        self.status = status
        self.template_id, self.parent_org = None, None
        self.total = total
        self.default_fund = Fund()
        self.logger = TempLogger("Default_Logger").logger

    def set_name(self, name: str):
        try:
            if stubs.check_uniq(name):
                self.name = name
                self.logger.info(f"Template Name is: {self.name}")
                return self
        except Exception as e:
            self.logger.exception(f"{'The name you have specified is already in use'}")
            raise e

    def get_name(self):
        try:
            return self.get_name()
        except Exception as e:
            self.logger.exception(e)
            raise e

    def set_status(self, able: bool):
        self.status = "Enabled" if able else "Disable"
        return self

    def get_status(self):
        self.logger.info(f"Status is {self.status}")
        return self.status

    def get_template_id(self):
        self.logger.info(f"Preset ID is: {self.template_id} ")
        return self.template_id

    def set_id(self, template_id):
        err = 'Text should not be longer than 255 characters'
        if Utils.validate_text(template_id):
            self.template_id = template_id
            self.logger.info(f"Template ID is: {self.template_id}")
            return self
        else:
            self.logger.exception(f"{err}")
            raise Exception(f"{err}")

    def get_parent_org(self):
        self.logger.info(f"Parent Org. is: {self.parent_org} ")
        return self.parent_org

    def set_parent_org(self, parent_org):
        err = 'Text should not be longer than 255 characters'
        if Utils.validate_text(parent_org):
            self.parent_org = parent_org
            self.logger.info(f"Parent Org. is: {self.parent_org} ")
            return self
        else:
            self.logger.exception(f"{err}")
            raise Exception(F"{err}")

    def __repr__(self):
        return "{}({})".format(self.__class__.__name__,
                               ', '.join("{k}={v}".format(k=k, v=self.__dict__[k])
                                         for k in sorted(self.__dict__.keys())))
