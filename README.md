# Google Apps Script Automation Project

This software works with Google Apps Script https://script.google.com

The 'main.py' python script utilizes the 1secmail API to generate a dummy mailbox and continuously monitor it for incoming emails.
Upon receiving an email, the script extracts any URLs present and utilizes these to retrieve the desired content from the respective URLs for analysis. 
The results of this analysis can be accessed via API call.

The 'script.js' file works with Google Apps Script to programatically create the documents, aggregate them, and share via email.

