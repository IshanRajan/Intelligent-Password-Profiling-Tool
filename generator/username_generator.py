# This script generates potential usernames using common patterns derived from
# consented profile data (e.g, first name, last name, nicknames, and years).
# This output helps demonstrate how personal information can make usernames
# predictable.

from input import get_user_info
profile = get_user_info()

def generate_username(profile):
    first_name = profile["first"]
    last_name = profile["last"]
    nickname = profile["nick"]
    birth_year = profile["year"]
    hobby = profile["hobby"]
    company = profile["company"]
    
    for 
    
