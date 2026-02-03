#enjoy


import json
import csv
import os


class ReportGenerationError(Exception):
    """Exception for report generation errors."""
    pass


def generate_report(profile_results, output_format):
    """
    Generate a report in the specified format with error handling.

    Args:
        profile_results: List of profile dictionaries with results
        output_format: Format type ('cli', 'json', 'csv', 'txt')

    Returns:
        bool: True if successful, False otherwise

    Raises:
        ReportGenerationError: If report cannot be generated
    """
    if not profile_results:
        raise ReportGenerationError("No profiles to report")

    try:
        if output_format == "cli":
            return _generate_cli_report(profile_results)
        elif output_format == "json":
            return _generate_json_report(profile_results)
        elif output_format == "csv":
            return _generate_csv_report(profile_results)
        elif output_format == "txt":
            return _generate_txt_report(profile_results)
        else:
            raise ReportGenerationError(
                f"Unknown output format: {output_format}")

    except ReportGenerationError:
        raise
    except Exception as e:
        raise ReportGenerationError(f"Unexpected error generating report: {e}")


def _calculate_summary(profile_results):
    """Calculate summary statistics for the report."""
    total_usernames = sum(len(p.get("usernames", [])) for p in profile_results)
    total_username_variations = sum(
        len(p.get("username_variations", [])) for p in profile_results)
    total_passwords = sum(len(p.get("passwords", [])) for p in profile_results)

    return {
        "profiles": len(profile_results),
        "usernames": total_usernames,
        "variations": total_username_variations,
        "passwords": total_passwords
    }


def _generate_cli_report(profile_results):
    """Generate CLI report (print to console)."""
    summary = _calculate_summary(profile_results)

    print("=" * 50)
    print("Intelligent Password Profiling Tool")
    print("Ethical Demonstration Report")
    print("=" * 50)
    print("\nSummary")
    print("-" * 50)
    print(f"Profiles processed: {summary['profiles']}")
    print(f"Total usernames: {summary['usernames']}")
    print(f"Total variations: {summary['variations']}")
    print(f"Total passwords: {summary['passwords']}")

    for idx, profile in enumerate(profile_results):
        profile_data = profile.get("profile", {})

        print("\n" + "-" * 50)
        print(f"Profile {idx + 1}")
        print(
            f"Name: {profile_data.get('first', 'N/A')} {profile_data.get('last', 'N/A')}")
        print(f"Nickname: {profile_data.get('nick', 'N/A')}")
        print(f"Year: {profile_data.get('year', 'N/A')}")
        print(f"Hobby: {profile_data.get('hobby', 'N/A')}")
        print("-" * 50)

        usernames = profile.get("usernames", [])
        if usernames:
            print(f"\nBase Usernames ({len(usernames)})")
            for username in usernames:
                print(f"  • {username}")

        variations = profile.get("username_variations", [])
        if variations:
            print(f"\nUsername Variations ({len(variations)})")
            for variation in variations:
                print(f"  • {variation}")

        passwords = profile.get("passwords", [])
        if passwords:
            print(f"\nPassword Candidates ({len(passwords)})")
            for password in passwords:
                print(f"  • {password}")

        weak = profile.get("weak_passwords", [])
        medium = profile.get("medium_passwords", [])
        strong = profile.get("strong_passwords", [])
        very_strong = profile.get("very_strong_passwords", [])

        print(f"\nPassword Analysis")
        print("-" * 50)

        if weak:
            print(f"\n  🔴 Weak ({len(weak)})")
            for p in weak:
                print(f"    • {p}")

        if medium:
            print(f"\n  🟡 Medium ({len(medium)})")
            for p in medium:
                print(f"    • {p}")

        if strong:
            print(f"\n  🟢 Strong ({len(strong)})")
            for p in strong:
                print(f"    • {p}")

        if very_strong:
            print(f"\n  🔵 Very Strong ({len(very_strong)})")
            for p in very_strong:
                print(f"    • {p}")

    print("\n" + "=" * 50)
    print("End of Report")
    print("=" * 50)

    return True


