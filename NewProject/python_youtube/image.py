import random
import urllib.request

def download_web_image(url):
    name= random.randrange(1,1000);
    file_name = str(name) +".jpeg"
    urllib.request.urlretrieve(url,file_name);

download_web_image("https://www.google.co.in/url?sa=i&rct=j&q=&esrc=s&source=images&cd=&cad=rja&uact=8&ved=0ahUKEwj3nsPU9OTQAhUFrY8KHUC1Af4QjRwIBw&url=https%3A%2F%2Fcommons.wikimedia.org%2Fwiki%2FFile%3AAsclepias_Curassavica_(Macro).jpeg&psig=AFQjCNGENkcRW4zifMhdvpxyCdamiVHDnw&ust=1481297285702752");