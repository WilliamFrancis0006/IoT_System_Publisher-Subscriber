"""
@author: Wesley Henderson
@edited by: William Francis
With thanks to Christopher Smith
"""

import paho.mqtt.client as mqtt
import psutil
from datetime import datetime
import time


if __name__ == "__main__":
    hn = "138.47.204.51"
    client = mqtt.Client()
    client.connect(hn)
    client.loop_start()
    while True:
        cpupct = psutil.cpu_percent()
        current_time = datetime.now()
        # Use '@@@' as delimiter between time and data
        msg = str(current_time) + '@@@' + str(cpupct)
        topic1 = "Francis/cpupct"
        client.publish(topic=topic1, payload=msg)
        time.sleep(2)
