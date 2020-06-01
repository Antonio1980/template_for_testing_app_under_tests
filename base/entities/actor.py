from base.entities.client import Client
from base.stubs import stubs


class Actor:
    def __init__(self, credentials, entry_method=1):
        self.client = Client()
        self.authorized = stubs.get_authorization()
        self.allocation_permissions = True
        self.logged = stubs.login_to_system(credentials)
        if entry_method == 2:
            self.incoming_integration()

    def if_logged(self):
        return self.logged

    def create_new_allocation_template(self, name):
        """
        Creates AllocationTemplate object with default presets.
        :param name: Any str.
        :return: AllocationTemplate object.
        """
        return self.client.create_new_template(name)

    def enter_percentage_value(self, fund, allocation_percentage):
        self.client.set_allocation(fund, allocation_percentage)
        return self.client.get_client_funds()

    def incoming_integration(self):
        """
        It's a stub function:
        Static data integration – preset allocations details
        will be received as part of a static data upload on a scheduled basis.
        :return: AllocationTemplate object.
        """
        preset_allocation = stubs.populate_and_schedule(self.client.create_new_template("Stub"))
        return preset_allocation
