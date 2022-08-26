import numpy as np
import pandas as pd
import config
import pickle
import json

class price():
    
    def __init__(self,symboling,normalized_losses,fuel_type,aspiration,num_of_doors,drive_wheels,engine_location,wheel_base,length,width,height,curb_weight,num_of_cylinders,engine_size,bore,stroke,compression_ratio,horsepower,peak_rpm,city_mpg,highway_mpg,body_style,engine_type,fuel_system):

        self.symboling = symboling
        self.normalized_losses = normalized_losses
        self.fuel_type = fuel_type
        self.aspiration = aspiration
        self.num_of_doors = num_of_doors
        self.drive_wheels = drive_wheels
        self.engine_location = engine_location
        self.wheel_base = wheel_base
        self.lenth = length
        self.width = width
        self.height = height
        self.curb_weight = curb_weight
        self.num_of_cylinders = num_of_cylinders
        self.engine_size = engine_size
        self.bore = bore
        self.stroke = stroke
        self.compression_ratio = compression_ratio
        self.horsepower = horsepower
        self.peak_rpm = peak_rpm
        self.city_mpg = city_mpg
        self.highway_mpg = highway_mpg
        self.body_style = body_style
        self.engin_type = engine_type
        self.fuel_system = fuel_system


def load_model(self):
    with open('config.MODEL_FILE_PATH','rb')as f:
        self.model = pickle.load(f)

    with open(config.JSON_FILE_PATH,'r')as f:
        self.json = json.load(f)

def get_price(self):
    self.load_model()
    body_style_index  = self.json['columns'].index(self.body_style)
    engine_type_index = self.json['columns'].index(self.engine_type)
    fuel_system_index = self.json['columns'].index(self.fuel_system)

    array = np.zeros(len(self.json),dtype=int)

    array[0] = self.symboling
    array[1] = self.normalized_losses
    array[2] = self.json['fuel_type_dict'][self.fuel_type]
    array[3] = self.aspiration
    array[4] = self.json['no_of_doors'][self.num_of_doors]
    array[5] = self.json['drive_wheels_dict'][self.drive_wheels] 
    array[6] = self.json['engine_location_dict'][self.engine_location] 
    array[7] = self.wheel_base
    array[8] = self.length 
    array[9] = self.width 
    array[10] = self.height 
    array[11] = self.curb_weight 
    array[12] = self.json['num_of_cylinders_dict'][self.num_of_cylinders]
    array[13] = self.engine_size 
    array[14] = self.bore 
    array[15] = self.stroke
    array[16] = self.compression_ratio 
    array[17] = self.horsepower
    array[18] = self.peak_rpm 
    array[19] = self.city_mpg
    array[20] = self.highway_mpg 

    array[body_style_index] = 1
    array[engine_type_index] = 1
    array[fuel_system_index] = 1

    price_pre = self.model.predict(array)
    return price_pre







