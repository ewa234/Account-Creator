import unittest
from Account_Creator import generateUsername
from Account_Creator import calculateYearGroup
from Account_Creator import isPasswordSecure

class TestGenerateUsername(unittest.TestCase):
    def test_username_01(self):
        username = generateUsername("Ronald Smith", "2022")
        self.assertEqual(username, "22SmithR", "username incorrect")
        
class TestCalculateYearGroup(unittest.TestCase):
    def test_year_group_01(self):
        yearGroup = calculateYearGroup("22smithR")
        self.assertEqual(yearGroup,"Year 9", "year group incorrect")

class TestIsPasswordSecure(unittest.TestCase):
    def test_is_password_secure_01(self):
        password = "password"
        isSecure = isPasswordSecure(password)
        self.assertEqual(isSecure,False, "password security incorrect")

if __name__ == "__main__":
    unittest.main()