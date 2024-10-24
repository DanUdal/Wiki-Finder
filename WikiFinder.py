import urllib3

http = urllib3.PoolManager()

wiki = http.request('GET', 'https://en.wikipedia.org/wiki/Special:Random')

string = wiki.data.decode("utf-8")

start = string.find("firstHeading")

end = string.find("<", start)

title = string[start:end]

newStart = title.find(">")

title = title[newStart + 1:]

url = "https://en.wikipedia.org/wiki/" + title.replace(" ", "_")

print("The title of the page is ", title)
answer = input("Would you like to go to this page? Y/N: ")
while True:
    if answer == "Y":
        print("The url for the page is", url)
        break
    else:
        if answer == "N":
            print("Thank you for using this service")
            break
    answer = input("Please answer Y/N: ")