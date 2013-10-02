UDPOC
=====

POC to check availability of SO_REUSEADDRESS on UDP sockets

HOW TO
-----

Install two apk on your phone. There are the same, only change is android app id.

Open Both (one by one) and click on start. Socket is started at port 8500 on both cases. Click home to send app to background.

Now you can check logcat with:

adb logcat | grep TiAPI

Or launch broadcast.py that send broadcast message every 2 seconds. Then you can see on the apps every message received.

Both apps listening on same HOST and PLATFORM. 

Trick is use SO_REUSEADDRESS.

More info:

http://stackoverflow.com/questions/14388706/socket-options-so-reuseaddr-and-so-reuseport-how-do-they-differ-do-they-mean-t

I use appcelerator udp module with some modifications.
