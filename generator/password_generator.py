from input.cli_input import get_user_info

profile = get_user_info()

def generate_passwords(profile):
    first_name = profile["first"].lower()
    last_name = profile["last"].lower()
    nickname = profile["nick"].lower()
    birth_year = profile["year"].lower()
    hobby = profile["hobby"].lower()
    company = profile["company"].lower()
    
    passwords = []
    
    if first_name and last_name and birth_year and nickname:
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
    
    if first_name and last_name and hobby and nickname and company:
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
    
    if first_name and hobby and nickname and company and birth_year:
        first_name_hobby = first_name + hobby
        passwords.append(first_name_hobby)
        
        first_name_123 = first_name + "123"
        passwords.append(first_name_123)
        
        first_name = first_name + "!"
        passwords.append(first_name)
        
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
        
        
        
        
    
    
    