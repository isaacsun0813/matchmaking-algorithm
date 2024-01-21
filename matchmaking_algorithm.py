import pandas as pd
import random

# Load the data
file_path = '/USER/ISAACSUN/DOWNLOADS/cooldata.csv'  
data = pd.read_csv(file_path)

# Function to check gender preference match
def gender_preference_match(person1, person2):
    return person1['Would you like to be matched with a female or male?'] == person2['Your gender?']

# Function to check if grade preference is satisfied
def is_grade_preference_satisfied(proposer, acceptor):
    acceptable_grades = proposer['Preference for Match'].split(', ')
    return acceptor['Grade'] in acceptable_grades

# Compatibility scoring function
def calculate_compatibility(person1, person2, preferences_columns):
    score = sum(abs(person1[preference] - person2[preference]) for preference in preferences_columns)
    return score

# Strict one-to-one matchmaking algorithm
def strict_one_to_one_matchmaking(data, preferences_columns):
    individuals = data.to_dict('records')
    random.shuffle(individuals)  # Shuffling for fairness
    matches = {}
    unmatched = set(individual['Name'] for individual in individuals)

    # Iterating through each individual for strict 1-to-1 matching
    for proposer in individuals:
        if proposer['Name'] in matches:
            continue  # Skip already matched individuals

        for acceptor in individuals:
            if acceptor['Name'] in matches or acceptor['Name'] == proposer['Name']:
                continue  # Skip already matched or same individuals

            # Checking for mutual preference satisfaction
            if gender_preference_match(proposer, acceptor) and is_grade_preference_satisfied(proposer, acceptor):
                # Create match and update unmatched set
                matches[proposer['Name']] = acceptor['Name']
                matches[acceptor['Name']] = proposer['Name']
                unmatched.discard(proposer['Name'])
                unmatched.discard(acceptor['Name'])
                break  # Stop searching once a match is found

    # Prepare matched pairs
    matched_pairs = [(p, matches[p]) for p in matches if p < matches[p]]  # Avoid duplicate pairs
    return matched_pairs, unmatched

# Selecting relevant columns and preferences
relevant_columns = ['Timestamp', 'Name', 'Your gender?', 'Would you like to be matched with a female or male?', 'Grade', 'Preference for Match']
preferences_columns = data.columns[9:-1]  # Adjust as necessary based on your data
cleaned_data = data[relevant_columns + list(preferences_columns)].dropna()

# Running the matchmaking algorithm
strict_matches, strict_leftovers = strict_one_to_one_matchmaking(cleaned_data, preferences_columns)

# Converting results to DataFrame
strict_matches_df = pd.DataFrame(strict_matches, columns=['Name1', 'Name2'])
strict_leftovers_df = pd.DataFrame(list(strict_leftovers), columns=['Unmatched Individuals'])

# Saving the results to CSV files (optional)
strict_matches_df.to_csv('/path/to/strict_one_to_one_matched_pairs.csv', index=False)
strict_leftovers_df.to_csv('/path/to/strict_one_to_one_unmatched_individuals.csv', index=False)
