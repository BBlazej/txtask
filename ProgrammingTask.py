#!/usr/bin/env python

import requests
import Queue
import threading
from lxml import html

class Producer(object):
	def __init__(self, queue):
        	self.queue = queue

	def __call__(self, urls):
    		for url in urls:
       			page = requests.get(url)	
        		queue.put(page.text)

class Consumer(object):
	def __init__(self, queue):
        	self.queue = queue
	def __call__(self):
		threadLock.acquire()
		empty = False
		while not empty:
			try:
				response = queue.get(True, 4)
				dom = html.fromstring(response)	
				for link in dom.xpath('.//a'):
					if link:
						print link.get('href')
						
			except Queue.Empty:
				empty = True
		threadLock.release()

if __name__ == '__main__':

    threadLock = threading.Lock()

    urls = ['http://www.yahoo.com', 'http://manadartblog.tumblr.com']
    queue = Queue.Queue()

    prod = Producer(queue)
    pthread = threading.Thread(target=prod, args=[urls])
  
    con = Consumer(queue)
    cthread = threading.Thread(target=con)
	cthread2 = threading.Thread(target=con)

    pthread.start()
    cthread.start()
	cthread2.start()
	
    pthread.join()
    cthread.join()
	cthread2.join()
