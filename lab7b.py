#!/usr/bin/env python3
# Student ID: ajpatel44

class Time:
    """Simple object type for time of the day.
    data attributes: hour, minute, second
    """
    def __init__(self, hour=12, minute=0, second=0):
        """constructor for time object""" 
        self.hour = hour
        self.minute = minute
        self.second = second

    def format_time(self):
        """Return time object (t) as a formatted string"""
        return f'{self.hour:02d}:{self.minute:02d}:{self.second:02d}'

    def sum_times(self, t2):
        """Add two time objects and return the sum."""
        total_seconds = self.time_to_sec() + t2.time_to_sec()
        total_seconds %= 24 * 3600  # wrap around if over 24 hours
        return sec_to_time(total_seconds)

    def change_time(self, seconds):
        """Add seconds to current time correctly."""
        total_seconds = self.time_to_sec() + seconds
        total_seconds %= 24 * 3600  # wrap around if over 24 hours
        t = sec_to_time(total_seconds)
        self.hour, self.minute, self.second = t.hour, t.minute, t.second
        return self.format_time()

    def time_to_sec(self):
        """Convert time object to total seconds."""
        return self.hour * 3600 + self.minute * 60 + self.second

    def valid_time(self):
        """Check if time attributes are valid."""
        if self.hour < 0 or self.minute < 0 or self.second < 0:
            return False
        if self.hour >= 24 or self.minute >= 60 or self.second >= 60:
            return False
        return True

def sec_to_time(seconds):
    """Convert seconds to Time object."""
    t = Time()
    minutes, t.second = divmod(seconds, 60)
    t.hour, t.minute = divmod(minutes, 60)
    return t

def change_time(t, seconds):
    """Standalone function to change time t by seconds."""
    return t.change_time(seconds)

def format_time(t):
    """Standalone function to format Time object as string."""
    return t.format_time()
