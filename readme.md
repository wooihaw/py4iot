# Preparing to run the sample codes
1. Download the repository as a zip file.
2. Once downloaded, extract the zip file into its own folder.
3. Follow one of the methods below to create a virtual environment.


## Create virtual environment with Conda
1. Create a cirtual environment called py4iot with Python 3.9:
   - conda create -n py4iot python=3.9
2. After the virtual environment is created, acivate it:
   - conda activate py4iot
3. Navigate to the folder with the extracted repository.
4. Install the required Python modules and packages:
   - python -m pip install -r requirements.txt
5. To deactivate the virtual environment:
   - conda deactivate

## Create virtual environment with Python venv
1. Navigate to the folder with the extracted repository.
2. Create a virtual environment:
    - python -m venv env
3. Once the virtual environment has been created, there is be a folder called "env" in the current folder.
4. To activate the virtual environment in Windows:
   - cd env\Scripts
   - activate
5. To active the virtual environment in Linux:
   - souce env/bin/activate
6. To deactive the virtual environment in Windows or Linux:
   - deactivate