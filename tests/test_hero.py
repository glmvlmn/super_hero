import allure

from utils.api.apy import Check
from utils.load.set_options import Find_hero


@allure.feature("Hero")
@allure.description("Api")
def test_hero():
    Find_hero.find_hero()
    Check.hero()

