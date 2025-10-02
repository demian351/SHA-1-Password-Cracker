import unittest
import password_cracker

class UnitTests(unittest.TestCase):
    
    def test_hash_1(self):
        actual = password_cracker.crack_sha1_hash("b305921a3723cd5d70a375cd21a61e60aabb84ec")
        expected = "sammy123"
        self.assertEqual(actual, expected)
    
    def test_hash_2(self):
        actual = password_cracker.crack_sha1_hash("c7ab388a5ebefbf4d550652f1eb4d833e5316e3e")
        expected = "abacab"
        self.assertEqual(actual, expected)
    
    def test_hash_3(self):
        actual = password_cracker.crack_sha1_hash("5baa61e4c9b93f3f0682250b6cf8331b7ee68fd8")
        expected = "password"
        self.assertEqual(actual, expected)
    
    def test_hash_not_in_database(self):
        actual = password_cracker.crack_sha1_hash("9999999999999999999999999999999999999999")
        expected = "PASSWORD NOT IN DATABASE"
        self.assertEqual(actual, expected)
    
    def test_hash_with_salt_1(self):
        actual = password_cracker.crack_sha1_hash("53d8b3dc9d39f0184144674e310185e41a87ffd5", use_salts=True)
        expected = "superman"
        self.assertEqual(actual, expected)
    
    def test_hash_with_salt_2(self):
        actual = password_cracker.crack_sha1_hash("da5a4e8cf89539e66097acd2f8af128acae2f8ae", use_salts=True)
        expected = "q1w2e3r4t5"
        self.assertEqual(actual, expected)
    
    def test_hash_with_salt_3(self):
        actual = password_cracker.crack_sha1_hash("ea3f62d498e3b98557f9f9cd0d905028b3b019e1", use_salts=True)
        expected = "bubbles1"
        self.assertEqual(actual, expected)

if __name__ == "__main__":
    unittest.main()