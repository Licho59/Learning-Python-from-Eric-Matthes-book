import unittest
from country_codes import get_country_code

class CodesTestCase(unittest.TestCase):
    """Test dla programu 'country_code.py"""

    def test_country_code(self):
        """Czy dane w postaci 'pl' są obsługiwane prawidłowo?"""
        code = get_country_code('Ukraine')
        self.assertEqual(code, 'ua')

unittest.main()