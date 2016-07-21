#####################
#date/ticker quandl api call
#api key: aHvRyhPooPx1JLFAQ36J
#######################

import quandl
import pandas
import datetime

quandl.ApiConfig.api_key = 'aHvRyhPooPx1JLFAQ36J'

while True:

    print("Input XYZ")
    getTicker = input()
    
    print("Input DD/MM/YYYY")
    getDate = input()
    

    getTicker = getTicker.upper()
    tableInput = 'YAHOO/AX_'+getTicker
    
    getDate = getDate.upper()
    x = getDate.split('/')

    getDate = x[2]+'-'+x[1]+'-'+x[0]
    d = datetime.date(int(x[2]),int(x[1]),int(x[0]))
    try:
        data = quandl.get(tableInput, start_date=getDate, end_date=getDate)
        df1 = float(data.Close)

        print('\n'+getTicker+ ' on '+ d.strftime("%A %d/%m/%Y")+':')
        print('\n$'+str(df1)+'\n')
    except:
        print('something went wrong grabbing data...\n you picked '+d.strftime("%A"))
        
