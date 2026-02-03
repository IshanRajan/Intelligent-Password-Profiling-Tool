#enjoy


class InputError(Exception):
    """Exception for user input errors."""
    pass


def get_user_info():
    """
    Collects user profile information with validation and consent.
    
    Returns:
        dict: Profile information with keys: first, last, nick, year, hobby, company
        
    Raises:
        InputError: If consent is not provided
        KeyboardInterrupt: If user cancels (Ctrl+C)
    """
    print("\n" + "="*50)
    print("PASSWORD PROFILING TOOL - CONSENT REQUIRED")
    print("="*50)
    print("This tool demonstrates how personal information")
    print("can be used to generate predictable credentials.")
    print("\nIMPORTANT: Only use with your own data or")
    print("data you have explicit permission to analyze.")
    print("="*50 + "\n")
    
    try:
        consent = input("Type 'I CONSENT' to continue: ").strip()
        
        if consent != "I CONSENT":
            raise InputError("Consent not provided. Cannot proceed.")
        
        print("\nConsent confirmed. Please provide profile information.")
        print("(Enter 'null' for any field you want to skip)\n")
        
        # Collect profile fields with validation
        first_name = input("First name: ").strip() or "null"
        last_name = input("Last name: ").strip() or "null"
        nickname = input("Nickname: ").strip() or "null"
        
        # Validate birth year
        while True:
            birth_year = input("Birth year (4 digits or 'null'): ").strip()
            if birth_year.lower() == "null":
                break
            if birth_year.isdigit() and len(birth_year) == 4:
                break
            print("  Invalid year. Enter 4 digits or 'null'")
        
        hobby = input("Hobby: ").strip() or "null"
        company = input("Company: ").strip() or "null"
        
        user_info = {
            "first": first_name,
            "last": last_name,
            "nick": nickname,
            "year": birth_year,
            "hobby": hobby,
            "company": company
        }
        
        # Confirm entered information
        print("\n" + "-"*50)
        print("Profile Summary:")
        for key, value in user_info.items():
            print(f"  {key.capitalize()}: {value}")
        print("-"*50 + "\n")
        
        return user_info
        
    except EOFError:
        raise KeyboardInterrupt("Input cancelled (EOF)")
    except KeyboardInterrupt:
        print("\nInput cancelled by user")
        raise


if __name__ == "__main__":
    try:
        profile = get_user_info()
        print("Profile created successfully!")
    except InputError as e:
        print(f"ERROR: {e}")
    except KeyboardInterrupt:
        print("\nGoodbye!")