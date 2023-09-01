from flask import Flask, render_template, redirect, url_for
from flask_bootstrap import Bootstrap5
from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, SelectField
from wtforms.validators import DataRequired, URL
import csv, pandas

'''
Red underlines? Install the required packages first: 
Open the Terminal in PyCharm (bottom left). 

On Windows type:
python -m pip install -r requirements.txt

On MacOS type:
pip3 install -r requirements.txt

This will install the packages from requirements.txt for this project.
'''

app = Flask(__name__)
app.config['SECRET_KEY'] = '8BYkEfBA6O6donzWlSihBXox7C0sKR6b'
Bootstrap5(app)

# Exercise:
# add: Location URL, open time, closing time, coffee rating, wifi rating, power outlet rating fields
# make coffee/wifi/power a select element with choice of 0 to 5.
#e.g. You could use emojis ☕️/💪/✘/🔌
# make all fields required except submit
# use a validator to check that the URL field has a URL entered.
# ---------------------------------------------------------------------------
class CafeForm(FlaskForm):
    cafe = StringField(label='Cafe name', validators=[DataRequired()])
    location = StringField(label='Cafe Location on Google Maps (URL)', validators=[DataRequired(), URL()])
    opening_time = StringField(label='Opening Time e.g. 8AM or 8:30AM', validators=[DataRequired()])
    closing_time = StringField(label='Closing Time e.g. 5PM or 5:30AM', validators=[DataRequired()])
    coffee_rating = SelectField(label='Coffee Rating', validators=[DataRequired()], choices=[('☕️'),('☕️☕️'),('☕️☕️☕️'),('☕️☕️☕️☕️'),('☕️☕️☕️☕️☕️')])
    wifi_rating = SelectField(label='Wifi Strength Rating', validators=[DataRequired()], choices=[('✘'),('💪'),('💪💪'),('💪💪💪'),('💪💪💪💪'),('💪💪💪💪💪')])
    power_socket = SelectField(label='Power Socket Availability', validators=[DataRequired()], choices=[('✘'),('🔌'),('🔌🔌'),('🔌🔌🔌'),('🔌🔌🔌🔌'),('🔌🔌🔌🔌🔌')])
    submit = SubmitField(label='Submit')


# all Flask routes below
@app.route("/")
def home():
    return render_template("index.html")


@app.route('/add', methods=["POST", "GET"])
def add_cafe():
    cafe_form = CafeForm()
    # Exercise:
    # Make the form write a new row into cafe-data.csv
    # with   if form.validate_on_submit()
    if cafe_form.validate_on_submit():
        with open("cafe-data.csv", mode="a", encoding='utf-8') as csv_file:
            csv_file.write(f"\n{cafe_form.cafe.data},"
                           f"{cafe_form.location.data},"
                           f"{cafe_form.opening_time.data},"
                           f"{cafe_form.closing_time.data},"
                           f"{cafe_form.coffee_rating.data},"
                           f"{cafe_form.wifi_rating.data},"
                           f"{cafe_form.power_socket.data}")        
        return redirect(url_for('cafes'))
    return render_template('add.html', form=cafe_form)


@app.route('/cafes')
def cafes():
    # Option 1 - Using pandas module:
    data = pandas.read_csv("cafe-data.csv")
    # cafes_list = []

    # for index, row in data.iterrows():
    #     cafe_info = {
    #         "Cafe Name": row["Cafe Name"],
    #         "Location": row["Location"],
    #         "Open Time": row["Open"],
    #         "Closing Time": row["Close"],
    #         "Coffee": row["Coffee"],
    #         "Wifi": row["Wifi"],
    #         "Power": row["Power"]
    #         }
    #     cafes_list.append(cafe_info)
    
    # convert to list comprehension
    cafes_list = [
    {
        "Cafe Name": row["Cafe Name"],
        "Location": row["Location"],
        "Open Time": row["Open"],
        "Closing Time": row["Close"],
        "Coffee": row["Coffee"],
        "Wifi": row["Wifi"],
        "Power": row["Power"]
    }
    for index, row in data.iterrows()
    ]

    return render_template('cafes.html', cafes=cafes_list)

    # Option 2 - Using csv module:
    # with open('cafe-data.csv', newline='', encoding='utf-8') as csv_file:
    #     csv_data = csv.reader(csv_file, delimiter=',')

    #     # Skip the header row if it contains column names
    #     header = next(csv_data, None)

    #     list_of_rows = []
    #     for row in csv_data:
    #         cafe_info = {
    #             "Cafe Name": row[0],  # Assuming Cafe Name is in the first column (index 0)
    #             "Location": row[1],   # Assuming Location is in the second column (index 1)
    #             "Open Time": row[2],  # Assuming Open Time is in the third column (index 2)
    #             "Closing Time": row[3],  # Assuming Closing Time is in the fourth column (index 3)
    #             "Coffee": row[4],     # Assuming Coffee is in the fifth column (index 4)
    #             "Wifi": row[5],       # Assuming Wifi is in the sixth column (index 5)
    #             "Power": row[6]       # Assuming Power is in the seventh column (index 6
    #             }
    #         list_of_rows.append(cafe_info)

    # return render_template('cafes.html', cafes=list_of_rows)
    

if __name__ == '__main__':
    app.run(debug=True)
