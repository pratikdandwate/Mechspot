from flask import Flask, render_template

app = Flask(__name__)


@app.route('/')
def home():
  return render_template('home.html')

@app.route('/services')
def services():
  return render_template('services.html')

@app.route('/about-us')
def aboutus():
  return render_template('aboutus.html')

@app.route('/contact-us')
def contactus():
  return render_template('contactus.html')

if __name__ == '__main__':
  app.run(host='0.0.0.0', debug=True)
