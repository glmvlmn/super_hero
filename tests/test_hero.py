import allure

from utils.api.api import Check
from utils.load.set_options import Find_hero


@allure.tag("API")
def test_hero():
    Find_hero.find_hero()
    Check.hero()

