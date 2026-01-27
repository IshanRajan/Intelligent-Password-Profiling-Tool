import argparse
import sys
import os
from input.cli_input import get_user_info
from data.data_loader import load_csv, load_json, load_text
from generator.username_generator import generate_username, expand_username_variations
from generator.password_generator import generate_passwords
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
        help="The file format you want the output to be stored in (Default being the command line)"
    )

    return parser.parse_args()


def main():
    try:
        args = parse_arguments()

        if args.input:
            file_path = args.input
            extension = Path(file_path).suffix.lower()

            if extension == ".csv":
                user_information = load_csv(args.input)

            elif extension == ".json":
                user_information = load_json(args.input)

            elif extension == ".txt":
                user_information = load_text(args.input)

            else:
                print("Incorrect File Type, please input.csv, .json and .txt")
                sys.exit(1)
        else:
            while True:
                cont = print(
                    "Do you wanna add the user information? \n [yes or no]")
                cont_case = cont.lower()
                if cont_case == "yes":
                    user_information = [get_user_info()]

                else:
                    break

        profile_results = []

        for profile in user_information:
            usernames = generate_username(profile)
            usernames_variations = expand_username_variations(
                usernames, profile)
            passwords = generate_passwords(profile)

            profile_results.append({
                "profile": profile,
                "username": usernames,
                "username_variations": usernames_variations, 
                "passwords": passwords
            })

        if args.output_format == "cli":
            pass
            # Saves as a CLI

        elif args.output_format == "json":
            pass
            # Saves as a JSON

        elif args.output_format == "csv":
            pass
            # Saves as a CSV

        elif args.output_format == "txt":
            pass
            # Saves as a TXT

    except ValueError as e:
        print(f"Error: {e}")

    except Exception as e:
        print(f"Unexpected error: {e}")
        sys.exit(1)
