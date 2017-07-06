# tweetspeed
Tweet your internet speed when it falls below XX mpbs. Notify your ISP via twitter.


### Steps  
First, create a Twitter application. Go to https://apps.twitter.com/ and click on Create New App.  
After creating the application, click on the tab that says Keys and Access Tokens.   
Generate the Consumer Key and Secret.  
Also, generate the Access Token and Token Secret. Do not give these values to anyone.  
Click on the tab Permissions and set the access to Read and Write.  
  
Download the speedtest.net command line script speedtest.py from https://github.com/sivel/speedtest-cli/blob/master/speedtest.py. Save it in a directory of your choice.  
  
Edit tweetspeed.py and change it to fit your needs.  
Input your specific TOKEN_KEY, TOKEN, CON_SEC_KEY, and CON_SEC.  
NOTE: if you're not able to send a tweet from this script, switch the values of TOKEN_KEY and TOKEN, and CON_SEC_KEY and CON_SEC (I got them backwards myself).  

