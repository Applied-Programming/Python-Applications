import requests
import operator
from bs4 import BeautifulSoup

# Scrape the webpage using the given URL
def scrape(url):
    word_list = []
    source_code = requests.get(url).text  #Get the source code of the webpage
    soup = BeautifulSoup(source_code,"html.parser") # Create a bs4 object

    #Find text by tags
    for post_text in soup.findAll('div', {'class': 'head'}):
        content = post_text.string        #Get the text
        words = content.lower().split()   #Convert all text into lowercase  
        for each_word in words:
            word_list.append(each_word)   #Add to word_list  
    clean_list(word_list)

# Remove extra characters from words
def clean_list(word_list):
    clean_word_list = []
    for each_word in word_list:
        # Define symbols that ought to be removed
        symbols = "!@#$%^&*()_+{}:\"<>?,./;'[]-='"
        for i in range(0,len(symbols)):
            each_word = each_word.replace(symbols[i],"") 
        if len(each_word) > 0:
            #print(each_word)
            clean_word_list.append(each_word) #Add to clean_word_list
    create_dictionary(clean_word_list)


# Create python dictionary of {words : count}
def create_dictionary(clean_word_list):
    word_count = {}
    for each_word in clean_word_list:
        if each_word in word_count:
            word_count[each_word] = word_count[each_word] + 1
        else:
            word_count[each_word] = 1

    # Print the dictionary elements    
    for key,value in sorted(word_count.items(), key=operator.itemgetter(1)):
        print(key,value)

scrape('http://www.snapdeal.com/product/apple-macbook-pro-13-inch/199160/reviews?page=5')
