import time
import random
from datetime import datetime as dt
# to fix windows paths for python use raw strings r'this\is\raw\string'

output_path = 'regular_output.txt'

phrases = ['Here I come', 'Out of my way people!', 'No one expects the Spanish inquisition!!']

def process_file(handler):
    phrase = random.choice(phrases)
    fhandler.write('\n')
    fhandler.write(phrase)
    content = fhandler.read()
    print(content)

fh = open(output_path, 'r+')

while True:
   if dt(dt.now().year, dt.now().month, dt.now().day, 1) < dt.now() < dt(dt.now().year, dt.now().month, dt.now().day, 3):
       
       phrase = random.choice(phrases)
       print(str(dt.now()))
       fh.write(phrase)
       fh.write('\n')
       content = fh.read()
       print(content)


   time.sleep(5)


