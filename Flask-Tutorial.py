# This is how commenting works in Python
''' This is a doc string, usually meant to describe functionality of a function.
    This is not for every comment line'''
# Indenting indicates a change in scope.
# For examples, in a if statement...
# if i in counter:
#   print i
# The command to print i is within the scope of the if function.
# Same thing for loops, okay? (for i in counter)
# Basically, NO INDENTING WITH SPACES!!!

# This is where you import libraries (called Modules in Python)
from flask import Flask

# This designates this file as a Flask Application
app = Flask(__name__)

# App route is the URL route. For examples, if your domain was
# http://www.SanyaGupta.cse.unr.edu, then the route would do functionality at
# http://www.SanyaGupta.cse.unr.edu/Read/ . Make sense?
@app.route('/Read/', methods=['GET'])

# This is to define a function, remember to indent after. Anything indented
# after the function is in the scope of the function.
def ReadFile():
    return "Vinh is the greatest!"


# Follow the same recipe for POST and the rest
@app.route('/Create/', methods=['POST'])
def CreateEntry():
    return "Write Posting stuff here"

@app.route('/Update/', methods=['PUT'])
def UpdateFile():
    return "Crap needs updating, yo"

@app.route('/Delete/', methods=['DELETE'])
def DeleteEverything():
    return "DESTROY EVERYTHING"

if __name__ == '__main__':
    # This application unless specified runs on localhost, which means ONLY
    # your computer. This is generally for testing purposes. Specifically,
    # it runs on 127.0.0.1:5000 as a default. 5000 is the port and the rest
    # is localhost
    app.run(debug=True)

    # If you wanted to set the code to run on a domain and port, you would
    # use these two lines. Turns off the debugger and sets the domain to deploy
    #app.debug = false
	#app.run(host='127.0.0.1', port=8081)
