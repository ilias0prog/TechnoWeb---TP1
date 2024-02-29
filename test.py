def spacebars_only(text: str) -> bool:
    """Check if a string contains only spaces"""
    t = text.strip()
    return (len(t)<=0) 
    
def check_input_validity(*args):
    for input in args:
        # Check if empty string :
        if len(input) < 1:
            raise ValueError("All the fields must be filled")
        # Check if only spacebars :
        i = input.strip()
        if len(i) < 1:
            raise ValueError("Please provide real title, author and editor")
    return

name = "aaaaaaaa"
author = "       "
editor = "blabla"
    
check_input_validity(name,author,editor)