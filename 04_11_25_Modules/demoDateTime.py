from datetime import date

def calculate_age(birth_year):
    """Calculate age from birth year"""
    current_year = date.today().year
    print(f"Current Year: {current_year}")
    age = current_year - birth_year
    return age

def days_lived(birth_year):
    """Approximate days lived"""
    age = calculate_age(birth_year)
    return age * 365

def main():
    print("=== Age Calculator ===")
    
    birth_year = int(input("Enter your birth year: "))
    
    age = calculate_age(birth_year)
    days = days_lived(birth_year)
    
    print(f"\nYou are {age} years old")
    print(f"You have lived approximately {days:,} days!")
    
    # Bonus: Calculate weeks
    weeks = days // 7
    print(f"That's about {weeks:,} weeks!")

main()