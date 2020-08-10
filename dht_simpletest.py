import time
import board
import adafruit_dht
from datetime import datetime

# Initialize the dht device, with pin connected to:
dhtDevice = adafruit_dht.DHT22(board.D4)

while True:
    try:
        # Print the values to the serial port
        temp_c = dhtDevice.temperature
        humidity = dhtDevice.humidity
        now = datetime.now().strftime("%B %d (%a) %H:%M:%S")
        print(
                "{} - Temp: {:.1f} C     Humidity: {}% ".format(
                    now, temp_c, humidity
            )
        )

    except RuntimeError as error:
        print("Error occured:")
        print(error.args[0])

    time.sleep(300.0)
