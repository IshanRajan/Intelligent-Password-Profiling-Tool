import re

def has_uppercase_loop(password):
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
    
    for password in generated_passwords:
        password_score = 0
        
        if first_name in password:
            weak_passwords.append(password)
        
        if last_name in password:
            weak_passwords.append(password)
        
        if birth_year in password:
            weak_passwords.append(password)
        
        if company in password:
            weak_passwords.append(password)
        
        if hobby in password:
            weak_passwords.append(password)
        
        if nickname in password:
            weak_passwords.append(password)
        
        for username in usernames:
            if username.lower() in password.lower():
                weak_passwords.append(password)
        
        for username in usernames_variations:
            if username.lower() in password.lower():
                weak_passwords.append(password)
        
        if len(password) > 12:
            password_score += 2
        
        elif 8<=len(password)<=12:
            password_score += 1
        
        else:
            password_score += 0
            
        if has_uppercase_loop(password) == True:
            password_score += 2
        
        elif has_uppercase_loop(password) == "all letters are capitalize":
            password_score += 1
        
        else:
            password_score += 0
            
        if contains_number_loop(password) == True:
            password_score += 2
        
        elif contains_number_loop(password) == "password contains only numbers":
            password_score += 0
        
        else:
            password_score += 0
        
        if contains_special_chars_regex(password) == True:
            password_score += 2
        
        elif contains_special_chars_regex(password) == False:
            password_score += 0
        
        else:
            password_score += 0
        
        if "aaaaa" in password:
            password_score -= 1
        
        if "12345" in password:
            password_score -= 1
        
        if "abcd" in password:
            password_score -= 1
        
        if password_score <= 2:
            weak_passwords.append(password)
        
        elif 3 <= password_score <= 5:
            medium_passwords.append(password)
        
        elif 7 <= password_score <= 10:
            strong_passwords.append(password)
        
        else:
            very_strong_passwords.append(password)
        
        weak_passwords = sorted(list(set(weak_passwords)))
        medium_passwords = sorted(list(set(medium_passwords)))
        strong_passwords = sorted(list(set(strong_passwords)))
        very_strong_passwords = sorted(list(set(very_strong_passwords)))
    
    return weak_passwords, medium_passwords, strong_passwords, very_strong_passwords
        

        
            
            
            
        
        
            
        
        
        
        
        
        
            
            
        
        
        
        
        
            
        
        
            
        
    