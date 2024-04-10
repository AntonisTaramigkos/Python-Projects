#import bs4
import requests

result = requests.get("https://www.videoschool.com/")


soup =bs4.BeautifulSoup(result.text,"html.parser")
images = soup.select("img")
for im in images:
    print(im)
# central_block = soup.select('.fusion-text.fusion-text-1 h5')
# #print(central_block)

# for h in central_block:
#     print(h.getText())