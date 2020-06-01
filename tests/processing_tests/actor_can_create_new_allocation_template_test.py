import allure
import pytest
from base.utils.utils import Utils
from base_config import BaseConfig

test_case = "TestActorCreatingNewTemplate"
location_percentage = 0.23
template_name = "New_Template"


@pytest.mark.incremental
@allure.title(test_case)
@allure.description("""
    Functional tests.
    1. Check that actor have default fund and able to allocate it.
    2. Check that actor can create new allocation template.
    3. Check that actor can enter percentage allocations, validate it and choose remaining.
    """)
@allure.severity(allure.severity_level.BLOCKER)
@allure.testcase(BaseConfig.GITHUB_URL + "processing_tests/actor_can_create_new_allocation_template_test.py",
                 "TestActorCreatingNewTemplate")
@pytest.mark.regression
class TestActorCreatingNewTemplate(object):
    funds, template = None, None

    def test_actor_can_select_funds(self, actor):
        assert actor.if_logged()
        TestActorCreatingNewTemplate.funds = actor.client.get_client_funds()
        assert len(actor.client.get_client_funds()) > 0, "Default fund wasn't be created."

    def test_create_new_template(self, actor):
        TestActorCreatingNewTemplate.template = actor.create_new_allocation_template(template_name)
        assert len(actor.client.get_client_funds()) > 1, "Default fund wasn't be created."

    def test_actor_enter_percentage_allocations(self, actor):
        fund_name = actor.client.default_fund.get_name()
        fund = actor.client.get_fund_by_name(fund_name)
        TestActorCreatingNewTemplate.funds = actor.enter_percentage_value(fund, location_percentage)

        assert Utils.validate_percentage(fund.quantity_allocated, fund.quantity_unallocated)
