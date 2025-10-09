# This script generates potential usernames using common patterns derived from
# consented profile data (e.g, first name, last name, nicknames, and years).
# This output helps demonstrate how personal information can make usernames
# predictable.

from input.cli_input import get_user_info
profile = get_user_info()

def generate_username(profile):
    first_name = profile["first"].lower()
    last_name = profile["last"].lower()
    nickname = profile["nick"].lower()
    birth_year = profile["year"].lower()
    hobby = profile["hobby"].lower()
    company = profile["company"].lower()
    
    potential_usernames = []
    
    if first_name and last_name:
        first_last = first_name + last_name
        potential_usernames.append(first_last)
        
        first_initial_last = first_name[0] + last_name
        potential_usernames.append(first_initial_last)
        
        last_initial_last = last_name + first_name[0]
        potential_usernames.append(last_initial_last)
        
        first_initial_last_initial = first_name[0] + last_name[0]
        potential_usernames.append(first_initial_last_initial)
        
        last_initial_first_initial = last_name[0] + first_name[0]
        potential_usernames.append(last_initial_first_initial)
    
    if nickname:
        potential_usernames.append(nickname)
    
    if first_name and birth_year:
        first_name_year = first_name + birth_year
        potential_usernames.append(first_name_year)
        
        nickname_year = nickname + birth_year
        potential_usernames.append(nickname_year)
        
        last_name_year = last_name + birth_year
        potential_usernames.append(last_name_year)
    
    if first_name and hobby:
        first_name_hobby = first_name + hobby
        potential_usernames.append(first_name_hobby)
        
        first_name_company = first_name + company
        potential_usernames.append(first_name_company)
        
        nickname_hobby = nickname + hobby
        potential_usernames.append(nickname_hobby)
    
    if hobby and birth_year:
        
        hobby_year = hobby + birth_year
        potential_usernames.append(hobby_year)
        
        company_year = company + birth_year
        potential_usernames.append(company_year)
        
        first_initial_hobby = first_name[0] + hobby
        potential_usernames.append(first_initial_hobby)
    
    potential_usernames = sorted(list(set(potential_usernames)))
    return potential_usernames

def expand_username_variations(base_usernames, profile):
    first_name = profile["first"].lower()
    last_name = profile["last"].lower()
    nickname = profile["nick"].lower()
    birth_year = profile["year"].lower()
    hobby = profile["hobby"].lower()
    company = profile["company"].lower()
    
    all_variations = []
    for item in base_usernames:
        if first_name in item and last_name in item:
            first_last =  item.replace(first_name + last_name ,first_name + "_" + last_name)
            all_variations.append(first_last)
            
            first_last = item.replace(first_name + "_" + )

if __name__ == "__main__":
    usernames = generate_username(profile)
    usernames_variations = expand_username_variations(usernames)
    print(usernames)

        
        


    
    
        
        
    
