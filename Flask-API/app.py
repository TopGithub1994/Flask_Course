# Server Side
from os import name
from flask import Flask
from flask_restful import Api,Resource,abort,reqparse,marshal_with,fields
from flask_sqlalchemy import SQLAlchemy,Model

app=Flask(__name__)

# database
db=SQLAlchemy(app)
app.config['SQLALCHEMY_DATABASE_URI']="sqlite:///database.db"
api=Api(app)

class CityModel(db.Model):
    id=db.Column(db.Integer,primary_key=True)
    name=db.Column(db.String(100),nullable=False)
    temp=db.Column(db.String(100),nullable=False)
    weather=db.Column(db.String(100),nullable=False)
    people=db.Column(db.String(100),nullable=False)

    def __repr__(self):
        return f"City(name={name},temp={temp},weather={weather},people={people})"

db.create_all()

# Request Parser
city_add_args=reqparse.RequestParser()
city_add_args.add_argument("name",type=str,required=True,help="Type name need String!")
city_add_args.add_argument("temp",type=str,required=True,help="Type temp need String!")
city_add_args.add_argument("weather",type=str,required=True,help="Type weather need String!")
city_add_args.add_argument("people",type=int,required=True,help="Type people need Interger!")

# Update Request Parser
city_update_args=reqparse.RequestParser()
city_update_args.add_argument("name",type=str,help="Type name need String!")
city_update_args.add_argument("temp",type=str,help="Type temp need String!")
city_update_args.add_argument("weather",type=str,help="Type weather need String!")
city_update_args.add_argument("people",type=int,help="Type people need Interger!")

resource_field={
    "id":fields.Integer,
    "name":fields.String,
    "temp":fields.String,
    "weather":fields.String,
    "people":fields.String
}

mycity={
    1:{"name":"ชลบุรี","weather":"Hot","people":15000},
    2:{"name":"ระยอง","weather":"Rainy","people":25000},
    3:{"name":"กรุงเทพ","weather":"Cool","people":2005000}
}

# validate request
def notFoundCity(city_id):
    if city_id not in mycity:
        abort(404,message="ไม่พบข้อมูล...")

# def notFoundNameCity(name):
#     if name not in mycity:
#         abort(404,message="ไม่พบข้อมูล...")

# design
class WeatherCity(Resource):

    @marshal_with(resource_field)
    def get(self,city_id):
        # notFoundCity(city_id)
        result = CityModel.query.filter_by(id=city_id).first()
        if not result:
            abort(404,message="ไม่พบข้อมูลที่ร้องขอ")
        return result

    @marshal_with(resource_field)
    def post(self,city_id):
        result = CityModel.query.filter_by(id=city_id).first()
        if result:
            abort(404,message="The id can't be same!")
        args=city_add_args.parse_args()
        city=CityModel(id=city_id,name=args["name"],temp=args["temp"],weather=args["weather"],people=args["people"])
        db.session.add(city)
        db.session.commit()
        return city,201

    @marshal_with(resource_field) # filter 
    def patch(self,city_id):
        args=city_update_args.parse_args()
        result = CityModel.query.filter_by(id=city_id).first()
        if not result:
            abort(404,message="No data match!")
        if args["name"]:
            result.name=args["name"] 
        if args["temp"]:
            result.temp=args["temp"]
        if args["weather"]:
            result.weather=args["weather"]
        if args["people"]:
            result.people=args["people"]

        db.session.commit()
        return result

# Call
api.add_resource(WeatherCity,"/weather/<int:city_id>")

if __name__ == "__main__":
    app.run(debug=True)