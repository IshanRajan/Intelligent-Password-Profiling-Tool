
import os, pandas as pd, json

def load_csv(filepath):
    """
    Load a CSV file and convert all text data to lowercase.

    This function reads a CSV from the given file path, converts all columns 
    containing text to lowercase to ensure consistency, and returns the data 
    as a list of dictionaries. Each dictionary represents a row in the CSV, 
    with column names as keys.

    Args:
        filepath (str): The path to the CSV file to load.

    Returns:
        list of dict: A list where each item is a dictionary representing a row
                      of the CSV, with all string values in lowercase.
    """

    df = pd.read_csv(filepath)
    for column_name, column_series in df.items():
        if column_series.dtype == object:
            df[column_name] = df[column_name].str.lower()
            
    list_of_dicts = df.to_dict(orient='records')
    return list_of_dicts
    
def load_json(filepath):
    """
    Load a JSON file and convert all string values to lowercase.

    Args:
        filepath (str): Path to the JSON file to be loaded.

    Returns:
        list of dict: A list of dictionaries representing the JSON data,
                      with all string values converted to lowercase.
    
    Notes:
        - Assumes the JSON file contains a list of dictionaries.
        - Non-string values are left unchanged.
    """

    with open(filepath, 'r') as data_file:
        df = json.load(data_file)
        for dictionary in df:
            for key in dictionary:
                if isinstance(dictionary[key], str):
                    dictionary[key] = dictionary[key].lower()
        return df

def load_text(filepath):
    pass
