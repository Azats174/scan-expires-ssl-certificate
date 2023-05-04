#!/usr/bin/python3
import datetime
import os
import calendar
import sys
import smtplib
import subprocess
from dateutil import parser
import argparse
from urllib.request import ssl, socket

arg = argparse.ArgumentParser(description='server name and  port')
arg.add_argument('hostname', type=str, help="server name")
arg.add_argument('port', type=int, help="server port")
args = arg.parse_args()
hostname = args.hostname
port = args.port
#
if  port == 443:
    context = ssl.create_default_context()

    with socket.create_connection((hostname, port)) as sock:
       with context.wrap_socket(sock, server_hostname=hostname) as ssock:
          certificate = ssock.getpeercert()

          certExpires = datetime.datetime.strptime(certificate['notAfter'], '%b %d %H:%M:%S %Y %Z')

          daysToExpiration = (certExpires - datetime.datetime.now()).days

          print(daysToExpiration)
#          os.system(f'echo {daysToExpiration}')


elif  port == 25:
# Connect to the SMTP server and start TLS
    smtp_conn = smtplib.SMTP(hostname, port)
    smtp_conn.starttls(context=ssl.create_default_context())
# Get the SSL certificate
    certificate = smtp_conn.sock.getpeercert()
# Extract the SSL certificate expiry date
    certExpires = datetime.datetime.strptime(certificate['notAfter'], '%b %d %H:%M:%S %Y %Z')

# Get the current date and time
# Calculate the number of days until the SSL certificate expires

    daysToExpiration = (certExpires - datetime.datetime.now()).days

# Print the number of days until the SSL certificate expires
    print(daysToExpiration)
# Close the SMTP connection
    smtp_conn.quit()
else: 
     print("error")
