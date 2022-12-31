# Google Apps Script Automation Project

I built this project to automate a process at my work, and I decided to make it open source.

--

It allows you to easily create as many Google Docs documents as you want, and populate each document with scraped content from a list of News Publication URLs.

All you have to do is send an email to a designated mailbox, This email may contain as many article links as possible.

--

This software works with Google Apps Script https://script.google.com

The 'main.py' python script utilizes the 1secmail API to generate a dummy mailbox and continuously monitor it for incoming emails.
Upon receiving an email, the script extracts any URLs present and utilizes these to retrieve the desired content from the respective URLs for analysis. 
The results of this analysis can be accessed via API call.

The 'script.js' file works with Google Apps Script to programatically create the documents, aggregate them, and share via email.

### How to setup.

You can easily fork this repo on replit https://replit.com/@Olawale4444/Flask-API.
You'd also need to insert a Username for the Mailbox in the replit main.py file.


Send an email with all the required URLs included to the email address from the main.py file

Open Google Drive and create a new Google Apps Script file. You can do this by going to "New" > "More" > "Google Apps Script".

Finally, you'd need to copy /paste the contents of script.js into your Google Apps Script file, save it and click "Run" 

You're all set.


### How it works

- An email is sent to the designated mailbox with as many news publication article links as possible.
- When the API endpoint is called by script.js, The main.py script checks the mailbox for the latest email, and scans for any URLs in the email.
- It then returns the required content of the URL in json format as a response.
- The scripts.js file then programmaticaly creates the Google Docs populated with the required content.


