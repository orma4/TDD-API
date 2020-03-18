from CalenderJ import *


def close_program():
    print("Program shut down")
    exit(0)


def activate_fasting_dates():
    CalenderJ.print_fasts_input()


def activate_conversion():
    CalenderJ.convert_input()


def activate_all_events():
    CalenderJ.set_date_input()


def main():
    while True:
        print("""
1. Check jewish fasting on specific dates
2. Convert Jewish date to Georgian date
3. Check all events in a specific dates
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
