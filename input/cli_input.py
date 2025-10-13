# This script runs at the start of the program.
# It collects user profile information with consent to prepare data
# for generating potential usernames and passwords.

def get_user_info():
    """
    Collects basic user profile information via CLI input with an explicit consent check.

    The function first requires the user to type 'I CONSENT' to confirm ethical use.
    If consent is not given, the program exits immediately.
    Once consent is provided, the function prompts for optional profile fields:
    - First name
    - Last name
    - Nickname
    - Birth year
    - Hobby
    - Company/organization

    Each field can be filled with real or synthetic data, or 'null' if not applicable.
    The collected data is returned as a dictionary for use in username and password generation.

    Returns:
        dict: A dictionary containing the collected user profile information with keys:
              'first', 'last', 'nick', 'year', 'hobby', 'company'.

    Example:
        >>> profile = get_user_info()
        Please type 'I CONSENT' to use this tool: I CONSENT
        Input the first name (or 'null' if none): John
        Input the last name (or 'null' if none): Smith
        Input the nickname (or 'null' if none): Johnny
        Input the birth_year (or 'null' if none): 1990
        Input the hobby (or 'null' if none): soccer
        Input the company (or 'null' if none): AcmeCorp
        >>> print(profile)
        {
            'first': 'John',
            'last': 'Smith',
            'nick': 'Johnny',
            'year': '1990',
            'hobby': 'soccer',
            'company': 'AcmeCorp'
        }
    """
    
    consent = input("Please type 'I CONSENT' to use this tool: ")
    if consent != "I CONSENT":
        print("Consent not provided. Exiting program.")
        exit()

    first_name = input("Input the first name (or 'null' if none): ").strip()
    last_name = input("Input the last name (or 'null' if none): ").strip()
    nickname = input("Input the nickname (or 'null' if none): ").strip()
    birth_year = input("Input the birth_year (or 'null' if none): ").strip()
    hobby = input("Input the hobby (or 'null' if none): ").strip()
    company = input("Input the company (or 'null' if none): ").strip()
    user_info = {
    "first": first_name,
    "last": last_name,
    "nick": nickname,
    "year": birth_year,
    "hobby": hobby,
    "company": company
        }
    return user_info
