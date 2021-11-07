from myapp import myapp_obj
from flask import render_template, redirect, flash
from myapp.forms import TopCities

@myapp_obj.route("/", methods = ['GET', 'POST'])
def home():
	title = 'Top Cities'
	name = 'James'
	form = TopCities()
	if form.validate_on_submit():
		flash(f'City name: {form.city_name.data} Rank: {form.city_rank.data} has been added')
		return redirect("/")
	return render_template('home.html', title = title, name = name, form = form)
