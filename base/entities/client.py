from base.entities.allocation_template import AllocationTemplate
from base.entities.fund import Fund
from base.utils.utils import Utils


class Client(AllocationTemplate):
    def __init__(self):
        super().__init__()
        self.client_funds = list()
        self.select_fund(self.default_fund)

    def set_allocation(self, fund, allocation_percentage):
        err = 'The allocation percentage is reached the gap.'
        self.logger.info(f"Given percentage is: {allocation_percentage} ")
        if [char for char in str(allocation_percentage).split(".")[1]].__len__() <= 5:
            fund.quantity_allocated = allocation_percentage
            fund.quantity_unallocated = 100.0 - allocation_percentage
            self.select_fund(fund)
        else:
            self.logger.exception(f"{err}")
            raise Exception(F"{err}")

    def create_new_template(self, template_name):
        new_template = Utils.adjust_template(AllocationTemplate().set_name(template_name))
        self.logger.info(f"New Template: {new_template}")
        self.select_fund(new_template.default_fund)
        return new_template

    def select_fund(self, fund: Fund):
        if isinstance(fund, Fund):
            self.client_funds.append(fund)
        return self

    def get_client_funds(self):
        if self.get_status() == "Enabled":
            self.logger.info(f"Client funds is : {self.client_funds} ")
            return self.client_funds if len(self.client_funds) != 0 else None

    def get_fund_by_name(self, fund_name):
        if self.get_status() == "Enabled":
            return [f for f in self.get_client_funds() if f.get_name() == fund_name].__getitem__(0)
