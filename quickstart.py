from scrapy import cmdline
import os
from datetime import datetime
import time
count = 0
while (count < 2):
    os.system("scrapy crawl vote -o database/vote.json")
    count = count+1
