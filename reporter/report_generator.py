
def generate_report(profile_results, output_format):
    total_usernames = 0
    total_username_variations = 0
    total_passwords = 0
    amount_of_profiles = len(profile_results)
    
    for p in profile_results:
        total_usernames +=sum(len(p["usernames"]))
        total_username_variations +=sum(len(p["username_variations"]))
        
    
    if output_format == "cli":
        print("========================================\n")
        print("Intelligent Password Profiling Tool\n")
        print("Ethical Demonstration Report\n")
        print("========================================\n")
        
        print("Summary\n")
        print("-------\n")
        print(f"Profiles processed: {amount_of_profiles}")
        
    elif output_format == "json":
        pass
    
    elif output_format == "csv":
        pass
    
    elif output_format == "txt":
        pass