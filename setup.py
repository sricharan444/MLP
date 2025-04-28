from setuptools import find_packages,setup
from typing import List
K='-e .'
def get_requirements(file_path:str)->List[str]:
      req=[]
      with open(file_path) as i:
            req=i.readlines()
            [r.replace("\n","") for  r in req]
            if K in req:
                  req.remove(K)
      return req

setup(
      name='mlproject',
      version='0.0.1',        packages=find_packages(),
      install_requires=get_requirements('requiements.txt')
      )
#version is used to update the package if the pakage is updated.