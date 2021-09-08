from datetime import datetime
import pandas as pd
#from itertools import islice
#import copy

def get_datetime():
    now = datetime.now()
    dt_string = now.strftime("%m/%d/%Y %H:%M:%S")
    return dt_string