
def profile_analyzer(usernames,usernames_variations, generated_passwords, profile):
    
    # Normalize all input values to lowercase for consistency
    first_name = profile["first"].lower()
    last_name = profile["last"].lower()
    nickname = profile["nick"].lower()
    birth_year = profile["year"].lower()
    hobby = profile["hobby"].lower()
    company = profile["company"].lower()
    
    weak = []
    for item in generated_passwords:
        if first_name in item:
            weak.append(item)
        
        if last_name in item:
            weak.append(item)
        
        if usernames.index(item) in item:
            weak.append(item)
        
        if usernames_variations.index(item) in item:
            weak.append(item)
        
        if birth_year in item:
            weak.append(item)
        
        if company in item:
            weak.append(item)
        
        if hobby in item:
            weak.append(item)
        
        for item in usernames:
            if usernames in item:
                weak.append(item)
        
            
        
        
            
        
    