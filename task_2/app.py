from flask import Flask, render_template, render_template_string, url_for, request
from geo_utils import find_pois
from db_funcs import get_all_data_from_db
from helper_funcs import validate_latitude, validate_longitude, validate_range, handle_category

app = Flask(__name__)


@app.route("/online/", methods=['GET', 'POST'])
def get_poi_online():

    if request.method == 'POST':
        user_request = {}
        lat = validate_latitude(request.form['latitude'])
        lon = validate_longitude(request.form['longitude'])
        if lat and lon:
            user_request['location'] = [lat, lon]
        else:
            return 'Invalid coordinates'
        if validate_range(request.form['range']):
            user_request['distance_range'] = validate_range(request.form['range'])
        else:
            return 'Invalid range'
        user_request['poi_category'] = handle_category(request.form['category'])

        try:
            poi_data = find_pois(user_request['location'],
                                 user_request['distance_range'],
                                 user_request['poi_category'])
        except:
            return "Can't get POI data"

        return render_template_string(poi_data)

    elif request.method == 'GET':
        return render_template('main_page.html')


@app.route("/db/")
def get_from_db():
    try:
        data = get_all_data_from_db()
    except:
        return "Can't get data from DB"
    return render_template('db_data.html', data=data)


if __name__ == "__main__":
    app.run(debug=False, host='0.0.0.0', port=5555)
