import requests
import webbrowser
from bs4 import BeautifulSoup

loop = True
while True:
    search = str(input("enter species: "))
    if search == "quit()":
        break

    payload = dict(SearchString=search)
    e = requests.post("https://dyntaxa.se/?search=", data=payload)

    soup = BeautifulSoup(e.text, "html.parser")
    try:
        taxonID = soup.find(name="tbody").find(name="tr").find_all(name="td")[6].string
        name = soup.find(name="tbody").find(name="tr").find_all(name="td")[4].string
        rname = soup.find(name="tbody").find(name="tr").find_all(name="td")[2].string
        final_url = "https://artportalen.se/search/map/taxon/" + str(taxonID)

        webbrowser.open(final_url, new=0)
        print(name)
        print(rname)
    except:
        print("The search yieled no results.")
