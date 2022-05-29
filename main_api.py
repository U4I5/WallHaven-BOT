#Bot make by U4I5 | Github

#Module importation 
import os
import time
import random
import schedule
from wallhaven.api import Wallhaven

# set your api here 
wallhaven = Wallhaven(api_key="bxxxxxxxxxxxxxxxxxxxxxr")

# the fonction to download Wallpaper and all other settings
def download():
  pass
  wallhaven.params["sorting"] = "views"
  wallhaven.params["categories"] = "100"
  wallhaven.params["atleast"] = "1920x1080"
  wallhaven.params["ratios"] = '16x9,16x10'
  wallhaven.params["page"] = random.randint (1,450)
  results = wallhaven.search()
  for wallpaper in results.data:
      wallpaper.save(os.path.dirname('/home/dark/Pictures/Wall Data/'))
  
# For repeat process every 4 hours or time you can set
schedule.every(1).hour.do(download())

while True:
    schedule.run_pending()
    time.sleep(1)


