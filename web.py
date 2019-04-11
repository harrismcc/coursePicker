#course catalog query for keyword "MLLC"
#cur_cat_oid=7&search_database=Search&search_db=Search&cpage=1&ecpage=1&ppage=1&spage=1&tpage=1&location=3&filter%5Bkeyword%5D=MLLC&filter%5Bexact_match%5D=1
import requests

url = "http://catalog.pitzer.edu/search_advanced.php?"

params = {"filter%5Bkeyword%5D" : "MLLC"}

# sending get request and saving the response as response object 
r = requests.get(url = url, params = params) 
  
# extracting data in json format 
data = r.json() 

print(data)