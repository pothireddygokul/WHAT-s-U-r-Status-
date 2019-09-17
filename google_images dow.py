from google_images_download import google_images_download 
import os
response = google_images_download.googleimagesdownload() 


search_queries =['best love quotes','best gym quotes','best education quotes','best friends quotes']  # use any keywords to search but use the same in main file!

def re_name(query): 
    i=1
    v="D:/codes/downloads/"+query+"/" 
    for file in os.listdir(v):
        des=str(i)+'.jpg'
        src= v+file
        des= v+des
        os.rename(src,des)
        i+=1
        
        
def downloadimages(query): 
    arguments = {"keywords": query,"format": "jpg","limit":5,"print_urls":True,"size": "large" }
				 
    try: 
        response.download(arguments) 
	 
    except FileNotFoundError: 
        arguments = {"keywords": query,"format": "jpg","limit":3,"print_urls":True,"size": "medium"} 
		
        try: 
            response.download(arguments) 
        except: 
            pass


for query in search_queries: 
    downloadimages(query)
    re_name(query)
    print() 
