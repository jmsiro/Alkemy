

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
 2. Engine manager in 'engine.py' will use this information to make the connetion to the DB.
 NOTE: In my case, I use docker-compose to test everything, the file with the services it is also in the repository. 