def _generate_json_report(profile_results):
    """Generate JSON report file."""
    output_file_path = "reports/people_expanded.json"

    try:
        with open(output_file_path, 'w', encoding='utf-8') as fp:
            json.dump(profile_results, fp, indent=2, ensure_ascii=False)
        print(f"✓ Report saved to: {output_file_path}")
        return True

    except PermissionError:
        raise ReportGenerationError(f"Permission denied: {output_file_path}")
    except Exception as e:
        raise ReportGenerationError(f"Error writing JSON: {e}")


def _generate_csv_report(profile_results):
    """Generate CSV report file."""
    output_file_path = "reports/people_expanded.csv"
    headers = ["first", "last", "nick", "year",
               "hobby", "company", "type", "value"]

    try:
        with open(output_file_path, 'w', newline='', encoding='utf-8') as f:
            writer = csv.DictWriter(f, fieldnames=headers)
            writer.writeheader()

            for profile in profile_results:
                profile_data = profile.get("profile", {})

                # Write usernames
                for username in profile.get("usernames", []):
                    row = {**profile_data, "type": "username", "value": username}
                    writer.writerow(row)

                # Write variations
                for variation in profile.get("username_variations", []):
                    row = {**profile_data, "type": "username_variation",
                           "value": variation}
                    writer.writerow(row)

                # Write passwords
                for password in profile.get("passwords", []):
                    row = {**profile_data, "type": "password", "value": password}
                    writer.writerow(row)

        print(f"✓ Report saved to: {output_file_path}")
        return True

    except PermissionError:
        raise ReportGenerationError(f"Permission denied: {output_file_path}")
    except Exception as e:
        raise ReportGenerationError(f"Error writing CSV: {e}")


def _generate_txt_report(profile_results):
    """Generate TXT report file."""
    output_file_path = "reports/people_expanded.txt"
    summary = _calculate_summary(profile_results)

    try:
        with open(output_file_path, "w", encoding='utf-8') as f:
            f.write("=" * 50 + "\n")
            f.write("Intelligent Password Profiling Tool\n")
            f.write("Ethical Demonstration Report\n")
            f.write("=" * 50 + "\n\n")

            f.write("Summary\n")
            f.write("-" * 50 + "\n")
            f.write(f"Profiles processed: {summary['profiles']}\n")
            f.write(f"Total usernames: {summary['usernames']}\n")
            f.write(f"Total variations: {summary['variations']}\n")
            f.write(f"Total passwords: {summary['passwords']}\n")

            for idx, profile in enumerate(profile_results):
                profile_data = profile.get("profile", {})

                f.write("\n" + "-" * 50 + "\n")
                f.write(f"Profile {idx + 1}\n")
                f.write(
                    f"Name: {profile_data.get('first', 'N/A')} {profile_data.get('last', 'N/A')}\n")
                f.write(f"Nickname: {profile_data.get('nick', 'N/A')}\n")
                f.write(f"Year: {profile_data.get('year', 'N/A')}\n")
                f.write(f"Hobby: {profile_data.get('hobby', 'N/A')}\n")
                f.write("-" * 50 + "\n")

                usernames = profile.get("usernames", [])
                f.write(f"\nBase Usernames ({len(usernames)})\n")
                for username in usernames:
                    f.write(f"{username}\n")

                variations = profile.get("username_variations", [])
                f.write(f"\nUsername Variations ({len(variations)})\n")
                for variation in variations:
                    f.write(f"{variation}\n")

                passwords = profile.get("passwords", [])
                f.write(f"\nPassword Candidates ({len(passwords)})\n")
                for password in passwords:
                    f.write(f"{password}\n")

            f.write("\n" + "=" * 50 + "\n")
            f.write("End of Report\n")
            f.write("=" * 50 + "\n")

        print(f"✓ Report saved to: {output_file_path}")
        return True

    except PermissionError:
        raise ReportGenerationError(f"Permission denied: {output_file_path}")
    except Exception as e:
        raise ReportGenerationError(f"Error writing TXT: {e}")
