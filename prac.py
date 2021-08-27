# import urllib library
from urllib.request import urlopen

# import json
import json
# store the URL in url as
# parameter for urlopen
url = "https://www.google.com/url?sa=t&rct=j&q=&esrc=s&source=web&cd=&cad=rja&uact=8&ved=2ahUKEwjrgeHe1NHyAhXIFLcAHZigAvsQFnoECAsQAw&url=https%3A%2F%2Fwww.cowin.gov.in%2F&usg=AOvVaw3X3uxskawBi-3TuAjqT2-m"

# store the response of URL
response = urlopen(url)

# storing the JSON response
# from url in data
data_json = json.loads(response.read())

# print the json response
print(data_json)
