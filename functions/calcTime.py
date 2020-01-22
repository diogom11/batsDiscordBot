from datetime import datetime, timedelta


def calculate_cs_time(cs_time_given ,n_cs_time):

    date = datetime.now()
    cs_time = date.replace(hour = cs_time_given[0], minute=cs_time_given[1], second=0)

    calculated = cs_time - datetime.now()
    str_calculated = str(calculated).split(":")

    return str_calculated

    


