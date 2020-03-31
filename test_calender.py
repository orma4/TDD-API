"""
Or Maman - 311392450
Testings 4
"""
import unittest
from unittest.mock import patch, MagicMock

from calender_jewish import calender_jewish


class calender_test(unittest.TestCase):
    """
    Test class
    """
    def test_conversion_output_1(self):
        """
        Test 1
        """
        stub_heb_year = 5749
        stub_heb_month = "Kislev"
        stub_heb_day = 25
        expected = [1988, 12, 4]
        result = calender_jewish.conversion_output(stub_heb_year, stub_heb_month, stub_heb_day)
        self.assertEqual(result, expected)

    def test_conversion_output_2(self):
        """
        Test 2
        """
        stub_heb_year = 4000
        stub_heb_month = "Nisan"
        stub_heb_day = 13
        expected = [240, 3, 24]
        result = calender_jewish.conversion_output(stub_heb_year, stub_heb_month, stub_heb_day)
        self.assertEqual(result, expected)

    def test_conversion_output_3(self):
        """
                Test 3
                """
        stub_heb_year = 4400
        stub_heb_month = "Adar1"
        stub_heb_day = 12
        expected = [640, 2, 12]
        result = calender_jewish.conversion_output(stub_heb_year, stub_heb_month, stub_heb_day)
        self.assertEqual(result, expected)

    def test_conversion_output_4(self):
        """
                Test 4
                """
        stub_heb_year = 4500
        stub_heb_month = "Adar2"
        stub_heb_day = 11
        expected = [740, 2, 17]
        result = calender_jewish.conversion_output(stub_heb_year, stub_heb_month, stub_heb_day)
        self.assertEqual(result, expected)

    def test_set_date_1(self):
        """
                Test 5
                """
        stub_month = "1"
        stub_year = "2020"
        result = calender_jewish.set_date(stub_month, stub_year)
        expected = ['2020-01-04', 'Parashat Vayigash', '2020-01-07', "Asara B'Tevet",
                    '2020-01-11', 'Parashat Vayechi',
                    '2020-01-18', "Parashat Shemot", '2020-01-25',
                    'Parashat Vaera', '2020-01-27', "Rosh Chodesh Sh'vat"]
        self.assertEqual(result, expected)

    @patch('calender_jewish.requests.get')
    def test_set_date_2(self, json_mock):
        """
                Test 6
                """
        set_date_data = {"location": {"geo": "none"},
                         "link": "https://www.hebcal.com",
                         "title": "Hebcal November 2011",
                         "date": "2020-03-15T15:44:11-00:00",
                         "items":
                             {"category": "holiday", "hebrew": "בדיקת מוק", "link":
                              "https://www.hebcal.com", "date": "2011-11-11",
                              "title": "testing holiday"}
                         }

        json_mock.return_value = MagicMock(ok=True)
        json_mock.return_value.json.return_value = set_date_data
        print(len(json_mock))
        stub = {"month": 11, "year": 2011}

        expected_item = {"category": "holiday", "hebrew": "בדיקת מוק",
                         "link": "https://www.hebcal.com",
                         "date": "2011-11-11", "title": "testing holiday"}

        date_result = calender_jewish.holidays_by_date(**stub)
        self.assertDictEqual(expected_item, date_result)

    def test_fasting_dates_1(self):
        """
                Test 7
                """
        stub1 = "3"
        stub2 = "2020"
        expected = ["2020-03-09", "Ta'anit Esther"]
        result = calender_jewish.print_fasts(stub1, stub2)
        self.assertEqual(result, expected)

    def test_fasting_dates_2(self):
        """
                Test 8
                """
        stub1 = "1"
        stub2 = "2020"
        expected = ["2020-01-07", "Asara B'Tevet"]
        result = calender_jewish.print_fasts(stub1, stub2)
        self.assertEqual(result, expected)

    def test_fasting_dates_3(self):
        """
                Test 9
                """
        stub1 = "2"
        stub2 = "2020"
        expected = []
        result = calender_jewish.print_fasts(stub1, stub2)
        self.assertEqual(result, expected)

    def test_fasting_dates_4(self):
        """
         Test 10
        """
        stub1 = "4"
        stub2 = "2020"
        expected = ["2020-04-08", "Ta'anit Bechorot"]
        result = calender_jewish.print_fasts(stub1, stub2)
        self.assertEqual(result, expected)


if __name__ == '__main__':
    unittest.main()
