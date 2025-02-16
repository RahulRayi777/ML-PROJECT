from typing import List

HYPEN_E_DOT = '-e .'

def get_requirements(file_path: str) -> List[str]:
    '''
    This function will return the list of requirements.
    '''
    requirements = []
    with open(file_path) as file_obj:
        requirements = file_obj.readlines()
    
    # Remove newline characters
    requirements = [req.replace("\n", "") for req in requirements]

    # Remove '-e .' if it exists in the requirements list
    if HYPEN_E_DOT in requirements:
        requirements.remove(HYPEN_E_DOT)

    return requirements
get_requirements(r'C:\Users\naray\OneDrive\Pictures\Desktop\01-College_Stuff\ML_PROJECT\requirements.txt')