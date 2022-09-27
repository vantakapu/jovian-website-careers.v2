from flask import Flask, render_template

app = Flask(__name__)

JOBS = [
  {
    'id': 1,
    'title': 'Data Analyst',
    'location': 'Berlin, Germany',
    'salary': 'EU 50,000'
  },
  {
    'id': 2,
    'title': 'Data Scientist',
    'location': 'Jena, Germany',
    'salary': 'EU 65,000'
  },
  {
    'id': 3,
    'title': 'Frontend Engineer',
    'location': 'Hamburg, Germany'
    
  },
  {
    'id': 4,
    'title': 'Backend Engineer',
    'location': 'Leipzig, Germany',
    'salary': 'EU 60,000'
  }
]

@app.route("/")
def hello_world():
  return render_template('home.html', 
                         jobs=JOBS,
                         company_name='Jovian')

if __name__ == "__main__":
  app.run(host='0.0.0.0', debug=True)