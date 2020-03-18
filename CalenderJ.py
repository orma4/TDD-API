import requests


class CalenderJ:
    """
     API: https://www.hebcal.com/home/195/jewish-calendar-rest-api
          https://www.hebcal.com/home/219/hebrew-date-converter-rest-api
     """

    @staticmethod
    def holidays_by_date(month, year):
        api_result = requests.get(
            "https://www.hebcal.com/hebcal/?v=1&cfg=json&maj=on&min=on&mod=on&nx=on&year={0}&month={"
            "1}&ss=on&mf=on&c=on&geo={2}&m=0&s=on".format(year, month, "none"))
        api_response = api_result.json()
        return api_response['items']

    @staticmethod
    def set_date(month, year):
        list = []
        print_text = CalenderJ.holidays_by_date(month, year)
        for item in print_text:
            print(item['date'], item['title'])
            list.append(item['date'])
            list.append(item['title'])
        return list

    @staticmethod
    def set_date_input():
        year = input("enter a year or write now for current year:")
        month = input("enter a month or write x for all months :")
        CalenderJ.set_date(month, year)

    @staticmethod
    def conversion_output(heb_year, heb_month, heb_day):
        api_result = requests.get(
            "https://www.hebcal.com/converter/?cfg=json&hy={0}&hm={1}&hd={2}&h2g=1".format(heb_year, heb_month,
                                                                                           heb_day))
        conversion = api_result.json()
        print("\nYear:", conversion['gy'], "\nMonth:", conversion['gm'], "\nDay:", conversion['gd'])
        list = [conversion['gy'], conversion['gm'], conversion['gd']]
        return list

    @staticmethod
    def convert_input():
        heb_year = input("Enter Hebrew year:")
        heb_month = input(
            "Enter Hebrew month (Nisan, Iyyar, Sivan, Tamuz, Av, Elul, Tishrei, Cheshvan, Kislev, Tevet, Shvat, "
            "Adar1, Adar2):")
        heb_day = input("Enter Hebrew day:")
        CalenderJ.conversion_output(heb_year, heb_month, heb_day)

    @staticmethod
    def fasting_dates(month, year):
        api_result = requests.get(
            "https://www.hebcal.com/hebcal/?v=1&cfg=json&maj=on&min=on&mod=off&nx=off&year={1}&month={"
            "0}&ss=off&mf=on&c=off&geo=none&m=0&s=off".format(month, year))
        api_response = api_result.json()
        return api_response['items']

    @staticmethod
    def print_fasts(month, year):
        list = CalenderJ.fasting_dates(month, year)
        test_list = []
        for item in list:
            if 'subcat' in item.keys():
                if (item['subcat'] == "fast") or (item['memo'] == "Day of Atonement") or (
                        item['title'] == "Tish'a B'Av"):
                    print(item['date'], item['title'])
                    test_list.append(item['date'])
                    test_list.append(item['title'])
        return test_list

    @staticmethod
    def print_fasts_input():
        year = input("Enter a year (now = current year): ")
        month = input("Enter a month (x = all months):")
        CalenderJ.print_fasts(month, year)
