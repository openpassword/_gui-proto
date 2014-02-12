import os
from nose.tools import *
from openpassword.agile_keychain import KeychainItemRepository
from openpassword.exceptions import InvalidPathException


class KeychainItemRepositoryTest:
    def setUp(self):
        current_path = os.path.dirname(os.path.realpath(__file__))
        fixture_path = current_path + '/../../../fixtures/test.agilekeychain'

        self.repository = KeychainItemRepository(fixture_path)

    def it_returns_keychain_item_for_given_unique_id(self):
        item = self.repository.item_by_unique_id('2E21D652E0754BD59F6B94B0323D0142')

        eq_(item.key_id, 'BE4CC37CD7C044E79B5CC1CC19A82A13')

    @raises(InvalidPathException)
    def it_raises_invalidpathexception_for_invalid_item(self):
        item = self.repository.item_by_unique_id('E21D652E0754BD59F6B94B0323D0')

    def it_return_all_items_in_the_keychain(self):
        items = self.repository.all_items()
        eq_(len(items), 9)
