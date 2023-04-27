import datetime
import lunarcalendar

# Specify the range of years for which to match the calendars
start_year = 2023
end_year = 2030

# Loop over each year in the range
for year in range(start_year, end_year+1):
    # Generate a list of the full moon dates in the lunar calendar for this year
    lunar_full_moons = lunarcalendar.Moon(year).phases()
    
    # Loop over each full moon date in the lunar calendar
    for lunar_date in lunar_full_moons:
        # Convert the lunar date to the corresponding solar date
        solar_date = lunarcalendar.toSolarDate(*lunar_date[:3])
        
        # Check if the solar date is also a full moon date
        if datetime.date(solar_date.year, solar_date.month, solar_date.day) in lunarcalendar.FullMoon(year):
            # If it is, print out the date in both calendars
            print(f"Full moon on {lunar_date[2]}/{lunar_date[1]}/{lunar_date[0]} (lunar) corresponds to {solar_date.day}/{solar_date.month}/{solar_date.year} (solar)")
