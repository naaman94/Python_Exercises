from flask import Flask, render_template
app = Flask(__name__)

#print("""\nExercises 1\n """)
#"""****************************************************************************************"""

@app.route('/')
def index():
    return 'This is the Index page'

@app.route('/hello')
def hello():
    return 'Hello World!'

@app.route('/members')
def members():
    return 'Members Page'


#print("""\nExercises 2\n """)
#"""****************************************************************************************"""
@app.route('/marks/<mark>')
def hello_name(mark):
    return render_template('index.html', marks =int(mark))
    
 
#print("""\nExercises 3\n """)
#"""****************************************************************************************"""

@app.route('/css')
def css():
 return render_template('index1.html')

if __name__ == '__main__':
    app.run()