from datetime import datetime, timedelta


def calculateCsTime(cs_time_given):

    date = datetime.now()
    cs_time = date.replace(hour=cs_time_given[0], minute=cs_time_given[1], second=0)

    calculated = cs_time - datetime.now()
    str_calculated = str(calculated).split(":")

    return str_calculated

    
def calculateCsTimeSeconds(cs_time_given):

    date = datetime.now()
    cs_time = date.replace(hour=cs_time_given[0], minute=cs_time_given[1], second=0)

    calculated = cs_time - datetime.now()
    str_calculated = str(calculated).split(":")

    total_seconds = int(str_calculated[0])*60*60 + int(str_calculated[1])*60 + int(str_calculated[2])
    return total_seconds