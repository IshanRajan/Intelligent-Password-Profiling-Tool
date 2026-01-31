
import argparse
import sys
import os
from input.cli_input import get_user_info
from data.data_loader import load_csv, load_json, load_text
from generator.username_generator import generate_username, expand_username_variations
from generator.password_generator import generate_passwords
from analyzer.profile_analyzer import profile_analyzer
from reporter.report_generator import generate_report
from pathlib import Path


def parse_arguments():

    parser = argparse.ArgumentParser(
        description="Intelligent Password Profiling Tool - Generates potential usernames and passwords based on user information. Make sure to read the ethics statement and the README."
    )

    parser.add_argument(
        "-i", "--input", type=str,
        default=None,
        help="Path to a profile input (if omitted, interactive mode is used)"
    )

    parser.add_argument(
        "-o", "--output-format", type=str,
        default="cli",
        choices=["cli", "json", "csv", "txt"],
        help="The file format you want the output to be stored in (Default being the command line)"
    )

    return parser.parse_args()


def ensure_reports_directory():
    """Create reports directory if it doesn't exist."""
    reports_dir = Path("reports")
    try:
        reports_dir.mkdir(exist_ok=True)
        return True
    except PermissionError:
        print("ERROR: No permission to create 'reports' directory")
        return False
    except Exception as e:
        print(f"ERROR: Could not create 'reports' directory: {e}")
        return False


def main():
    user_information = []

    try:
        args = parse_arguments()

        if args.input:
            file_path = args.input
            extension = Path(file_path).suffix.lower()

            # Validate file exists
            if not os.path.isfile(file_path):
                print(f"ERROR: File not found: {file_path}")
                sys.exit(1)

            try:
                if extension == ".csv":
                    user_information = load_csv(file_path)

                elif extension == ".json":
                    user_information = load_json(file_path)

                elif extension == ".txt":
                    user_information = load_text(file_path)

                else:
                    print(f"ERROR: Unsupported file type '{extension}'. Supported: .csv, .json, .txt")
                    sys.exit(1)

                print(f"✓ Successfully loaded {len(user_information)} profile(s) from {file_path}\n")

            except PermissionError:
                print(f"ERROR: Permission denied when reading {file_path}")
                sys.exit(1)
            except Exception as e:
                print(f"ERROR: Could not load file: {e}")
                sys.exit(1)

        else:
            # Interactive mode — loop so users can add as many profiles as they want
            while True:
                cont = input("Do you want to add user information? [yes/no]: ").strip().lower()

                if cont in ["yes", "y"]:
                    try:
                        profile = get_user_info()
                        user_information.append(profile)
                        print(f"✓ Profile added! (Total: {len(user_information)})\n")
                    except (EOFError, KeyboardInterrupt):
                        print("\nProfile input cancelled.")
                        break
                    except Exception as e:
                        print(f"ERROR during profile input: {e}\n")
                        continue

                elif cont in ["no", "n"]:
                    break

                else:
                    print("Please enter 'yes' or 'no'\n")

        # Validate we have profiles to process
        if not user_information:
            print("No profiles to process. Exiting.")
            sys.exit(0)

        # Process each profile
        profile_results = []

        for idx, profile in enumerate(user_information, 1):
            try:
                usernames = generate_username(profile)
                usernames_variations = expand_username_variations(usernames, profile)
                passwords = generate_passwords(profile)

                # Analyze passwords and categorize them by strength
                weak, medium, strong, very_strong = profile_analyzer(
                    usernames, usernames_variations, passwords, profile
                )

                profile_results.append({
                    "profile": profile,
                    "usernames": usernames,
                    "username_variations": usernames_variations,
                    "passwords": passwords,
                    "weak_passwords": weak,
                    "medium_passwords": medium,
                    "strong_passwords": strong,
                    "very_strong_passwords": very_strong
                })

                print(f"✓ Processed profile {idx}/{len(user_information)}")

            except KeyError as e:
                print(f"WARNING: Profile {idx} is missing required field: {e}. Skipping.")
                continue
            except Exception as e:
                print(f"WARNING: Error processing profile {idx}: {e}. Skipping.")
                continue

        if not profile_results:
            print("ERROR: No profiles were successfully processed.")
            sys.exit(1)

        print(f"\n✓ Successfully processed {len(profile_results)} profile(s)\n")

        # Create reports directory if saving to a file
        if args.output_format != "cli":
            if not ensure_reports_directory():
                print("ERROR: Cannot create output directory.")
                sys.exit(1)

        # Generate report
        print(f"Generating report in '{args.output_format}' format...\n")
        success = generate_report(profile_results, args.output_format)

        if success is False:
            print("ERROR: Report generation failed!")
            sys.exit(1)

    except KeyboardInterrupt:
        print("\n\nProgram interrupted by user. Exiting.")
        sys.exit(0)

    except Exception as e:
        print(f"UNEXPECTED ERROR: {e}")
        sys.exit(1)


if __name__ == "__main__":
    main()
    