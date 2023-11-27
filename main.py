from flask import redirect,Flask,request, render_template
import csv
app = Flask(__name__)

@app.route("/")
def home():
	return render_template('index.html')

@app.route('/<string:page_name>')
def about(page_name):
	return render_template(page_name)
def write_to_file(data):
	with open("data.txt", mode='a') as data2:
		email = data['email']
		subject = data['subject']
		message= data['message']
		file = data2.write(f'\n{email},{subject},{message}')

def write_to_csv(data):
	with open("data.csv", mode='a') as data2:
		email = data['email']
		subject = data['subject']
		message = data['message']
		csv_writer = csv.writer(data2,delimiter=',',lineterminator='',quotechar="'",quoting=csv.QUOTE_MINIMAL)
		csv_writer.writerow([email,subject,message])

@app.route('/submit_form', methods=['POST', 'GET'])
def submit_form():
	if request.method=='POST':
		data = request.form.to_dict()
		write_to_csv(data)
		write_to_file(data)
		print(data)
		return redirect('thankyou.html')
	else:
		return 'error'

'''@app.route("/about.html")
def about():
	return render_template('about.html')

@app.route("/works.html")
def works():
	return render_template('works.html')

@app.route("/index.html")
def index():
	return render_template('index.html')

@app.route("/contact.html")
def contact():
	return render_template('contact.html')
'''
if __name__ == "__main__":
	app.run(debug=True)