#!/usr/bin/env python3
# Student ID: ajpatel44
from lab7a import *

def time_to_sec(time):
    '''convert a time object to a single integer representing the number of seconds from mid-night'''
    minutes = time.hour * 60 + time.minute
    seconds = minutes * 60 + time.second
    return seconds

def sec_to_time(seconds):
    '''convert a given number of seconds to a time object in hour, minute, second format'''
    time = Time()
    minutes, time.second = divmod(seconds, 60)
    time.hour, time.minute = divmod(minutes, 60)
    return time

def sum_times(t1, t2):
    total_sec = time_to_sec(t1) + time_to_sec(t2)
    total_sec %= 24 * 3600
    return sec_to_time(total_sec)

def change_time(t, seconds):
    total_sec = time_to_sec(t) + seconds
    total_sec %= 24 * 3600
    return sec_to_time(total_sec)
