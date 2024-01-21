# For anyone curious how the algorithm worked, here's a high level overview:

# Data Cleaning
1. Load the CSV
2. Select relevant columns: Name, Gender, Gender Preference, Year Preference, and Personal Preferences (preferred matches were manually handled)
3. Clean and preprocess the data

# Gender and Year Matching
1. Group individuals by gender
2. Within each gender group, further group by year preference

# Compatibility Scoring
1. For each pair of individuals within the gender and year groups, calculate compatibility scores based on personal preferences

# Matchmaking Algorithm
1. Initialize empty lists for matched pairs and unmatched individuals.
2. For each gender group:
    a. Iterate over individuals.
    b. For each individual, find the most compatible individual from the opposite gender group.
    c. Create a pair and add to the matched list.
    d. Remove paired individuals from the list.
3. Add remaining unmatched individuals to the unmatched list.

# Handling Leftovers
1. List all individuals who are left unmatched.

# Result Output
1. Output the list of matched pairs.
2. Output the list of unmatched individuals.
