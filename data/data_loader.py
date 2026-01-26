
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
    """
    Load a plain text file where each line contains six space-separated fields:
    first name, last name, nickname, birth year, hobby, and company.

    Each line is split into parts and mapped onto a fixed set of keys in this
    order: ["first", "last", "nick", "year", "hobby", "company"].

    Returns:
        list[dict]: A list of dictionaries, one per line in the file.
                    All values remain strings, exactly as they appear
                    in the text file.

    Notes:
        - The function assumes every line has exactly six fields.
        - If the file structure doesn’t match this format, the output may be
          incorrect.
    """

    keys = ["first", "last", "nick", "year", "hobby", "company"]
    df = []
    with open(filepath, 'r') as data_file:
        for line in data_file:
            parts = line.strip().split()
            my_dict = dict(zip(keys, parts))
            df.append(my_dict)
        return df
            
                
                
                
                
                
