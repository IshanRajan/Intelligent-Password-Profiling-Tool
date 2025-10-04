# This script is used to run the starting of the program, and is meant to get
# data about the user, they want to create potential usernames and passwords



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
        print("Sorry you can't run the program")
        exit()

    first_name = input("Input the first name, if no last name enter null")
    last_name = input("Input the last name, if no last name enter null")
    nickname = input("Input the nickname, if no nickname enter null")
    birth_year = input("Input the birth_year, if no birth_year enter null")
    hobby = input("Input the hobby, if no hobby enter null")
    company = input("Input the company, if no company enter null")
    user_info = {
    "first": first_name,
    "last": last_name,
    "nick": nickname,
    "year": birth_year,
    "hobby": hobby,
    "company": company
        }
    return user_info
