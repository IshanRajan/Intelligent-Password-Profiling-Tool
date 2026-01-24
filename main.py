import argparse
import os
from input.cli_input import get_user_info
from data.data_loader import load_csv, load_json, load_text
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
            extension = file_path.suffix.lower()
            
            if extension == ".csv":
               
        else:
            user_information = get_user_info()
    
    except:
    