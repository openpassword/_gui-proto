from nose.tools import *
import os
import openpassword


class AgileKeychainTest:
    def setUp(self):
        current_path = os.path.dirname(os.path.realpath(__file__))
        fixture_path = current_path + '/../../../fixtures/test.agilekeychain'

        self.keychain = openpassword.AgileKeychain(fixture_path)

    def test_unlock_and_get_item_by_unique_id(self):
        self.keychain.unlock("masterpassword123")
        item = self.keychain.get_item_by_unique_id("97019BEBCF9E402F8F0C033474B1B85D")

        eq_(item.data["fields"][0]["value"], "somedifferentusername")
        eq_(item.data["fields"][1]["value"], "password123")
