from bs4 import BeautifulSoup
import requests
import re

out_filename = "for_journal_club.csv"
f = open(out_filename, "w", encoding='utf-8-sig')
headers = "search_keyword, article_name, author, summary, url_link, Number_of_citations \n"
# opens file, and writes headers
f.write(headers)

for i in range(5):
    # for the number of pages to scraped
    page_url = "https://scholar.google.com/scholar?start={}&q=deep+learning+in+neural+networks&hl=en&as_sdt=400007".format(i)
    r = requests.get(page_url)
    souped = BeautifulSoup(r.text, 'html.parser')
    # inspect elements from the webpage to locate
    containers = souped.findAll("div", {"class": "gs_r gs_or gs_scl"})
    search_cont = souped.findAll("div", {"id": "gs_hdr_srch"})
    cont = search_cont[0]
    search_keyword = cont.form.div.input["value"]

    for container in containers:
        # for number of occurrences of each element type on the webpage
        article_name = container.select("div")[3].h3.a.text
        author = container.select("div")[3].div.a.text
        summary = container.select("div")[3].select("div")[1].text
        url_link = container.div.div.div.a["href"]
        Number_of_citations = container.select("div")[3].select("div")[2].select("a")[2].text

        print("article_name:" + article_name + "\n")
        print("author:" + author + "\n")
        print("summary:" + summary + "\n")
        print("url_link:" + url_link + "\n")
        print("Number_of_citations:" + Number_of_citations + "\n")

        f.write(search_keyword + "," + article_name.replace(",", "") + "," + author + "," + re.sub('[^A-Za-z0-9]+', " ", summary) + "," + url_link + "," + re.sub("[^0-9]", "", Number_of_citations) + "\n")
f.close()
