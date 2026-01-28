
def generate_report(profile_results, output_format):
    total_usernames = 0
    total_username_variations = 0
    total_passwords = 0
    amount_of_profiles = len(profile_results)
    
    for p in profile_results:
        total_usernames +=len(p["usernames"])
        total_username_variations +=len(p["username_variations"])
        total_passwords +=len(p["passwords"])
        
    if output_format == "cli":
        print("========================================\n")
        print("Intelligent Password Profiling Tool\n")
        print("Ethical Demonstration Report\n")
        print("========================================\n")
        
        print("Summary\n")
        print("-------\n")
        print(f"Profiles processed: {amount_of_profiles}\n")
        print(f"Total usernames generated: {total_usernames}\n")
        print(f"Total username variations: {total_username_variations}\n")
        
        for profile in profile_results:
            print("----------------------------------------\n")
            print(profile["profile"])
            print(f"Name: {profile.get('first')} {profile.get('last')}\n")
            print(f"Nickname: {profile.get('nickname')}\n")
            print(f"Year: {profile.get('year')}\n")
            print(f"Hobby: {profile.get('hobby')}\n")
            print("\n----------------------------------------\n")
            print("Fields used: first,last,nickname,year,hobby\n")
            
            print(f"Base Usernames {len(profile['usernames'])}\n")
            print("--------------\n")
            for usernames in profile["usernames"]:
                print(f"{usernames}\n")
            
            print(f"Expand Username Variations {len(profile['username_variations'])}\n")
            print("--------------\n")
            for username_variation in profile["username_variations"]:
                print(f"{username_variation}\n")
            
            print(f"Password Candidates {len(profile['passwords'])}\n")
            print("--------------\n")
            for password_variation in profile["passwords"]:
                print(f"{password_variation}\n")
            
        print("========================================\n")
        print("End of report\n")
        print("========================================\n")
               
    elif output_format == "json":
        pass
    
    elif output_format == "csv":
        pass
    
    elif output_format == "txt":
        pass