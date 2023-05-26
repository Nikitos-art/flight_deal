from datetime import datetime, timedelta
from flight_deal.flight_search import FlightSearch
from flight_deal.data_manager import DataManager
from notification_manager import NotificationManager


data_manager = DataManager()
sheet_data = data_manager.get_destination_data()
flight_search = FlightSearch()


ORIGIN_CITY_IATA = "LON"

if sheet_data[0]["iataCode"] == "":
    for row in sheet_data:
        row["iataCode"] = flight_search.get_destination_code(row["city"])
    print(sheet_data)

    #data_manager.destination_data = sheet_data
    data_manager.update_destination_codes()

tomorrow = datetime.now() + timedelta(days=1)
six_month_from_today = datetime.now() + timedelta(days=(6 * 30))

for destination in sheet_data:
    flight = flight_search.check_flights(
        ORIGIN_CITY_IATA,
        destination["iataCode"],
        from_time=tomorrow,
        to_time=six_month_from_today
    )

    if flight.price < destination["lowestPrice"]:
        print("Found a cheaper flight")
        NotificationManager(flight.price, flight.origin_city, flight.origin_airport, flight.destination_city,
                            flight.destination_airport, flight.out_date, flight.return_date)
        print("SMS notification has been sent.")

    # print("__________________________________________")
    # print(f"Destination city{flight.destination_city}")
    # print(f"Price{flight.price}")