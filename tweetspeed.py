#!/usr/bin/python3
import os
import sys
import csv
import datetime
import time
import twitter

def test():

        #run speedtest-cli
        print ('Running tests in background. Please be patient')
        #change directory path where speedtest.py exists
        a = os.popen("python /tweetspeed/speedtest.py --simple").read()
        print ('Speedtest CLI complete. Running traceroute now.')
        # point traceroute to your ISP i.e. comcast.com or spectrum.com
        b = os.popen("traceroute frontier.com").read()
        #split the 3 line result (ping,down,up)
        lines = a.split('\n')
        print (a)
        print (b)
        print ('Speedtest CLI  & Traceroute complete')

        ts = time.time()
        date =datetime.datetime.fromtimestamp(ts).strftime('%Y-%m-%d %H:%M:%S')
        #if speedtest could not connect set the speeds to 0
        if "Cannot" in a:
                p = 100
                d = 0
                u = 0
        #extract the values for ping down and up values
        else:
                p = lines[0][6:11]
                d = lines[1][10:14]
                u = lines[2][8:12]

        #save the data to local file for logging purposes 
        out_file = open('/home/username/tweetspeed/data.csv', 'a', newline='')
        writer = csv.writer(out_file)
        writer.writerow([date, p, d, u])
        writer.writerow([b])
        #writer.writerow([]) # adds extra blank row to log file
        out_file.close()

        #connect to twitter. Update with your twitter login keys/secrets. See README.md
        TOKEN_KEY=" "
        TOKEN=" "
        CON_SEC_KEY=" "
        CON_SEC=" "

        my_auth = twitter.OAuth(TOKEN,TOKEN_KEY,CON_SEC,CON_SEC_KEY)
        twit = twitter.Twitter(auth=my_auth)

        #try to tweet if speedtest couldnt connect. Probably wont work if the internet is down. Update with YOUR INFO
        if "Cannot" in a:
                try:
                        tweet="Hey @FrontierCorp @askfrontier, why is my internet down? I pay for 75Mbps down\\75Mbps up in Dallas area? #frontieroutage #frontier #frontierfios"
                        twit.statuses.update(status=tweet)
                except:
                        pass

        # tweet if down speed is less than setting i.e. <50 or <100
        elif eval(d)<50:
                print ("Trying to tweet")
                try:
                        # I know there must be a better way than to do (str(int(eval())))
                        tweet="Hey @FrontierCorp, why is my internet speed " + str(int(eval(d))) + "down\\" + str(int(eval(u))) + "up when I pay for 75down\\75up in Dallas area? #frontier #frontierfios"
                        twit.statuses.update(status=tweet)
                except Exception as e:
                        print(e)
                                        
        return
        
if __name__ == '__main__':
        test()
        print ('Completed tests')
