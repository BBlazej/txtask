# txtask

What is it?
___________


Is is a programming task, which was given to me by Joe when i applied for a job
of a programmer. This script, have a list of URLs, it extracts the
markup from each of them and then it print out all the hyperlinks if founds.

How does it do it?
__________________


It have two classes each on one threads. The producer is downloading the markup to 
queue and The Consumer parses the markup and prints out the hyperlinks. These two 
classes are running concurrently. As a locking mechanism they use automated
lockings from queue.

Used libraries
______________


requests: 
Requests allow you to send HTTP/1.1 requests. You can add headers, form data, 
multipart files, and parameters with simple Python dictionaries, and access the
response data in the same way. It’s powered by httplib and urllib3, but it does 
all the hard work and crazy hacks for you.
https://pypi.python.org/pypi/requests

Queue:
The Queue module implements multi-producer, multi-consumer queues. It is 
especially useful in threaded programming when information must be exchanged 
safely between multiple threads. The Queue class in this module implements all
the required locking semantics.
https://docs.python.org/2/library/queue.html

threading:
This module constructs higher-level threading interfaces on top of the lower 
level _thread module. 
https://docs.python.org/3/library/threading.html

lxml: 
The lxml XML toolkit is a Pythonic binding for the C libraries libxml2 and 
libxslt. It is unique in that it combines the speed and XML feature completeness
of these libraries with the simplicity of a native Python API, mostly compatible
but superior to the well-known ElementTree API. The latest release works with all
CPython versions from 2.6 to 3.5. See the introduction for more information about 
background and goals of the lxml project.
http://lxml.de/

Contact
_______


bbajzik@gmil.com



