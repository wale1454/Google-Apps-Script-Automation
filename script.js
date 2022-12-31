
function AppsScriptAutomation(){

// Calls the api and uses the response to create and populate a google docs document.

// Get's api endpoint
var response = UrlFetchApp.fetch(" INSERT API ENDPOINT HERE ");

var jsonn = response.getContentText();   // get the response content as text
var data1 = JSON.parse(jsonn);   //parse text into json


// List of responses ( Title and body in the API as a list object)
Results1 = data1["Results"] ;
// console.log(Results1[1]["artcName"])

// No of URLs/ articles
var arrayLength = Results1.length;

console.log("Number of article = :" , arrayLength) ;

let ListURLs = "-"


var style = {};

  // style[DocumentApp.Attribute.FONT_FAMILY] = 'Calibri';
  style[DocumentApp.Attribute.FONT_SIZE] = 25;
  style[DocumentApp.Attribute.BOLD] = true;
  style[DocumentApp.Attribute.FOREGROUND_COLOR ] = "#963d3d"


for (var i = 0; i < arrayLength; i++) {

  DocName1 = Results1[i]["artcName"] ;
  DocBody1 =  Results1[i]["artcBody"] ;

    const newDocu = DocumentApp.create( DocName1 );

    newDocu.getBody().appendParagraph(DocName1) ;


    newDocu.getBody().appendParagraph("   ----  ") ;
    
    newDocu.getBody().appendParagraph(DocBody1) ;

    const urLink = newDocu.getUrl();

    ListURLs = ListURLs + urLink + " - , - "

    console.log("Documents created");

  }

const emailperson = Session.getActiveUser().getEmail();

bodyEmail = " Hello " + emailperson + "\n" + "\n" + "Here's a list of your URLs" + ListURLs 

const subject = " List of Publications in Google docs " ;

GmailApp.sendEmail(emailperson, subject, bodyEmail);


}

