from bs4 import BeautifulSoup as soup
from urllib.request import Request, urlopen
import csv

class acer_scraper:
    for i in range(1,2): #Eigentlich range(1,37):
        my_url = 'https://de-store.acer.com/laptops?p=' + str(i)

        #Open URL and grabbing the page
        my_client = urlopen(my_url)
        page_html = my_client.read()
        my_client.close()

        #Parse the function
        page_soup = soup(page_html, "html.parser")

        filename = "products.csv"
        temp_array = []
        file = open(filename, 'w', newline='')
        writer = csv.writer(file)


        if i > 1:
            infile = open(filename)
            for line in infile:
                temp_array.append(line)
            infile.close()

       # f = open(filename,"w")

        #Add at the first time the headers
        if(i == 1):
            writer.writerow(["Marke", "Name", "Preis","Betriebsystem","Prozessor", "Grafikkarte", "Festplatte", "Arbeitsspeicher", "Displayart", "Displayauflösung", "Displaygröße", "Gewicht", "Akku Laufzeit", "Max. Stromversorgnung Wattleistung", "Maße"])

        #Add the items from previous pages
        for line in temp_array:
            f.write(line)


        #Grab the Containers with the information about the notebook
        containers = page_soup.findAll("li", {"class":"item"})
        for container in containers:
            product_name = container.a["title"]
            price_container = container.findAll("span", {"class" : "price"})
            product_price = price_container[0]["content"]

            #Noch aussourcen in eigene Methode
            technical_infos_container = containers[0].findAll("a", {"class" : "tracking-click"})
            technical_info = technical_infos_container[-1]["href"]
            technical_info_client = urlopen(technical_info)
            technical_info_html = technical_info_client.read()
            technical_info_soup = soup(technical_info_html, "html.parser") #Seite ist jetzt gesoupt
            
            #Ab jetzt weiter machen um die Ganzen Informationen rauszusuchen...

            info_container = technical_info_soup.find("div", {"class" : "product-collateral toggle-content tabs"})
            informations = {} #Create empty Dictonary to save the technical informations


            #print(info_container)
            tables = info_container.findChildren('table')
            rows = info_container.findChildren(['tr', 'td'])
            for row in rows:
                ths = row.findChildren('th')
                tds = row.findAll(['td'])
                for th in ths:
                    for td in tds:
                        td_value = td.string
                        th_value = th.string
                        if(td_value is not None and th_value is not None):
                            informations[th_value] = td_value
            
            CPU = informations["Prozessorhersteller"] + " " + informations["Prozessor"] + " " + informations["Prozessormodell"]+ " " + informations["Prozessorkern"] + " "+ informations["Prozessorgeschwindigkeit"]
            GPU = informations["Hersteller Grafikcontroller"] + " " + informations["Grafik-Controller-Modell"]
            festplatte = informations["Flash-Speicherkapazität"]
            arbeitsspeicher = informations["Speicher"] + " " + informations["Speichertechnologie"]
            betriebssystem = informations["Betriebssystem"]
            displayart = informations["Bildschirmtyp"]
            displayauflösung = informations["Bildschirmauflösung"]
            displaygröße = informations["Bildschirmdiagonale"]
            gewicht = informations["Gewicht (ungefähre)"]
            akku_laufzeit = informations["Akkulaufzeit"]
            netzteil = informations["Maximale Stromversorgung Wattleistung"]
            maße = "Höhe: " + informations["Höhe"] + " " + "Breite: " + informations["Breite"] + " " + "Tiefe: " + informations["Tiefe"]

            writer.writerow(["Acer", product_name, product_price,betriebssystem, CPU, GPU, festplatte, arbeitsspeicher, displayart, displayauflösung, displaygröße, gewicht, akku_laufzeit, netzteil, maße])
        file.close()


class lenovo_scraper:
    my_url = "https://www.lenovo.com/de/de/d/laptops-by-specs?sort=sortBy&currentResultsLayoutType=list"

    #Open URL and grabbing the page
    my_client = urlopen(my_url)
    page_html = my_client.read()
    my_client.close()

    #Parse the function
    page_soup = soup(page_html, "html.parser")

    filename = "products.csv"
    temp_array = []
    file = open(filename, 'w', newline='')
    writer = csv.writer(file)

    # if i > 1:
    #     infile = open(filename)
    #     for line in infile:
    #         temp_array.append(line)
    #     infile.close()

    # for line in temp_array:
    #     f.write(line)

    containers = page_soup.findAll("div", {"class" : "facetResults-l-item "})
    print(len(containers))


#acer_scraper
lenovo_scraper



