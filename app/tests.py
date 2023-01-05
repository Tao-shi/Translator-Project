'''
This module tests the translation functions from service.py
'''

import unittest
from app.translator import english_to_french, french_to_english


class TestFrenchToEnglish():
    '''
    Tests the french_to_english function
    '''

    def translate(self, text):
        '''
        Runs the translation function
        '''
        return french_to_english(text)

    def test_non_string_input_returns_none(self):
        '''
        Tests for non-string imputs
        :return:
        '''
        assert self.translate(None) is None
        assert self.translate(1) is None
        assert self.translate(1.4) is None

    def test_string_input_converts_to_english(self):
        # Test only string
        assert self.translate("Bonjour") == 'Hello'
        # Test Alphanumeric
        assert self.translate("Bonjour 202") == 'Hello 202'
        # Test Non french words are not converted
        assert self.translate("Bonjour Azeem 202") == 'Hello Azeem 202'
        # Test Non french words are not converted
        assert self.translate("Bonjour ZYZ") == 'Hello ZYZ'


class TestEnglishToFrench:
    '''
    Tests the english_to_french function
    '''
    def translate(self, text):
        '''
        Translates the text
        '''
        return english_to_french(text)

    def test_non_string_input_returns_none(self):
        assert self.translate(None) is None
        assert self.translate(1) is None
        assert self.translate(1.4) is None

    def test_string_input_converts_to_english(self):
        # Test only string
        assert self.translate("Hello") == 'Bonjour'
        # Test Alphanumeric
        assert self.translate("Hello 202") == 'Bonjour 202'
        # Test Non french words are not converted
        assert self.translate("Hello Azeem 202") == 'Bonjour Azeem 202'
        # Test Non french words are not converted
        assert self.translate("Hello ZYZ") == 'Bonjour ZYZ'
