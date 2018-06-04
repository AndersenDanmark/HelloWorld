
driver=webdriver.Firefox(executable_path=DRIVER_EXE)
page_number=0
for page_number in range(0,3):
    
    mydict={'q':job_search_keywords,
           'l':job_search_location,
            'sort':job_search_sortbydate,
           'start':search_result_pg}

    resp_make_url=requests.get(base_url,params=mydict)
    
    searched_url=resp_make_url.url
    
    
#loop through one page of searched results:
    
    #creating a response object called resp
    resp = requests.get(searched_url)

    #You can find out what encoding Requests is using, and change it, using the r.encoding property
    #print(resp.encoding)

    # Running the url link through BeautifulSoup give us a BeautifulSoup object, which represents the document as a nested data structure.
    start_soup = BeautifulSoup(resp.content)
    urls = start_soup.findAll('a',{'rel':'nofollow','target':'_blank'}) #this are the links of the job posts

    urls = [link['href'] for link in urls] 
    
    #print job links of the current search result page:

        
    for i in range(len(urls)): #change it back to for i in range(len(urls)): 
        get_info = True
        try:
            driver.get(original_url+urls[i]) #The driver.get method will navigate to a page given by the URL.
        except TimeoutException:
            get_info = False
        except IndexError:
            get_info = False
            continue
        j = random.randint(1000,2200)/1000.0


        time.sleep(j) #waits for a random time so that the website don't consider you as a bot


        if get_info:
            soup=BeautifulSoup(driver.page_source)

            #head_tag=soup.head.title

            #title_tag = head_tag.contents[0]

            #print(title_tag)


            #job_title=soup.b.string
           
            job_title=soup.find_all("b",{"class":"jobtitle"})[0]              
            print(job_title.text)


            company=soup.find_all("span",{"class":"company"})[0]
            print(company.text)

            location=soup.find_all("span",{"class":"location"})[0]
            print(location.text)

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
            collection.insert(jobs)
            
    
#move to the next page of searched results
    search_result_pg+=10
    #print(page_number)
    
    #print(searched_url) # print urls for search result page 1, 2 ,3