

# Requirements:

  You should have python3 installed
  Ubuntu based system

# Installation Instructions:

  Create a new folder

  Unzip files into folder

  Your directory should look like this:
      /FlaskApp
      /requirements.txt
      /dummydata.py
      /installation.md

  Open your terminal in the folder and run the following commands: 

  ``` 
  python3 -m venv projenv
  source projenv/bin/activate
  export FLASK_APP="FlaskApp"
  pip install -r requirements.txt
  flask run
  ```
  To restart the server run the following commands
  ```
  fuser -k 5000/tcp
  flask run
  ```
    
   

