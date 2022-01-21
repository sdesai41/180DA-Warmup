import paho.mqtt.client as mqtt

#define callbacks-functions that run when events happen.
#the callback fir when the clieant recieves a CONNACK response from the server
def on_connect(client,userdata,flags,rc):
    print("Connection returned result: " + str(rc))
    #subscribing in on_connect() means that if we lose the connection and reconnect then subscriptions will be renewed
    client.subscribe("ece180d/test",qos=1)
    client.subscribe("ece180d/team2",qos=1)
#the callback of the client when it disconnects
def on_disconnect(client, userdata,rc):
    if rc!=0:
        print('unexpected disconnect')
    else:
        print('expected disconnect')

#default message callback
def on_message(client, userdata,message):
    print('recieved message:" '+str(message.payload)+ '" on topic "' + message.topic + '" With qos' +str(message.qos))

#1. create client instance.
client=mqtt.Client()
#add addiontal client optinons (security, certs, etc)
#many defaults good to start
#add callbacks to clients
client.on_connect=on_connect
client.on_disconnect=on_disconnect
client.on_message=on_message
#2. connect to broker using one of the connect*() functions
client.connect_async("test.mosquitto.org")
#3. call one of the loop*() functions to maintain network traffic
client.loop_start()
while True: #add stopping condition?
    pass #do nonblocked activities
    #use subscribbe to subscribe to topic
    #use publish to publish a message to broke
    #use disconnect to disconnect from broker

client.loop_stop()
client.disconnect()
