import unittest
from src.account import *
from src.profile import *

class TestAccount(unittest.TestCase):

    def setUp(self):

        # Creating some objects to use in the tests
        self.profile_1 = Profile("harrisonF", "myP@assword")
        self.profile_2 = Profile("markH", "anotherP@ssword")
        self.profile_3 = Profile("xlinkx", "p@ssw0rd")
        self.account_1 = Account("Jane", "Smith", "janes@email.com")
   

    # Test an Account can add a Profile
    def test_add_profile(self):
        # Arrange
        expected = 1
        # Act
        self.account_1.add_profile(self.profile_1)
        actual = len(self.account_1.profiles)
        # Assert
        self.assertEqual(expected, actual)
        

    # Test an Account can remove a given Profile
    def test_remove_profile(self):
        # Arrange
        expected = 0
        # Act
        self.account_1.add_profile(self.profile_1)
        self.account_1.remove_profile(self.profile_1)
        actual = len(self.account_1.profiles)
        # Assert
        self.assertEqual(expected, actual)


    # Test an Account can return a list of Profiles
    def test_get_profiles(self):
        # Arrange
        expected = [self.profile_1, self.profile_2, self.profile_3]
        # Act
        self.account_1.add_profile(self.profile_1)
        self.account_1.add_profile(self.profile_2)
        self.account_1.add_profile(self.profile_3)
        actual = self.account_1.profiles
        # Assert
        self.assertEqual(expected, actual)

   
