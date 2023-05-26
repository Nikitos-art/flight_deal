import os
from twilio.rest import Client
from dotenv import load_dotenv

load_dotenv('flight_deal/.env')
account_sid = os.getenv('ACCOUNT_SID')
auth_token = os.getenv('AUTH_TOKEN')
twilio_phone = os.getenv('MY_TWILIO_PHONE')
my_phone = os.getenv('MY_PHONE')

class NotificationManager:

    def __init__(self, price, dept_city_name, dept_IATA, arrival_city, arrival_IATA, outbound_date, inbound_date):
        self.price = price
        self.dept_city_name = dept_city_name
        self.dept_IATA = dept_IATA
        self.arrival_city = arrival_city
        self.arrival_IATA = arrival_IATA
        self.outbound_date = outbound_date
        self.inbound_date = inbound_date

        client = Client(account_sid, auth_token)
        message = client.messages.create(
            body=f"price {self.price}  departure_city_name {self.dept_city_name}  departure_IATA {self.dept_IATA} "
                 f"arrival_city {self.arrival_city}  arrival_IATA {self.arrival_IATA}  outbound_date {self.outbound_date}"
                 f"inbound_date {self.inbound_date}",
            from_=twilio_phone,
            to=my_phone
        )
        print(message.sid)

