from myapp import db

class Cities(db.Model):
	id = db.Column(db.Integer, primary_key=True)
	city_name=db.Column(db.String(64), index=True)
	city_rank=db.Column(db.Integer)
	isVisited=db.Column(db.Boolean)
