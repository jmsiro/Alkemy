
After cloning the ropository:
 1.  Get into the directory in which it was downloadwd with the command: cd <repository>
 2.  Once into the correct directory, execute: pip install virtualenv
 (Only if you don't already have virtualenv installed)
 3. Run the following command to create you new enviroment: virtualenv venv
 ('venv' is the name given to the virtual environment, it can be different)
 4. Once created, run: source venv/bin/activate
 5. Followed by: pip install -r requirements.txt to install the necessary dependencies
 
Before starting:
 1. Create a .env file with the following:
      DATABASE_HOST = ''
      POSTGRES_USER = ''
      POSTGRES_PASSWORD = ''
      POSTGRES_PORT = ''
      ----------------------------------------------------------------
      PGADMIN_EMAIL: ''
      PGADMIN_PASSWORD: ''
      ----------------------------------------------------------------
      LOG_DIR = ''
      DOWNLOADS_DIR = '' # where to downloar the .csv files.
      EXCELS_DIR = '' # where to to save the .xlsx files from the queries to the database.
 2. Engine manager in 'engine.py' will use the first four items of this information to make the connetion to the DB.
 3. Items 5 and 6 are used to set the credentials to access the PostgreSQL database administrator.
 4. The last three will be used by the functions in process.py.
 NOTE: In my case, I use docker-compose to test everything, the file with the services it is also in the repository. 
