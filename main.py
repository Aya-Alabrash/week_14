form get_covid_cases import *
from get_weather import *

def main():
    country = "canada"
    print(get_covid_cases(country))
    print(get_weather(country))

    message = f"\nLocation: {location}\n\n{weather_info}\n\n{covid_info}"
    # Your Email details
    sender_email = "Your_Email@gmail.com"
    sender_password = "Your_password/App_password"
    receiver_email = "Receiver@gmail.com"
    subject = f"Update for {location}"

    # Send the email
    send_email(sender_email, sender_password, receiver_email, subject, message)

if __name__ == '__main__':
    main()