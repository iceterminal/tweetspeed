# tweetspeed
Tweet your internet speed when it falls below XX mpbs. Notify your ISP via twitter.
  
This script will run a command line internet speed test, and then log it locally as well as TWEET the slow results to your ISP via twitter. Can be manual or automatic.
  
### Steps  
First, create a Twitter application. Go to https://apps.twitter.com/ and click on Create New App.  
After creating the application, click on the tab that says Keys and Access Tokens.   
Generate the Consumer Key and Secret.  
Also, generate the Access Token and Token Secret. Do not give these values to anyone.  
Click on the tab Permissions and set the access to Read and Write.  
  
Download the speedtest.net command line script speedtest.py or from https://github.com/sivel/speedtest-cli/blob/master/speedtest.py. Save it in a directory of your choice.  
  
Edit tweetspeed.py and change it to fit your needs.  
Input your specific TOKEN_KEY, TOKEN, CON_SEC_KEY, and CON_SEC.  
  
I suggest creating a virtualenv for this & run it manually. Or create a cronjob and run it hourly to bug the piss out of your ISP on slow speeds. It helped me convince Frontier to fix my speeds.
  
From command line: `python3 tweetspeed.py`
  
NOTE: if you're not able to send a tweet from this script, switch the values of TOKEN_KEY and TOKEN, and CON_SEC_KEY and CON_SEC (I got them backwards myself).  

