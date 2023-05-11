#!/usr/bin/python3
import os

if __name__ == "__main__":

    message = "#pythoniscool\n"
    message_bytes = message.encode('utf-8')
    os.write(1, message_bytes)
