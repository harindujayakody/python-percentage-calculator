import webbrowser
import datetime

def calculate_percentage(value, percentage):
    return (value * percentage) / 100

def display_credits():
    current_year = datetime.datetime.now().year
    print("\n\033[1;35m=================================================")
    print(f"Made with ❤️ by Harindu Jayakody - © {current_year}")
    print("Check out more: [https://codekits.info]")
    print("=================================================\033[0m\n")

def display_hero_section():
    print("\033[1;36m")  # Cyan color for header
    print("=========================================")
    print("    Welcome to the Simple Percentage Calculator    ")
    print("=========================================")
    print("\033[0m")  # Reset to default text color
    print("This calculator helps you to easily find out the percentage of any given number.")
    print("Just enter the value and the percentage you want to calculate, and let the tool do the rest!")
    print("\nGuidelines:")
    print("1. Enter the numeric value you want to find the percentage of.")
    print("2. Enter the percentage value (e.g., for 20%, just enter 20).")
    print("3. The calculator will output the result.")
    display_credits()  # Display credits in the hero section
    print("\033[1;36m=========================================\033[0m\n")  # End with colored line

def open_website():
    webbrowser.open("https://codekits.info")

def main():
    display_hero_section()

    while True:
        try:
            value = float(input("\033[1;33mEnter the value: \033[0m"))  # Yellow color for input prompt
            percentage = float(input("\033[1;33mEnter the percentage: \033[0m"))
            result = calculate_percentage(value, percentage)
            print(f"\033[1;32m{percentage}% of {value} is {result}\033[0m\n")  # Green color for output

            if input("\033[1;35mCalculate another percentage? (yes/no): \033[0m").lower() != 'yes':
                break

        except ValueError:
            print("\033[1;31mPlease enter valid numbers.\033[0m")  # Red color for error message

    if input("Do you want to visit our website? (yes/no): ").lower() == 'yes':
        open_website()

if __name__ == "__main__":
    main()
