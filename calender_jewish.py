"""
     Or Maman - 311392450
     """
import requests


class calender_jewish:
    """
         API: https://www.hebcal.com/home/195/jewish-calendar-rest-api
              https://www.hebcal.com/home/219/hebrew-date-converter-rest-api
    """

    @staticmethod
    def holidays_by_date(month, year):
        """
        Check all events in a specific dates
        """
        api_result = requests.get(
            "https://www.hebcal.com/hebcal/?v=1&cfg=json&maj=on&min=on&mod=on&nx=on&year={0}&month="
            "{""1}&ss=on&mf=on&c=on&geo={2}&m=0&s=on".format(year, month, "none"))
        api_response = api_result.json()
        return api_response['items']

    @staticmethod
    def set_date(month, year):
        """
        Check all events in a specific dates
        """
        my_list = []
        print_text = calender_jewish.holidays_by_date(month, year)
        for item in print_text:
            print(item['date'], item['title'])
            my_list.append(item['date'])
            my_list.append(item['title'])
        return my_list

    @staticmethod
    def set_date_input():
        """
            set date inputs
        """
        year = input("enter a year or write now for current year:")
        month = input("enter a month or write x for all months :")
        calender_jewish.set_date(month, year)

    @staticmethod
    def conversion_output(heb_year, heb_month, heb_day):
        """
        Convert Jewish date to Georgian date
        """
        api_result = requests.get(
            "https://www.hebcal.com/converter/?cfg=json&hy={0}&hm={1}&hd={2}&h2g=1"
            .format(heb_year, heb_month, heb_day))
        conversion = api_result.json()
        print("\nYear:", conversion['gy'], "\nMonth:", conversion['gm'], "\nDay:", conversion['gd'])
        my_list = [conversion['gy'], conversion['gm'], conversion['gd']]
        return my_list

    @staticmethod
    def convert_input():
        """Convert Jewish date to Georgian date
                       """
        heb_year = input("Enter Hebrew year:")
        heb_month = input(
            "Enter Hebrew month (Nisan, Iyyar, Sivan, Tamuz, Av, Elul, Tishrei, "
            "Cheshvan, Kislev, Tevet, Shvat, " "Adar1, Adar2):")
        heb_day = input("Enter Hebrew day:")
        calender_jewish.conversion_output(heb_year, heb_month, heb_day)

    @staticmethod
    def fasting_dates(month, year):
        """Check jewish fasting on specific dates
                       """
        api_result = requests.get(
            "https://www.hebcal.com/hebcal/?v=1&cfg=json&maj=on&min=on&mod=off&nx=off&year={1}"
            "&month={""0}&ss=off&mf=on&c=off&geo=none&m=0&s=off".format(month, year))
        api_response = api_result.json()
        return api_response['items']

    @staticmethod
    def print_fasts(month, year):
        """
        Check jewish fasting on specific dates
        """
        my_list = calender_jewish.fasting_dates(month, year)
        test_list = []
        for item in my_list:
            if 'subcat' in item.keys():
                if (item['subcat'] == "fast") or (item['memo'] == "Day of Atonement") or (
                        item['title'] == "Tish'a B'Av"):
                    print(item['date'], item['title'])
                    test_list.append(item['date'])
                    test_list.append(item['title'])
        return test_list

    @staticmethod
    def print_fasts_input():
        """
         print fasts inputs
         """
        year = input("Enter a year (now = current year): ")
        month = input("Enter a month (x = all months):")
        calender_jewish.print_fasts(month, year)
