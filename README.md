# scan-expires-ssl-certificate
This python script  check  expires certificate.
This script support for different ports (443 and 25 in this case) and used the appropriate protocol (HTTPS and SMTP) to connect to the server. I use ssl.create_default_context() to create a default SSL/TLS context and socket.create_connection() to create a socket connection for HTTPS and use smtplib.SMTP() and starttls() to connect to the SMTP server and issue the STARTTLS command to switch to SSL/TLS.

And scripts extract the SSL certificate expiry date as before and calculated the number of days until it expires. Finally, you have printed the number of days until the SSL certificate expires.

Run ./ssl_check.py  hostname port
