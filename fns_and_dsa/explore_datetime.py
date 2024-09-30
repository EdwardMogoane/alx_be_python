
from datetime import datetime, timedelta

def display_current_datetime():
    # Get current date and time
    current_date = datetime.now()
    
    # Format and print current date and time
    print("Current date and time:", current_date.strftime("%Y-%m-%d %H:%M:%S"))

def calculate_future_date():
    # Prompt user for number of days to add
    days_to_add = int(input("Enter the number of days to add to the current date: "))
    
    # Calculate future date
    current_date = datetime.now()
    future_date = current_date + timedelta(days=days_to_add)
    
    # Print future date
    print("Future date:", future_date.strftime("%Y-%m-%d"))

def main():
    display_current_datetime()
    calculate_future_date()

if __name__ == "__main__":
    main()

