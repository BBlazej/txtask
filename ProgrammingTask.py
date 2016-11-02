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
		
		empty = False
		while not empty:
			try:
				response = queue.get(True, 1)
				dom = html.fromstring(response)	
				threadLock.acquire()
				for link in dom.xpath('.//a'):
					if link:
						print link.get('href')
				threadLock.release()		
			except Queue.Empty:
				empty = True
		

if __name__ == '__main__':

	
   threadLock = threading.Lock()

   urls = ['http://www.sme.sk', 'http://www.pravda.sk','http://hasici-bystricany.webnode.sk','http://www.microstep.com','http://www.bbc.com','http://www.shmu.sk']
   queue = Queue.Queue(10)

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
