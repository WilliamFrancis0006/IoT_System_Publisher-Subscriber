"""
Original Author: Wesley Henderson
With thanks to Christopher Smith


EDITED BY: William Francis
DATE: 5/4/20


(NOTE: All of my edits are commented in FULL CAPS and TO THE RIGHT OF THE CODE for ease of grading)
"""

import datetime
import paho.mqtt.client as mqtt
import matplotlib.pyplot as plt

def on_connect(client, userdata, flags, rc):
    """Subscribe to topics once connected to broker."""
    print("Connected with result code "+str(rc))
    
                                            # TOPICS I SUBCRIBED TO
                                            
    client.subscribe("Francis/cpupct")      # (MY PUBLISHER)

    
    client.subscribe("Damare/cpupct")     # (CLASSMATE'S PUBLISHERS)
    client.subscribe("Miller/cpupct")
    client.subscribe("Markham/cpupct")
    client.subscribe("Bingham/cpupct")
    
def on_message(client, userdata, msg):
    """When messages are received from broker, do some things."""
    #You will need to modify this function to handle each topic you are subscribed to

    topic = msg.topic
    message = msg.payload.decode()
    print(str(topic))
    print(str(message))
    # Make sure this is a topic we care about.
    # Or, if we're subscribed to multiple topics, see which it is before
    # deciding what to do with the message

                                                            # ADDS EACH SPECIFIC SUBSCRIBERS TO A DIFFERENT SET OF LISTS IN USERDATA (time#[], cpupct#[])
                                                            
                                                    
    if "Francis/cpupct" in str(topic):                      # APPENDS INDEX 0 & 1 (in userdata)
        timestamp, cpupct = message.split('@@@')
        userdata[0].append(datetime.datetime.strptime(timestamp,
                                             '%Y-%m-%d %H:%M:%S.%f'))
        userdata[1].append(float(cpupct))
        
    if "Damare/cpupct" in str(topic):                     # APPENDS INDEX 2 & 3 (in userdata)
        timestamp, cpupct = message.split('@@@')
        userdata[2].append(datetime.datetime.strptime(timestamp,
                                             '%Y-%m-%d %H:%M:%S.%f'))
        userdata[3].append(float(cpupct))
        
    if "Miller/cpupct" in str(topic):                             # APPENDS INDEX 4 & 5 (in userdata)
        timestamp, cpupct = message.split('@@@')
        userdata[4].append(datetime.datetime.strptime(timestamp,
                                             '%Y-%m-%d %H:%M:%S.%f'))
        userdata[5].append(float(cpupct))
        
    if "Markham/cpupct" in str(topic):                             # APPENDS INDEX 6 & 7 (in userdata)
        timestamp, cpupct = message.split('@@@')
        userdata[6].append(datetime.datetime.strptime(timestamp,
                                             '%Y-%m-%d %H:%M:%S.%f'))
        userdata[7].append(float(cpupct))
        
    if "Bingham/cpupct" in str(topic):                     # APPENDS INDEX 8 & 9 (in userdata)
        timestamp, cpupct = message.split('@@@')
        userdata[8].append(datetime.datetime.strptime(timestamp,
                                             '%Y-%m-%d %H:%M:%S.%f'))
        userdata[9].append(float(cpupct))

if __name__ == "__main__":
    
    # Create the lists to store data read from the broker
    times = []                  # ADDED LISTS FOR EACH SUBSCRIBER
    cpupcts = []

    times2 = []         
    cpupcts2 = []

    times3 = []
    cpupcts3 = []

    times4 = []
    cpupcts4 = []

    times5 = []
    cpupcts5 = []
    
    # Pass those lists to the client object so that it can update them
    client = mqtt.Client(userdata=[times, cpupcts, times2, cpupcts2, times3, cpupcts3, times4, cpupcts4, times5, cpupcts5])  # EACH SUBSCRIBER HAS A DIFFERENT SET OF LISTS TO STORE THERE DATA
    
    # Make the client aware of our callback functions
    client.on_connect = on_connect
    client.on_message = on_message

    client.connect("138.47.204.51", 1883, 60)
    fig = plt.figure()
    
    # Create some subplots in case we'd like to plot multiple sensor data at once.
    
    ax1 = fig.add_subplot(511)      #CREATED THE SUBPLOTS (ax1-ax5) WITH (5, 1) PARAMETERS
    ax2 = fig.add_subplot(512)      
    ax3 = fig.add_subplot(513)
    ax4 = fig.add_subplot(514)
    ax5 = fig.add_subplot(515)
    
    fig.tight_layout(pad = 1)       #SPECIFIES SPACING BETWEEN SUBPLOTS
    
    fig.suptitle("CPU PERCENTAGES OF ADVANCED COMPUTER NETWORKS STUDENTS")    #ADDS TITLE

    client.loop_start()

    Counter = 0

    while Counter < 60:     # 60 RUNTIME (NOT INFINITE ANYMORE)
        
        try:
            Counter += 1

            ax1.clear()
            ax1.plot(times, cpupcts, color = 'blue')   #PLOTS EACH LIST THAT WE CREATED FOR DATA FROM SUBSCRIBERS (color coded too)
            plt.gcf().autofmt_xdate()                  #I CHANGED plot_date() TO plot() IT HAS NO EFFECT ON THE TIME DATA BUT MAKES THE PLOTS IN A LINE FORMAT WITH LOOKS NICER

            ax2.clear()
            ax2.plot(times2, cpupcts2, color = 'red')
            plt.gcf().autofmt_xdate()

            ax3.clear()
            ax3.plot(times3, cpupcts3, color = 'yellow')
            plt.gcf().autofmt_xdate()

            ax4.clear()
            ax4.plot(times4, cpupcts4, color = 'green')
            plt.gcf().autofmt_xdate()

            ax5.clear()
            ax5.plot(times5, cpupcts5, color = 'orange')
            plt.gcf().autofmt_xdate()
            
            
            ax1.set_xlabel('Time')          #ADDS LABELS FOR EACH SUBPLOT
            ax1.set_ylabel("My CPU Usage(%)")
            
            ax2.set_xlabel('Time')                  
            ax2.set_ylabel("Damare CPU Usage(%)")
            
            ax3.set_xlabel('Time')
            ax3.set_ylabel("Miller CPU Usage(%)")
            
            ax4.set_xlabel('Time')
            ax4.set_ylabel("Markham CPU Usage(%)")
            
            ax5.set_xlabel('Time')
            ax5.set_ylabel("Bingham CPU Usage(%)")
            plt.pause(0.5)
            
        except(KeyboardInterrupt):
            # Exit cleanly if we hit ctrl-c
            client.loop_stop()
            client.disconnect()
            break
