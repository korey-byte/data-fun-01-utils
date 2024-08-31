''' ITERATION 3

Module: 2K Sales LLC - Reasonbly priced shoes by a reasonable seller

This module provides a simple, reusable foundation for my analytics projects.

Process:
In this third iteration, I declare additional variables to show skills with different data types.
'''

###########################################
# Declare global variables - keep byline at the end
# We will use this information in a smarter byline
###########################################

# Boolean variable to indicate if the company is the best company ever
is_best_company_ever: bool = True

# Integer variable for the number of years in biness
years_in_biness: int = 5

# List of strings representing the softwares i'm kind of sort of good at
skills_semi_mastered: list = ["Salesforce", "Excel", "Power_bi"]

# List of floats representing my latest and greatest homework scores
Koreys_pretty_good_homework_scores: list = [8.0, 3.0, 2.0, 8.0, 4.0]

###########################################
# Declare a global variable named byline.
# Make it a multiline f-string to show our information.
###########################################

byline: str = f"""
---------------------------------------------------------
2K Sales LLC : Reasonably priced shoes by a reasonable seller
---------------------------------------------------------
Is Best Company Ever: (is_best_company_ever}
Years in Biness: (years_in_biness)
Skills Semi Mastered: (skills_semi_mastered)
Koreys Pretty Good Homework Scores: (koreys_pretty_good_homework_scores)
"""

###########################################
# Define the get_byline() Function
###########################################

def get_byline() -> str: 
    '''Return a byline for my analytics projects."'
    return byline

###########################################
# Define a main() function for this module.
###########################################

def main() -> None:
    '''Print results of get_byline() when main() is called.'''
    print(get_byline())
