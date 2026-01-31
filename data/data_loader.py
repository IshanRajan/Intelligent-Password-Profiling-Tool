import os
import pandas as pd
import json


class DataLoaderError(Exception):
    """Base exception for data loading errors."""
    pass


def load_csv(filepath):
    """
    Load a CSV file and convert all text data to lowercase.
    
    Raises:
        DataLoaderError: If file cannot be loaded or parsed
    """
    if not os.path.isfile(filepath):
        raise DataLoaderError(f"CSV file not found: {filepath}")
    
    try:
        df = pd.read_csv(filepath)
    except pd.errors.EmptyDataError:
        raise DataLoaderError(f"CSV file is empty: {filepath}")
    except pd.errors.ParserError as e:
        raise DataLoaderError(f"CSV parsing error: {e}")
    except Exception as e:
        raise DataLoaderError(f"Error reading CSV: {e}")
    
    # Validate required columns exist
    required_columns = ["first", "last", "nick", "year", "hobby", "company"]
    missing = [col for col in required_columns if col not in df.columns]
    if missing:
        raise DataLoaderError(
            f"CSV missing required columns: {', '.join(missing)}\n"
            f"Required: {', '.join(required_columns)}"
        )
    
    # Convert text columns to lowercase
    for column_name in df.columns:
        if df[column_name].dtype == object:
            df[column_name] = df[column_name].fillna('null').str.lower()
    
    list_of_dicts = df.to_dict(orient='records')
    return list_of_dicts


def load_json(filepath):
    """
    Load a JSON file and convert all string values to lowercase.
    
    Raises:
        DataLoaderError: If file cannot be loaded or parsed
    """
    if not os.path.isfile(filepath):
        raise DataLoaderError(f"JSON file not found: {filepath}")
    
    try:
        with open(filepath, 'r', encoding='utf-8') as data_file:
            df = json.load(data_file)
    except json.JSONDecodeError as e:
        raise DataLoaderError(f"Invalid JSON format: {e}")
    except Exception as e:
        raise DataLoaderError(f"Error reading JSON: {e}")
    
    # Validate it's a list
    if not isinstance(df, list):
        raise DataLoaderError("JSON must contain a list of profile objects")
    
    # Validate each profile has required fields
    required_fields = ["first", "last", "nick", "year", "hobby", "company"]
    
    for idx, dictionary in enumerate(df):
        if not isinstance(dictionary, dict):
            raise DataLoaderError(f"Profile {idx} is not a dictionary")
        
        missing = [field for field in required_fields if field not in dictionary]
        if missing:
            raise DataLoaderError(
                f"Profile {idx} missing fields: {', '.join(missing)}"
            )
        
        # Convert strings to lowercase
        for key in dictionary:
            if isinstance(dictionary[key], str):
                dictionary[key] = dictionary[key].lower()
    
    return df


def load_text(filepath):
    """
    Load a plain text file with space-separated profile fields.
    
    Expected format: first last nick year hobby company (one profile per line)
    
    Raises:
        DataLoaderError: If file cannot be loaded or has invalid format
    """
    if not os.path.isfile(filepath):
        raise DataLoaderError(f"Text file not found: {filepath}")
    
    keys = ["first", "last", "nick", "year", "hobby", "company"]
    df = []
    
    try:
        with open(filepath, 'r', encoding='utf-8') as data_file:
            for line_num, line in enumerate(data_file, 1):
                line = line.strip()
                
                # Skip empty lines
                if not line:
                    continue
                
                parts = line.split()
                
                # Validate line has exactly 6 fields
                if len(parts) != 6:
                    raise DataLoaderError(
                        f"Line {line_num} has {len(parts)} fields, expected 6\n"
                        f"Format: first last nick year hobby company"
                    )
                
                # Convert to lowercase and create dict
                parts_lower = [part.lower() for part in parts]
                my_dict = dict(zip(keys, parts_lower))
                df.append(my_dict)
                
    except DataLoaderError:
        raise
    except Exception as e:
        raise DataLoaderError(f"Error reading text file: {e}")
    
    if not df:
        raise DataLoaderError("Text file contains no valid profiles")
    
    return df