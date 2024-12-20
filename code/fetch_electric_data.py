import http.client
import json
from datetime import datetime, timedelta

# Function to get data for a single day
def get_data_for_day(conn, headers, date):
    conn.request("GET", f"/price?date={date}&priceFormat=cent&country=FI&currency=EUR", headers=headers)
    res = conn.getresponse()
    data = res.read()
    return data.decode("utf-8")

# Main function to loop over the days of the year and save data to a file
def fetch_yearly_data(start_date, end_date, filename):
    conn = http.client.HTTPSConnection("electricity-price.p.rapidapi.com")
    headers = {
        'X-RapidAPI-Key': "898c9fb7d7msh0d1be58dd0cd5e5p16eddajsn13a986ec4f59",
        'X-RapidAPI-Host': "electricity-price.p.rapidapi.com"
    }

    current_date = start_date

    # Open the file outside of the loop, so we don't open and close it on each iteration
    with open(filename, 'w') as file:
        while current_date <= end_date:
            print(f"Fetching data for {current_date.strftime('%Y-%m-%d')}")
            data = get_data_for_day(conn, headers, current_date.strftime('%Y-%m-%d'))
            file.write(data + '\n')  # Write data to file with a newline
            current_date += timedelta(days=1)

# Start and end dates
start_date = datetime(2023, 1, 1)
end_date = datetime(2023, 12, 31)

# Filename to save the data
filename = 'electricity_data.txt'

# Fetch all the data and save it
fetch_yearly_data(start_date, end_date, filename)
print(f"Data has been saved to {filename}")
