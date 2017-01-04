import requests
from bs4 import BeautifulSoup 

# Main crawler function to scrape the webpages:
# max_pages denote the no of pages to be scraped
def crawler(max_pages):
    page = 1
    while page <= max_pages:
        url = 'http://www.snapdeal.com/product/apple-macbook-pro-13-inch/199160/reviews?page='\
        + str(page)\
        + '&sortBy=HELPFUL#defRevPDP'
        
        source_code = requests.get(url) # Get the source code of the webpage
        plain_text = source_code.text   # Get all the text from the source code
        #print(plain_text)

        bsobj = BeautifulSoup(plain_text, "html.parser")  # Create a BeutifulSoup object
        
        for main in bsobj.findAll('div', {'class': 'user-review'}): 
            p = main.get_text()         #Find text according to tags 
            #print(p)
            
            #Write all the reviews to a text file.
            with open("reviews.txt","a") as myfile:
                    myfile.write(p)

        print ("Scraping Page number {}".format(page))        
        page += 1

                
crawler(25)
#myfile.close()
