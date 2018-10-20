# Jones_Christopher_set09103_cw1
* Python Flask SHOULD BE INSTALLED (Either via the server or downloaded on to your local drive)
* Putty SHOULD BE INSTALLED FOR WINDOWS

## To start on Mac:

 * First open the terminal and type ssh MatricNo@set09103.napier.ac.uk
 * You will then be promted to type your password in 
 * Once logged in type the following 2 commands into the terminal in no particular order 
   * export FLASK_ENV=development (ensures the server is using the right environment
   * export FLASK_APP=home.py (lets the server know which file it should read)
 * After that type the following command into the terminal python -m flask run --host=0.0.0.0 --port:Your Port Number
   *This will start up the server
 * Type http://set09103.napier.ac.uk:Your Port Number into the browser


## To start on Windows:

* First open Putty and type ssh MatricNo@set09103.napier.ac.uk
 * You will then be promted to type your password in 
 * Once logged in type the following 2 commands into the terminal in no particular order 
   * export FLASK_ENV=development (ensures the server is using the right environment
   * export FLASK_APP=home.py (lets the server know which file it should read)
 * After that type the following command into the terminal python -m flask run --host=0.0.0.0 --port:Your Port Number
   *This will start up the server
 * Type http://set09103.napier.ac.uk:Your Port Number into the browser
