import unittest

from app.models import User


class MyTestCase(unittest.TestCase):
    def test_something(self):
        self.assertEqual(True, False)  # add assertion here


    # We create a setUp method that creates an instance of our User class we then pass in the password property.
    def setUp(self):
        self.new_user = User(username="theuser", email="theuser@users.com", profile_pic_path="no_path", pass_secure="password", password='banana')

    # We then create a testcase test_password_setter this ascertains that when password is being hashed and the pass_secure contains a value.
    def test_password_setter(self):
        self.assertTrue(self.new_user.pass_secure is not None)

    # The second taste case confirms that our application raises an AttributeError when we try and access the password property
    def test_no_access_password(self):
        with self.assertRaises(AttributeError):
            self.new_user.password

    # The third test confirms that our password_hash can be verified when we pass in the correct password.
    def test_password_verification(self):
        self.assertTrue(self.new_user.verify_password("banana"))



if __name__ == '__main__':
    unittest.main()
