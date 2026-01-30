import json
import csv


def generate_report(profile_results, output_format):
    total_usernames = 0
    total_username_variations = 0
    total_passwords = 0
    amount_of_profiles = len(profile_results)

    for p in profile_results:
        total_usernames += len(p["usernames"])
        total_username_variations += len(p["username_variations"])
        total_passwords += len(p["passwords"])

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

        counter = 0
        for profile in profile_results:
            profile_data = profile["profile"]
            print("----------------------------------------\n")
            print(f"Profile: {counter}")
            print(
                f"Name: {profile_data.get('first')} {profile_data.get('last')}\n")
            print(f"Nickname: {profile_data.get('nickname')}\n")
            print(f"Year: {profile_data.get('year')}\n")
            print(f"Hobby: {profile_data.get('hobby')}\n")
            print("\n----------------------------------------\n")
            print("Fields used: first,last,nickname,year,hobby\n")

            print(f"Base Usernames {len(profile['usernames'])}\n")
            print("--------------\n")
            for usernames in profile["usernames"]:
                print(f"{usernames}\n")

            print(
                f"Expand Username Variations {len(profile['username_variations'])}\n")
            print("--------------\n")
            for username_variation in profile["username_variations"]:
                print(f"{username_variation}\n")

            print(f"Password Candidates {len(profile['passwords'])}\n")
            print("--------------\n")
            for password_variation in profile["passwords"]:
                print(f"{password_variation}\n")

            counter += 1

        print("========================================\n")
        print("End of report\n")
        print("========================================\n")

    elif output_format == "json":
        output_file_path = "reports/people_expanded.json"

        try:
            with open(output_file_path, 'w') as fp:
                json.dump(profile_results, fp)

        except PermissionError:
            print(
                f"ERROR: Permission denied when writing to {output_file_path}")
            return False

        except Exception as e:
            return False

    elif output_format == "csv":
        output_file_path = "reports/people_expanded.csv"
        headers = ["first", "last", "nick", "year", "hobby", "company",
                   "type", "value"]  # type indicates username, variation, or password

        try:

            with open(output_file_path, 'w', newline='', encoding='utf-8') as f:
                writer = csv.DictWriter(f, fieldnames=headers)
                writer.writeheader()

                for profile in profile_results:

                    for username in profile["usernames"]:
                        writer.writerow(
                            {"type": "username", "value": username})

                    for variation in profile["username_variations"]:
                        writer.writerow(
                            {"type": "username_variation", "value": variation})

                    for password in profile["passwords"]:
                        writer.writerow(
                            {"type": "password", "value": password})

        except PermissionError:
            print(
                f"ERROR: Permission denied when writing to {output_file_path}")
            return False

        except Exception as e:
            return False

    elif output_format == "txt":
        output_file_path = "reports/people_expanded.txt"
        try:
            with open(output_file_path, "w", newline="", encoding='utf-8') as f:
                f.write("========================================\n")
                f.write("Intelligent Password Profiling Tool\n")
                f.write("Ethical Demonstration Report\n")
                f.write("========================================\n")

                f.write("Summary\n")
                f.write("-------\n")
                f.write(f"Profiles processed: {amount_of_profiles}\n")
                f.write(f"Total usernames generated: {total_usernames}\n")
                f.write(
                    f"Total username variations: {total_username_variations}\n")

                counter = 0
                for profile in profile_results:
                    profile_data = profile["profile"]
                    f.write("----------------------------------------\n")
                    f.write(f"Profile: {counter}")
                    f.write(
                        f"Name: {profile_data.get('first')} {profile_data.get('last')}\n")
                    f.write(f"Nickname: {profile_data.get('nickname')}\n")
                    f.write(f"Year: {profile_data.get('year')}\n")
                    f.write(f"Hobby: {profile_data.get('hobby')}\n")
                    f.write("\n----------------------------------------\n")
                    f.write("Fields used: first,last,nickname,year,hobby\n")

                    f.write(f"Base Usernames {len(profile['usernames'])}\n")
                    f.write("--------------\n")
                    for usernames in profile["usernames"]:
                        f.write(f"{usernames}\n")

                    f.write(
                        f"Expand Username Variations {len(profile['username_variations'])}\n")
                    f.write("--------------\n")
                    for username_variation in profile["username_variations"]:
                        f.write(f"{username_variation}\n")

                    f.write(
                        f"Password Candidates {len(profile['passwords'])}\n")
                    f.write("--------------\n")
                    for password_variation in profile["passwords"]:
                        f.write(f"{password_variation}\n")

                    counter += 1
                
                print("========================================\n")
                print("End of report\n")
                print("========================================\n")

        except PermissionError:
                print(
                    f"ERROR: Permission denied when writing to {output_file_path}")
                return False

        except Exception as e:
                return False
