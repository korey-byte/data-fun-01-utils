''' ITERATION 2

Module: 2K Sales LLC - Reasonably priced shoes by a resonable seller

This module provides a simple, reusable foundation for my analytics projects.

Process:
In this second iteration, add a function that returns the byline as a string.
I'll create a function named get_byline().
It'll return my byline to whatever calls the get_byline() function.
I'll update the main() function to use the new get_byline() function.

#############################
# Declare a global variable named byline.
#############################

byline: str = '2K Sales LLC: Reasonably priced shoes by a reasonable seller'

#############################
# Define the get_byline() Function
#############################

def get_byline() -> str:
    '''Return a byline for my analytics project.'''
    return byline
    
#############################
# Define a main() function for this module.
#############################

def main() -> None:
    '''Print the byline to the console when this function is called.'''
    print(get_byline())
    
#############################
# Conditional Execution
#############################

if __name__ == '__main__':
    main()
