
# coding: utf-8

# In[78]:


import re
from nltk.corpus import stopwords
from goose3 import Goose
from bs4 import BeautifulSoup
from selenium import webdriver
from selenium.common.exceptions import *
import time
import requests
import random
import pandas as pd
import matplotlib.pyplot as plt
import csv
import pymongo
from pymongo import MongoClient
import json
import pprint


# In[79]:


base_url = "https://www.bloomberg.com"    
#change the start_url can scrape different cities.
start_url = "http://www.indeed.com/jobs?q=data+scientist&l=San+Francisco%2C+CA"

#creating a response object called resp
resp = requests.get(start_url)

#You can find out what encoding Requests is using, and change it, using the r.encoding property
#print(resp.encoding)

# Running the url link through BeautifulSoup give us a BeautifulSoup object, which represents the document as a nested data structure.
start_soup = BeautifulSoup(resp.content)
urls = start_soup.findAll('a',{'rel':'nofollow','target':'_blank'}) #this are the links of the job posts


# In[80]:


urls[0]


# In[81]:


#To store all url links to a list called links.
#urls=[]
#for link in urls:
#    urls.append(link.get('href'))
#print(urls[0:2])


# In[82]:


urls = [link['href'] for link in urls] 


# In[83]:


# prevent the driver stopping due to the unexpectedAlertBehaviour.
webdriver.DesiredCapabilities.FIREFOX["unexpectedAlertBehaviour"] = "accept"
get_info = True

DRIVER_EXE = r"C:\Users\Andrew Yan\Documents\GitHub\data_skills\geckodriver.exe"
#the instance of Firefox WebDriver is created.


# In[84]:


driver=webdriver.Firefox(executable_path=DRIVER_EXE)


# In[85]:


# set a page load time limit so that don't have to wait forever if the links are broken.
driver.set_page_load_timeout(15) 
for i in range(1): #change it back to for i in range(len(urls)): 
    get_info = True
    try:
        driver.get(base_url+urls[i]) #The driver.get method will navigate to a page given by the URL.
    except TimeoutException:
        get_info = False
        continue
    j = random.randint(1000,2200)/1000.0
    time.sleep(j) #waits for a random time so that the website don't consider you as a bot
    if get_info:
        soup=BeautifulSoup(driver.page_source)
        
        head_tag=soup.head.title
        
        title_tag = head_tag.contents[0]
        
        print(title_tag)
        
        
        #job_title=soup.b.string
        
        job_title=soup.find_all("b",{"class":"jobtitle"})[0]              
        #print(job_title.text)
        
    
        company=soup.find_all("span",{"class":"company"})[0]
        #print(company.text)
        
        location=soup.find_all("span",{"class":"location"})[0]
        #print(location.text)
        
        job_description=soup.find_all("span",{"id":"job_summary"})[0]
       
        #print(job_description.text)

        #print (driver.current_url)
        
        
        jobs={
            
            "Job Title":job_title.text,
            "Company Name":company.text,
            "Location":location.text,
            "Url":driver.current_url,
            "Job Description":job_description.text
            
        }
        
        
        print(jobs)
        
driver.quit()
    


# In[87]:


jobs={

"Job Title":job_title.text,
"Company Name":company.text,
"Location":location.text,
"Url":driver.current_url,
"Job Description":job_description.text

}

'''
#build connection
client = MongoClient('mongodb://127.0.0.1:27017')


#creating a database called jobs_database
db = client.jobs_database

#creating a collection (table) called collection
collection = db.jobs_collection

job_id = db.collection.insert_one(jobs).inserted_id
collection.find_one({"Job Title": "Data Scientist"})
'''

def readFromMongoDB(heroku_zdtgskz7, datasciencejobs, ID):
    
    ID = int(ID)
    client =MongoClient("mongodb://andrewyan:andrewyan!23@ds237660.mlab.com:37660/heroku_zdtgskz7")
    mydb = client[heroku_zdtgskz7]
    qry = {"ID": ID}
    obj = mydb[datasciencejobs].find_one(qry,{'_id': False}) # the second parameter {'_id': False} causes the objectID not to be returned
    #print('Mongo obj:', obj)
    client.close()
    return obj
'''
{
    "_id": "heroku_zdtgskz7.andrewyan",
    "user": "andrewyan",
    "db": "heroku_zdtgskz7",
    "roles": [
        {
            "role": "dbOwner",
            "db": "heroku_zdtgskz7"
        }
    ]
}

'''
def writeToMongoDB(heroku_zdtgskz7, datasciencejobs, ID, jobs):

    ID = int(ID)
    client =MongoClient("mongodb://andrewyan:andrewyan!23@ds237660.mlab.com:37660/heroku_zdtgskz7")
    #client = MongoClient("mongodb://localhost:27017/")

    # Connect to DB:
    # mydb = client.heroku_dgltjp2d
    mydb = client[heroku_zdtgskz7]

    obj = json.loads(jobs)

    doc = { "ID":ID, "value" : obj }
    
    
    # if this ID doesnt exist yet, insert a new one
    #mydb[_tableName].insert_one(doc)
    
    # if this ID already exists, we will need to update it with a new value
    # mycollection.update({'_id':mongo_id}, {"$set": post}, upsert=False)
    mydb[db].update({ 'ID':ID }, doc, upsert=True )
    
    client.close()

    return

writeToMongoDB(heroku_zdtgskz7, datasciencejobs, ID, jobs)

pprint.pprint(collection.find_one())

