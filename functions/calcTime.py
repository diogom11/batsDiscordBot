from datetime import datetime, timedelta


def calculate_cs_time(cs_time_given ,n_cs_time):

    date = datetime.now()
    cs_time = date.replace(hour = cs_time_given[0], minute=cs_time_given[1], second=0)

    calculated = cs_time - datetime.now()
    str_calculated = str(calculated).split(":")

    cs_string = f"{str_calculated[0]} hours, {str_calculated[1]} minutes, {str_calculated[2]} seconds left to COUNTER STRIKE HOUR NUMBER {n_cs_time}"
    print(cs_string)
    return cs_string

    


