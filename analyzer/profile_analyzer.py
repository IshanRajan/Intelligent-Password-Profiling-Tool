import re

def has_uppercase_loop(password):
    """
    Check if a password contains uppercase letters.

    Returns:
        True  -> password has some uppercase letters
        False -> password has none
        "all letters are capitalize" -> every letter is uppercase
    """
    
    length_password = len(password)
    count = 0
    for char in password:
        if char.isupper():
            count += 1
                
        else:
            pass
            
    if length_password == count:
        return "all letters are capitalize"
            
    elif count == 0:    
        return False
            
    else:
        return True

def contains_number_loop(password):
    """
    Check if a password contains numbers.

    Returns:
        True  -> password has some digits
        False -> password has none
        "password contains only numbers" -> all characters are digits
    """
    
    length_password = len(password)
    count = 0
    for char in password:
        if char.isdigit():
            count += 1
                
        else:
            pass
            
    if length_password == count:
        return "password contains only numbers"
            
    elif count == 0:
        return False
            
    else:
        return True

def contains_special_chars_regex(password):
    """
    Check if a password contains special characters.

    Returns:
        True  -> some special characters present
        False -> none present
        "password contains only special characters" -> every character is special
    """
    
    length_password = len(password)
    count = 0
    for char in password:
        # Matches any character that is NOT a letter (a-z, A-Z), digit (0-9), or space
        if re.search(r'[^a-zA-Z0-9]', char):
            count += 1

    if length_password == count:
        return "password contains only special characters"
            
    elif count == 0:
        return False
            
    else:
        return True

def profile_analyzer(usernames,usernames_variations, generated_passwords, profile):
    """
    Analyze generated passwords based on personal information and strength rules.

    Rules:
        - If a password contains personal info (first name, last name, nickname,
          birth year, hobby, company), it is automatically weak.
        - If a password contains a username or username variation, it is automatically weak.
        - Otherwise, the password is scored based on:
              length, uppercase letters, numbers, special characters,
              and penalties for predictable sequences.
        - Passwords are categorized into:
              weak, medium, strong, very strong.

    Args:
        usernames (list): direct usernames to check against
        usernames_variations (list): modified versions of usernames
        generated_passwords (list): passwords to evaluate
        profile (dict): contains 'first', 'last', 'nick', 'year', 'hobby', 'company'

    Returns:
        tuple of 4 lists: (weak, medium, strong, very strong)
    """
    
    # Normalize all input values to lowercase for consistency
    first_name = profile["first"].lower()
    last_name = profile["last"].lower()
    nickname = profile["nick"].lower()
    birth_year = profile["year"].lower()
    hobby = profile["hobby"].lower()
    company = profile["company"].lower()
    
    weak_passwords = []
    medium_passwords = []
    strong_passwords = []
    very_strong_passwords = []
    
    # Check each password the user generated
    for password in generated_passwords:
        password_score = 0
        username_found = False
        
        # If the password contains personal info (name, nickname, birth year, etc.)
        # it is automatically considered weak. No scoring is done.
        if any(x and x.lower() in password.lower()
            for x in [first_name, last_name, nickname, birth_year, hobby, company]):
                weak_passwords.append(password)
                continue
        
         # If any username appears in the password, it's immediately weak.
        for username in usernames:
            if username.lower() in password.lower():
                weak_passwords.append(password)
                username_found = True
                break
        
        if username_found:
            continue
        
        # Same idea, but checking username variations
        for username in usernames_variations:
            if username.lower() in password.lower():
                weak_passwords.append(password)
                username_found = True
                break
            
        if username_found:
            continue
        
        # Score based on password length
        if len(password) > 12:
            password_score += 2
        
        elif 8<=len(password)<=12:
            password_score += 1
        
        else:
            password_score += 0
        
        # Evaluate character types (uppercase, numbers, special chars)
        uppercase_status = has_uppercase_loop(password)
        number_status = contains_number_loop(password)
        special_status = contains_special_chars_regex(password)
        
        # Uppercase scoring:
        # +2 if the password has mixed cases
        # +1 if all letters are uppercase (less ideal but still strong)    
        if uppercase_status == True:
            password_score += 2
        
        elif uppercase_status == "all letters are capitalize":
            password_score += 1
        
        else:
            password_score += 0
        
        # Number scoring:
        # +2 if it contains at least one number
        # 0 if it's all digits or has no digits
        if number_status == True:
            password_score += 2
        
        elif number_status == "password contains only numbers":
            password_score += 0
        
        else:
            password_score += 0
        
        # Special character scoring:
        # +2 if it contains special characters
        if special_status == True:
            password_score += 2
        
        elif special_status == False:
            password_score += 0
        
        else:
            password_score += 0
        
        # Penalize common weak patterns
        if "aaaaa" in password:
            password_score -= 1
        
        if "12345" in password:
            password_score -= 1
        
        if "abcd" in password:
            password_score -= 1
        
        # Sort passwords into categories based on score
        if password_score <= 2:
            weak_passwords.append(password)
        
        elif 3 <= password_score <= 5:
            medium_passwords.append(password)
        
        elif 6 <= password_score <= 8:
            strong_passwords.append(password)
        
        else:
            very_strong_passwords.append(password)
    
    # Remove duplicates and sort results
    weak_passwords = sorted(list(set(weak_passwords)))
    medium_passwords = sorted(list(set(medium_passwords)))
    strong_passwords = sorted(list(set(strong_passwords)))
    very_strong_passwords = sorted(list(set(very_strong_passwords)))
    
    return weak_passwords, medium_passwords, strong_passwords, very_strong_passwords
        

        
            
            
            
        
        
            
        
        
        
        
        
        
            
            
        
        
        
        
        
            
        
        
            
        
    