
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
        
        for username in usernames:
            if username.lower() in password.lower():
                weak_passwords.append(password)
        
        for username in usernames_variations:
            if username.lower() in password.lower():
                weak_passwords.append(password)
        
        if len(password) > 12:
            password_score = 3
        
        elif 8<=len(password)<=12:
            password_score = 2
        
        else:
            password_score = 1
        
        if 
            
        
        
        
        
        
            
        
        
            
        
    