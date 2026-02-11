import pandas as pd
usernames = pd.Series([' Alice ', 'bOB', ' Charlie_Data ', 'daisy'])
cleaned_usernames = usernames.str.strip().str.lower()
print("Cleaned Usernames:")
print(cleaned_usernames)
contains_a = cleaned_usernames.str.contains('a')
print("\nNames Containing Letter 'a':")
print(contains_a)
