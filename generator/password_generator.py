from input.cli_input import get_user_info

def generate_passwords(profile):
    """
    Generate common password patterns using personal information.

    This function creates a variety of password combinations based on a user's
    provided profile data, such as first name, last name, nickname, birth year,
    hobby, and company. It simulates how predictable passwords are often formed
    from personal info, helping demonstrate weak password practices.

    The function builds combinations using:
        - Names and years (e.g., "john1999", "jdoe2000")
        - Separators like !, @, _, ., and #
        - Common numeric suffixes (e.g., 1, 12, 123, 1234, 007, 2025)
        - Mixed terms including hobbies and companies (e.g., "john_soccer", "jane@google")

    Args:
        profile (dict): A dictionary containing user profile fields:
            {
                'first': str,   # First name or 'null'
                'last': str,    # Last name or 'null'
                'nick': str,    # Nickname or 'null'
                'year': str,    # Birth year or 'null'
                'hobby': str,   # Hobby or 'null'
                'company': str  # Company or 'null'
            }

    Returns:
        list: A sorted list of unique password strings based on the given inputs.

    Example:
        >>> profile = {
        ...     "first": "John",
        ...     "last": "Smith",
        ...     "nick": "Johnny",
        ...     "year": "1999",
        ...     "hobby": "soccer",
        ...     "company": "Google"
        ... }
        >>> generate_passwords(profile)
        ['google123', 'john1999', 'john!smith', 'johnsoccer', 'johnny007', ...]
    """
    
    first_name = profile["first"].lower()
    last_name = profile["last"].lower()
    nickname = profile["nick"].lower()
    birth_year = profile["year"].lower()
    hobby = profile["hobby"].lower()
    company = profile["company"].lower()
    
    passwords = []
    
    # --- Year-based patterns ---
    if first_name and birth_year:
        first_name_birth_year = first_name + birth_year
        passwords.append(first_name_birth_year)
        
        last_name_birth_year = last_name + birth_year
        passwords.append(last_name_birth_year)
        
        nickname_birth_year = nickname + birth_year
        passwords.append(nickname_birth_year)
        
        first_initial_last_name_birth_year = first_name[0] + last_name + birth_year
        passwords.append(first_initial_last_name_birth_year)
        
        first_name_last_initial_birth_year = first_name + last_name[0] + birth_year
        passwords.append(first_name_last_initial_birth_year)
        
    # --- Company and hobby patterns ---
    if first_name and last_name and company:
        first_name_last_name = first_name + "!" + last_name
        passwords.append(first_name_last_name)
        
        first_name_last_name = first_name + "@" + last_name
        passwords.append(first_name_last_name)
        
        nickname_company = nickname + "#" + company
        passwords.append(nickname_company)
        
        first_name_hobby = first_name + "_" + hobby
        passwords.append(first_name_hobby)
        
        last_name_first_name = last_name + "." + first_name
        passwords.append(last_name_first_name)
    
    # --- Mixed + numeric variations ---
    if first_name and hobby and nickname and company and birth_year:
        first_name_hobby = first_name + hobby
        passwords.append(first_name_hobby)
        
        first_name_exclaim = first_name + "!"
        passwords.append(first_name_exclaim)
        
        first_name_1 = first_name + "1"
        passwords.append(first_name_1)
        
        first_name_12 = first_name + "12"
        passwords.append(first_name_12)
        
        first_name_123 = first_name + "123"
        passwords.append(first_name_123)
        
        first_name_1234 = first_name + "1234"
        passwords.append(first_name_1234)
        
        first_name_hobby_123 = first_name + hobby + "123"
        passwords.append(first_name_hobby_123)
        
        nickname_hobby = nickname + hobby + "!"
        passwords.append(nickname_hobby)
        
        first_name_company_2025 = first_name + company + "2025"
        passwords.append(first_name_company_2025)
        
        first_name_hobby_birth_year = first_name + hobby + birth_year
        passwords.append(first_name_hobby_birth_year)
        
        nickname_007 = nickname + "007"
        passwords.append(nickname_007)
        
        company_123 = company + "123"
        passwords.append(company_123)
        
        nickname_123 = nickname + "123"
        passwords.append(nickname_123)
        
        nickname_exclaim = nickname + "!"
        passwords.append(nickname_exclaim)
        
        first_name_company = first_name + "@" + company
        passwords.append(first_name_company)

    passwords = sorted(list(set(passwords)))
    return passwords

if __name__ == "__main__":
    profile = get_user_info()
    passwords = generate_passwords(profile)
    print(passwords)
        
        
        
        
    
    
    