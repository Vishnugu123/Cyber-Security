from setuptools import find_packages ,setup
from typing import List

def get_requirements()->List[str]:
    '''
    this will return list of requirements 
    '''
    requirement_lst:List[str]=[]
    try:
        with open('requirements.txt') as file:
            #read the lines from file
            lines = file.readlines()
            # process each line
            for line in lines:
                requirement = line.strip()
                # ignore empty lines & -e .
                if requirement and requirement != '-e .':
                    requirement_lst.append(requirement)
    except FileNotFoundError:
        print('requirements.txt not found')


    return requirement_lst


setup(
    name="Network Security",
    author_email="vishu7699181@gmail.com",
    author="vishnu",
    version="0.0.0.1",
    packages=find_packages(),
    install_requires=get_requirements()
)

