from flask import Flask, render_template, url_for, request, redirect
import csv

app = Flask(__name__)

# use a decorator to define routes on the flask server
@app.route('/')
def home():
  return render_template('index.html')

@app.route('/<string:page_name>')
def show_page(page_name=None):
  return render_template(page_name)

@app.route('/submit_form', methods=['POST', 'GET'])
def submit_form():
  if request.method == 'POST':
    try:
      data = request.form.to_dict()
      write_to_csv(data)
      return redirect('/thankyou.html')
    except:
      return 'Did not save to database', 422
  else:
    return 'Something went wrong, try again!', 500


def write_to_file(data):
  with open('database.txt', mode='a') as database:
    email = data['email']
    subject = data['subject']
    message = data['message']
    line = f"\n{data['email']},{data['subject']},{data['message']}"
    file = database.write(line)

def write_to_csv(data):
    with open('database.csv', newline='', mode='a') as database2:
      email = data['email']
      subject = data['subject']
      message = data['message']
      csv_writer = csv.writer(database2, delimiter=',', quotechar='"', quoting=csv.QUOTE_MINIMAL)
      csv_writer.writerow([email, subject, message])
