from playsound import playsound
def loopSound():
    while True:
        playsound('alert.wav', block=True)

import requests,sys,time,os
# get todays date
from datetime import date, datetime
attempt=0
while True:
    try:
        district=int(sys.argv[1])
        today=datetime.today().strftime('%d-%m-%Y')
        # thrissur
        url= 'https://cdn-api.co-vin.in/api/v2/appointment/sessions/public/calendarByDistrict?district_id={0}&date={1}'
        url=url.format(district,today)
        headers ={
            'accept': 'application/json' ,
            'Accept-Language': 'hi_IN',
            'user-agent':'Mozilla/5.0 (Windows NT 6.3; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/90.0.4430.93 Safari/537.36'
            }
        print(today)
        print(district)
        print(url)
        import requests
        r= requests.get(url,headers=headers)
        print(r.status_code)
        notify=False
        if r.status_code==200:
            resp = r.json()
            # print(resp)
            for i in resp['centers']:
                #print(i['name'])
                #print(i['block_name'])
                #print(i['fee_type'])
                for s in i['sessions']:
                    if (int(s['available_capacity'])>0 and int(s['min_age_limit'])==18):
                        notify=True
                        with open(today+'_slot.txt','a') as f:
                            f.write('Slots available for : '+s['date'])
                            f.write('\nCentre name : '+i['name'])
                            f.write('\nBlock name :'+i['block_name'])
                            f.write('\nFee type :'+i['fee_type'])
                            f.write('\nAvailable capacity Dose 1: '+str(s['available_capacity_dose1']))
                            f.write('\nAvailable capacity Dose 2: '+str(s['available_capacity_dose2']))
                            f.write('\nAge limit '+str(s['min_age_limit']))
                            f.write('\nVaccine : '+s['vaccine'])
                            f.write('\nSlots : '+str(s['slots']))
                            f.write('\n+-----------------------------------------------+\n')

                            print('Slots available for : '+s['date'])
                            print('\nCentre name : '+i['name'])
                            print('\nBlock name :'+i['block_name'])
                            print('\nFee type :'+i['fee_type'])
                            print('\nAvailable capacity Dose 1: '+str(s['available_capacity_dose1']))
                            print('\nAvailable capacity Dose 2: '+str(s['available_capacity_dose2']))
                            print('\nAge limit '+str(s['min_age_limit']))
                            print('\nVaccine : '+s['vaccine'])
                            print('\nSlots : '+str(s['slots']))
                            print('\n+-----------------------------------------------+\n')

                #print("-----------------------------------")
            if notify:
                import threading
                from playsound import playsound
                # providing a name for the thread improves usefulness of error messages.
                loopThread = threading.Thread(target=loopSound, name='alert')
                loopThread.daemon = True # shut down music thread when the rest of the program exits
                loopThread.start()
                while True:
                    if input("Press q to exit...")=='q':
                        sys.exit()
        attempt+=1
        print("+++++++++++++++++++++++++Execution end ["+str(attempt)+"]++++++++++++++++++++++++++++++++")
    except Exception as e:
        print("Exception occured - " + str(e))
    time.sleep(60)

