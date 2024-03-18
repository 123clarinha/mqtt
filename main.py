import paho.mqtt.client as mqtt

def ao_conectar(cliente, userdata, flags, rc):
    print("Nos conectamos com o seguinte codigo de resultado {}".format(str(rc)))


def ao_receber(cliente, userdata, msg):
    print("{} --- {}".format(msg.topic, str(msg.payload)))
