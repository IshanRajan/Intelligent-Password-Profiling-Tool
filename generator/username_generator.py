# This script generates potential usernames using common patterns derived from
# consented profile data (e.g., first name, last name, nicknames, and years).
# It also expands those usernames with realistic variations such as separators,
# prefixes, capitalization, and numeric suffixes.
# This output helps demonstrate how personal information can make usernames
# predictable and highlight the importance of avoiding guessable naming patterns.

from input.cli_input import get_user_info


def is_valid_value(value):
    """
    Check if a value is valid (not None, not 'null', not empty).

    Args:
        value: The value to check

    Returns:
        bool: True if valid, False otherwise
    """
    return value and value.lower() not in ['null', '']


def generate_username(profile):
    """
    Generate base username combinations derived from a user's profile.

    Args:
        profile (dict): A dictionary containing user attributes such as
                        first name, last name, nickname, birth year, hobby, and company.

    Returns:
        list: A sorted list of potential base usernames derived from the given profile.
    """
    # Normalize all input values to lowercase for consistency
    first_name = profile["first"].lower()
    last_name = profile["last"].lower()
    nickname = profile["nick"].lower()
    birth_year = profile["year"].lower()
    hobby = profile["hobby"].lower()
    company = profile["company"].lower()

    potential_usernames = []

    # --- Basic name-based combinations ---
    if is_valid_value(first_name) and is_valid_value(last_name):
        first_last = first_name + last_name
        potential_usernames.append(first_last)

        first_initial_last = first_name[0] + last_name
        potential_usernames.append(first_initial_last)

        last_initial_last = last_name + first_name[0]
        potential_usernames.append(last_initial_last)

        first_initial_last_initial = first_name[0] + last_name[0]
        potential_usernames.append(first_initial_last_initial)

        last_initial_first_initial = last_name[0] + first_name[0]
        potential_usernames.append(last_initial_first_initial)

    # --- Include nickname-only username ---
    if is_valid_value(nickname):
        potential_usernames.append(nickname)

     # --- Add year-based combinations ---
    if is_valid_value(first_name) and is_valid_value(birth_year):
        first_name_year = first_name + birth_year
        potential_usernames.append(first_name_year)

        if is_valid_value(nickname):
            nickname_year = nickname + birth_year
            potential_usernames.append(nickname_year)

        if is_valid_value(last_name):
            last_name_year = last_name + birth_year
            potential_usernames.append(last_name_year)

    # --- Hobby and company-related usernames ---
    if is_valid_value(first_name) and is_valid_value(hobby):
        first_name_hobby = first_name + hobby
        potential_usernames.append(first_name_hobby)

        if is_valid_value(company):
            first_name_company = first_name + company
            potential_usernames.append(first_name_company)

        if is_valid_value(nickname):
            nickname_hobby = nickname + hobby
            potential_usernames.append(nickname_hobby)

    # --- Mixed hobby/year patterns ---
    if is_valid_value(hobby) and is_valid_value(birth_year):
        hobby_year = hobby + birth_year
        potential_usernames.append(hobby_year)

        if is_valid_value(company):
            company_year = company + birth_year
            potential_usernames.append(company_year)

        if is_valid_value(first_name):
            first_initial_hobby = first_name[0] + hobby
            potential_usernames.append(first_initial_hobby)

    # Remove duplicates and sort alphabetically
    potential_usernames = sorted(list(set(potential_usernames)))
    return potential_usernames


def expand_username_variations(base_usernames, profile):
    """
    Expand base usernames into realistic variations using separators,
    capitalization, prefixes, and numeric suffixes.

    Args:
        base_usernames (list): The initial list of base usernames.
        profile (dict): A dictionary containing user attributes for contextual logic.

    Returns:
        list: A sorted list of expanded username variations.
    """
    # Extract user info for pattern-based logic (LOWERCASE)
    first_name = profile["first"].lower()
    last_name = profile["last"].lower()
    nickname = profile["nick"].lower()
    birth_year = profile["year"].lower()
    hobby = profile["hobby"].lower()
    company = profile["company"].lower()

    all_variations = []
    for item in base_usernames:
        # --- Add separator and capitalization patterns ---
        if first_name in item and last_name in item:
            first_last = item.replace(
                first_name + last_name, first_name + "_" + last_name)
            all_variations.append(first_last)

            first_last = item.replace(
                first_name + last_name, first_name + "." + last_name)
            all_variations.append(first_last)

            first_last = item.replace(
                first_name + last_name, first_name + "-" + last_name)
            all_variations.append(first_last)

            first_last = item.replace(
                first_name + last_name, first_name.capitalize() + last_name.capitalize())
            all_variations.append(first_last)

            first_last = item.replace(
                first_name + last_name, first_name.capitalize() + "_" + last_name.capitalize())
            all_variations.append(first_last)

            first_last = item.replace(
                first_name + last_name, first_name.upper() + last_name.upper())
            all_variations.append(first_last)

            # --- Prefix-based variations ---
            the_first_last = item.replace(
                first_name + last_name, "thereal" + first_name + last_name)
            all_variations.append(the_first_last)

            official_first_last = item.replace(
                first_name + last_name, "official" + first_name + last_name)
            all_variations.append(official_first_last)

            its_first_last = item.replace(
                first_name + last_name, "its" + first_name + last_name)
            all_variations.append(its_first_last)

            mr_first_last = item.replace(
                first_name + last_name, "mr" + first_name + last_name)
            all_variations.append(mr_first_last)

        # --- Add numeric suffix variants ---
        if first_name in item and last_name in item:
            first_name_number = item.replace(
                first_name + last_name, first_name + last_name + "1")
            all_variations.append(first_name_number)

            first_name_number = item.replace(
                first_name + last_name, first_name + last_name + "12")
            all_variations.append(first_name_number)

            first_name_number = item.replace(
                first_name + last_name, first_name + last_name + "123")
            all_variations.append(first_name_number)

            first_name_number = item.replace(
                first_name + last_name, first_name + last_name + "2025")
            all_variations.append(first_name_number)

            first_name_number = item.replace(
                first_name + last_name, first_name + last_name + birth_year)
            all_variations.append(first_name_number)

    # Remove duplicates and sort alphabetically
    all_variations = sorted(list(set(all_variations)))
    return (all_variations)


if __name__ == "__main__":
    profile = get_user_info()
    # Generate and expand usernames, then print results
    usernames = generate_username(profile)
    usernames_variations = expand_username_variations(usernames, profile)

    print("\n--- Base Usernames ---")
    print(usernames)

    print("\n--- Expanded Username Variations ---")
    print(usernames_variations)
