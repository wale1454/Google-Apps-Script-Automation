import json, requests
from flask import Flask, request, jsonify
from goose3 import Goose
import re

# This script utilizes the 1secmail API to generate a dummy mailbox and continuously monitor it for incoming emails. 
# Upon receiving an email, the script extracts any URLs present and utilizes these to retrieve the desired content from the respective URLs for analysis. 
# The results of this analysis can be accessed via API call.


# Init app
app = Flask(__name__)

# Flask maps HTTP requests to Python functions.
# The process of mapping URLs to functions is called routing.

@app.route('/', methods=['GET'])
def home():
    ghDict2 = { "Results": [ ]
                }
    # the mailbox address would be 'mailboxUsername@1secmail.com'
    mailboxUsername = "INSERT USERNAME HERE" 


    #Gets all the messages from the mailbox with a GET request.
    url1 = f"https://www.1secmail.com/api/v1/?action=getMessages&login={mailboxUsername}&domain=1secmail.com"
    urlContent= requests.get(url1).json()

    # Get the ID of the most recent email that came in.
    lastEmailID = urlContent[0]["id"]


    # With the ID of the last email, we check the content of the last email with another GET request.
    # We then use a regex func. to find all the URLs in the content of the email.
    
    url5 = f"https://www.1secmail.com/api/v1/?action=readMessage&login=wiley123&domain=1secmail.com&id={lastEmailID}"
    content  = requests.get(url5).json()
    emailUrl = content["textBody"]

    def Find(string):
    # findall() has been used, with valid conditions for urls in string.
    # we then put all the URLs into a list. 
      
      regex = r"(?i)\b((?:https?://|www\d{0,3}[.]|[a-z0-9.\-]+[.][a-z]{2,4}/)(?:[^\s()<>]+|\(([^\s()<>]+|(\([^\s()<>]+\)))*\))+(?:\(([^\s()<>]+|(\([^\s()<>]+\)))*\)|[^\s`!()\[\]{};:'\".,<>?«»“”‘’]))"
      url = re.findall(regex,string)	
      return [x[0] for x in url]

    NewUrlList = Find(emailUrl)


  # Looping through the list, for each URL we get the article name, article content, and then pass it into a dictionary
  #  The dictionary is then Jsonized and returned when then API is called. 
  
    for j  in NewUrlList:
        # Gets the title of the article
        g = Goose()
        article = g.extract(url=j)
        articleName = article.title

        articleBody = article.cleaned_text
        # articleBody = articleBody1.replace("\n", " ")

        eachContent = {}
        eachContent["artcBody"] = articleBody
        eachContent["artcName"] = articleName



        ghDict2["Results"].append(eachContent)
    return jsonify(ghDict2)

