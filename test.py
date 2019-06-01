import fitbit
import gather_keys_oauth2 as Oauth2
import datetime
import json
import time as t
import matplotlib.pyplot as plt 
import requests
class data:
    def __init__(self):
        self.USER_ID = '22DG4C'
        self.CLIENT_SECRET = '940862ba343ec9ed386b999e689560d4'
        self.yesterday = str((datetime.datetime.now() - datetime.timedelta(days=1)).strftime("%Y-%m-%d"))
        self.today = str(datetime.datetime.now().strftime("%Y%m%d"))
        self.autenticate()
    def autenticate(self):
        self.server = Oauth2.OAuth2Server(self.USER_ID, self.CLIENT_SECRET)      
        self.server.browser_authorize()
        ACCESS_TOKEN = str(self.server.fitbit.client.session.token['access_token'])
        REFRESH_TOKEN = str(self.server.fitbit.client.session.token['refresh_token'])
        self.auth2_client = fitbit.Fitbit(self.USER_ID, self.CLIENT_SECRET, oauth2=True, access_token= ACCESS_TOKEN, refresh_token= REFRESH_TOKEN)
    def step(self,timer):
        if timer == "1d":
            step_hr = []
            time_all = []
            temp_step = 0
            index = 0
            total = 0
            
            fit_statsHR = self.auth2_client.make_request("https://api.fitbit.com/1/user/-/activities/steps/date/today/1d.json")
            print(fit_statsHR)
            for i in fit_statsHR["activities-steps-intraday"]["dataset"]:
                time = i.get("time")
                if time[3:5] != "00":
                    temp = int(i.get("value"))
                    temp_step += temp
                    total += temp
                if time[3:5] == "59":
                    temp = int(i.get("value"))
                    step_hr.append(temp_step + temp)
                    time_all.append(str(index)+ ":00")
                    index += 1
                    total += temp
                    temp_step = 0
            plt.plot(time_all,step_hr)
            plt.xlabel("Time in 1 day")
            plt.ylabel("Number of Steps")
            plt.title("Your Steps")
            plt.show()
        else:
            date = []
            count = 0
            steps = []
            temp_step = 0
            fit_statsHR = self.auth2_client.time_series("activities/steps",period = timer)
            for i in fit_statsHR["activities-steps"]:
                count += 1
                temp = i.get("dateTime")
                temp2 = temp[8:10] + "/" + temp[5:7] + "/" + temp[2:4]
                temp_step += int(i.get("value"))
                if count % 7 == 1:    
                    date.append(temp2)
                    steps.append(temp_step)
                    temp_step = 0
            print(count)
            plt.plot(date,steps)
            plt.xlabel("date")
            plt.ylabel("Number of Steps")
            plt.title("Your Steps")
            plt.show()
if __name__ == "__main__":
    test = data()
    print(test.step("3m"))
    
"""

CLIENT_ID = '22DG4C'
CLIENT_SECRET = '940862ba343ec9ed386b999e689560d4'

server = Oauth2.OAuth2Server(CLIENT_ID, CLIENT_SECRET)
server.browser_authorize()
ACCESS_TOKEN = str(server.fitbit.client.session.token['access_token'])
REFRESH_TOKEN = str(server.fitbit.client.session.token['refresh_token'])
auth2_client = fitbit.Fitbit(CLIENT_ID, CLIENT_SECRET, oauth2=True, access_token=ACCESS_TOKEN, refresh_token=REFRESH_TOKEN)


def steps():
    fit_statsHR = auth2_client.make_request("https://api.fitbit.com/1/user/-/activities/steps/date/today/1d.json")
    return fit_statsHR

if __name__ == "__main__":
    test = steps()
    print(test)
"""
