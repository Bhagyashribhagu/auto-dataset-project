from flask import Flask , render_template  , jsonify , request
import config
from projectapp.utils import price

app = Flask(__name__)

@app.route('/price_predict')
def home():
    symboling=3.00
    normalized_losses=115.00
    fuel_type='gas'
    aspiration= 'std'
    num_of_doors='two'
    drive_wheels= 'fwd'
    engine_location='front'
    wheel_base=88.60
    length=168.80
    width=64.10
    height=48.80
    curb_weight=2548.00
    num_of_cylinders= 'four'
    engine_size=130.00
    bore=3.47
    stroke=2.68
    compression_ratio=9.00
    horsepower=111.00
    peak_rpm=5000.00
    city_mpg=21.00
    highway_mpg=27.00
    body_style='sedan'
    engine_type='ohcf'
    fuel_system='mpfi'

    res = price(symboling,normalized_losses,fuel_type,aspiration,num_of_doors,drive_wheels,engine_location,wheel_base,length,width,height,curb_weight,num_of_cylinders,engine_size,bore,stroke,compression_ratio,peak_rpm,city_mpg,highway_mpg,body_style,engine_type,fuel_system)
    result = res.get_price()
    return jsonify({'result':result})

app.run()    

