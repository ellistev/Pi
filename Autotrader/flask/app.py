from flask import Flask, request
from flask_restful import Resource, Api
from json import dumps

# Create a engine for connecting to SQLite3.
# Assuming salaries.db is in your app root folder

#e = create_engine('sqlite:///salaries.db')

app = Flask(__name__)
api = Api(app)


class Category(Resource):
    def get(self, photoUrl):
        # Connect to databse
        #conn = e.connect()
        # Perform query and return JSON data
        #query = conn.execute("select distinct DEPARTMENT from salaries")
        return {'category': photoUrl} #[i[0] for i in query.cursor.fetchall()]}


class MakeModel(Resource):
    def get(self, photoUrl):
        #conn = e.connect()
        #query = conn.execute("select * from salaries where Department='%s'" % department_name.upper())
        # Query the result and get cursor.Dumping that data to a JSON is looked by extension
        result = {'makemodels': photoUrl} #[dict(zip(tuple(query.keys()), i)) for i in query.cursor]}
        return result
        # We can have PUT,DELETE,POST here. But in our API GET implementation is sufficient


api.add_resource(Category, '/category/<string:photoUrl>')
api.add_resource(MakeModel, '/makemodel/<string:photoUrl>')

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=80)
