"""
     Or Maman - 311392450
     """
import sys

from calender_jewish import calender_jewish


def close_program():
    """
    Close program
    """
    print("Program shut down")
    sys.exit()


def activate_fasting_dates():
    """
        Check jewish fasting on specific dates
        """
    calender_jewish.print_fasts_input()


def activate_conversion():
    """
        Convert Jewish date to Georgian date
        """
    calender_jewish.convert_input()


def activate_all_events():
    """
        Check all events in a specific dates
        """
    calender_jewish.set_date_input()


def main():
    """
    Main menu
    """
    while True:
        print("""
1. Check jewish fasting on specific date
2. Convert Jewish date to Georgian date
3. Check all events in a specific date
4. Close
        """)
        menu_input = input()
        switcher = {
            1: lambda x: activate_fasting_dates(),
            2: lambda x: activate_conversion(),
            3: lambda x: activate_all_events(),
            4: lambda x: close_program(),
        }
        switcher.get(int(menu_input))(0)


if __name__ == "__main__":
    main()
