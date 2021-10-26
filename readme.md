- [1. IMPORTANT](#1-important)
- [2. Preparing to run the sample codes](#2-preparing-to-run-the-sample-codes)
  - [2.1. Create virtual environment with Conda](#21-create-virtual-environment-with-conda)
  - [2.2. Create virtual environment with Python venv](#22-create-virtual-environment-with-python-venv)
  - [2.3. Install only the required Python modules and packages](#23-install-only-the-required-python-modules-and-packages)
- [3. Description of Sample Codes](#3-description-of-sample-codes)



# 1. IMPORTANT
The materials in this [repository](https://github.com/wooihaw/py4iot) (https://github.com/wooihaw/py4iot) are meant for proof-of-concept (POC) only and they must not be used for production or deployment.

# 2. Preparing to run the sample codes
1. Download the repository as a zip file.
2. Once downloaded, extract the zip file into its own folder.
3. Follow one of the methods below to create a virtual environment.

## 2.1. Create virtual environment with Conda
1. Follow this method if you have installed Anaconda.
2. Launch Anaconda Prompt.
3. Create a cirtual environment called py4iot with Python 3.9:
   - conda create -n py4iot python=3.9
4. After the virtual environment is created, activate it:
   - conda activate py4iot
5. Navigate to the folder with the extracted repository.
6. Install the required Python modules and packages:
   - python -m pip install -r requirements.txt
7. To deactivate the virtual environment:
   - conda deactivate

## 2.2. Create virtual environment with Python venv
1. Launch a terminal/command prompt.
2. Navigate to the folder with the extracted repository.
3. Create a virtual environment:
    - python -m venv env
4. Once the virtual environment has been created, there will be a folder called "env" in the current folder.
5. To activate the virtual environment in Windows:
   - cd env\Scripts
   - activate
   - cd ..\\..
6. To active the virtual environment in Linux:
   - souce env/bin/activate
7. Install the required Python modules and packages:
   - python -m pip install -r requirements.txt
8. To deactive the virtual environment in Windows or Linux:
   - deactivate

## 2.3. Install only the required Python modules and packages
1. Follow this method if you do not wish to create a virtual environment.
2. Launch a terminal/command prompt.
3. Install the required Python modules and packages:
   - python -m pip install paho-mqtt dash

# 3. Description of Sample Codes
Filename | Description
:---|:---
api_app.py | Python script for RESTful API (server)
api_example | Python script on accessing the RESTful API (client)
dashboard_app.py | Python script for the dashboard (server)
mqtt_pub.py | Python script for MQTT publisher
mqtt_sub.py | Python script for MQTT subscriber
