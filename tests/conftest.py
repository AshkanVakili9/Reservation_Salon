from pytest_factoryboy import register


from .factories import *


register(UserFactory)
register(SmsFactory)
