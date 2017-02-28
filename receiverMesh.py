#!/usr/bin/env python

# from __future__ import print_function
import time
from RF24 import *
import base64
import pdb
import RPi.GPIO as GPIO
import os, sys
import struct
import binascii

irq_gpio_pin = None

radio = RF24(22, 0)
pipes = ["1Node", "2Node"]


def setup():
    radio.begin()
    radio.payloadSize = 6
    radio.enableDynamicPayloads()
    radio.setAutoAck(1)
    radio.setDataRate(RF24_250KBPS)  # 250kbs
    radio.setPALevel(RF24_PA_MAX)
    radio.setChannel(90)
    radio.setRetries(15, 15)
    radio.setCRCLength(RF24_CRC_16)
    radio.openWritingPipe(pipes[0])
    radio.openReadingPipe(1, pipes[0])
    # radio.maskIRQ(0,0,1)
    radio.startListening()


def writeToFile(received_payload):
    #print('Got payload size={} value="{}"'.format(radio.payloadSize, received_payload.decode('utf-8')))

    # Timestamp erzeugen
    utime = int(time.time())

    # Hier aktuelle Zeit einfuegen
    data.write("1481278800" + " " + received_payload + " \n")  # % utime
    data.flush()



def receive():
    if radio.available():
        while radio.available():
            receive_payload = radio.read(radio.payloadSize)
            #print "%s" % receive_payload
            writeToFile(receive_payload)


# Hauptprogramm:
setup()
radio.printDetails()
data = open('data', 'a+')
print(" \n Hauptprogramm:")
while 1:
    receive()

    # spaeter durch interrupt ersetzten
    time.sleep(1)
data.close()
