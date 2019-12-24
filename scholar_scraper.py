from bs4 import BeautifulSoup as Soup
import requests
# import csv

page_url = "https://scholar.google.com/scholar?hl=en&as_sdt=0%2C14&q=deep+learning+in+neural+networks&oq="
r = requests.get(page_url)
souped = Soup(r.text, 'html.parser')

# print(souped.prettify())

containers = souped.findAll("div", {"class": "gs_r gs_or gs_scl"})
# search_cont = souped.findAll("div", {"class":"gs_in_txtw gs_in_txtb gs_in_acw"})
search_cont = souped.findAll("div", {"id": "gs_hdr_srch"})

container = containers[0]
cont = search_cont[0]

# out_filename = "for_journal_club.csv"
# headers = "search_keyword, article_name, author, summary, url_link, Number_of_citations  \n"
# opens file, and writes headers
# f = open(out_filename, "w")
# f.write(headers)

search_keyword = cont.form.div.input["value"]


for container in containers:
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



