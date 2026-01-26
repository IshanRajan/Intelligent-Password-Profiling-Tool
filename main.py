import argparse
import sys
import os
from input.cli_input import get_user_info
from data.data_loader import load_csv, load_json, load_text
from generator.username_generator import generate_username, expand_username_variations
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
            # Maybe I can potentially loop here
            user_information = [get_user_info()]
        
        usernames = generate_username(user_information)
        usernames_variations = expand_username_variations(usernames,user_information)
    
    except ValueError as e:
        print(f"Error: {e}")
    
    except Exception as e:
        print(f"Unexpected error: {e}")
        sys.exit(1)
