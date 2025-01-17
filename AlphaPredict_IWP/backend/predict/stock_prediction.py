import numpy as np
import sys
import datetime as dt
import yfinance as yf
from datetime import timedelta
from sklearn.preprocessing import MinMaxScaler
from keras.models import Sequential
import keras
import os
from keras.layers import Dense,Dropout,LSTM
data=[]
prediction_days=60
def get_data(company,offset):
        #company='TSLA'   #globabl company 'FB' 'GOOGL'  Indian:"IDEA.NS" for national 'IDEA.BS' for bombay

        off={'1M':120,'1W':95,'1Y':209}
        end=""
        # model=keras.models.load_model(company)
        if offset=="1W":
                end=dt.datetime.now()+timedelta(weeks=1)
        elif offset=="1M":
                end=dt.datetime.now()
        elif offset=="1Y":
                end=dt.datetime.now()
                end.replace(end.year+1)

        start=end-timedelta(days=off[offset])
        start=start.strftime("%Y-%m-%d")
        end=end.strftime("%Y-%m-%d")

        data=yf.download(company,start,end)
        #prepare data

        scaler=MinMaxScaler(feature_range=(0,1))
        scaled_data=scaler.fit_transform(data['Close'].values.reshape(-1,1))

        

        x_train=[]
        y_train=[]

        for x in range(prediction_days,len(scaled_data)):
            x_train.append(scaled_data[x-prediction_days:x,0])
            y_train.append(scaled_data[x,0])

        x_train,y_train=np.array(x_train),np.array(y_train)

        x_train=np.reshape(x_train,(x_train.shape[0],x_train.shape[1],1))
        
        model=Sequential()
        model.add(LSTM(units=50,return_sequences=True,input_shape=(x_train.shape[1],1)))  #units 50 is default but u can change it 
        model.add(Dropout(0.2))

        model.add(LSTM(units=50,return_sequences=True))
        model.add(Dropout(0.2))

        model.add(LSTM(units=50))
        model.add(Dropout(0.2))

        model.add(Dense(units=1)) #Prediction of the next close

        model.compile(optimizer="adam",loss='mean_squared_error')
        model.fit(x_train,y_train,epochs=10,batch_size=32)
        model.save(company)
        predict(company,offset)

def predict(company,offset):
        if(company in os.listdir()):
                off={'1M':120,'1W':95,'1Y':209}
                model=keras.models.load_model(company)
                if offset=="1W":
                    end=dt.datetime.now()+timedelta(weeks=1)
                elif offset=="1M":
                    end=dt.datetime.now()
                elif offset=="1Y":
                    end=dt.datetime.now()
                    end.replace(end.year+1)
                start=end-timedelta(days=off[offset])
                start=start.strftime("%Y-%m-%d")
                end=end.strftime("%Y-%m-%d")
                data=yf.download(company,start,end)
                scaler=MinMaxScaler(feature_range=(0,1))
                scaled_data=scaler.fit_transform(data['Close'].values.reshape(-1,1))
                x_train=[]
                x_train.append(scaled_data[0:prediction_days,0])
                real_data=np.array(x_train)
                
                real_data=np.reshape(real_data,(real_data.shape[0],real_data.shape[1],1))
                prediction=model.predict(real_data)
                prediction=scaler.inverse_transform(prediction)
            
                return prediction
        else:
            get_data(company,offset)
                
if(sys.argv[2]!="undefined"):
    predicted=predict(sys.argv[1],sys.argv[2])
    print("DONE")
    print(">>>>>>",predicted)
    


sys.stdout.flush()



# End of first code






















# Start of ashesh code


# import numpy as np
# import sys
# import datetime as dt
# import yfinance as yf
# from datetime import timedelta
# from sklearn.preprocessing import MinMaxScaler
# from keras.models import Sequential
# import keras
# import os
# from keras.layers import Dense, Dropout, LSTM

# data = []
# prediction_days = 60

# def get_data(company, offset):
#     off = {'1M': 120, '1W': 7, '1Y': 365} 
#     end = dt.datetime.now()
#     start = end - timedelta(days=off[offset])
#     end_str = end.strftime("%Y-%m-%d")
#     start_str = start.strftime("%Y-%m-%d")

#     data = yf.download(company, start=start_str, end=end_str)
#     scaler = MinMaxScaler(feature_range=(0, 1))
#     scaled_data = scaler.fit_transform(data['Close'].values.reshape(-1, 1))

#     x_train = []
#     y_train = []

#     for x in range(prediction_days, len(scaled_data)):
#         x_train.append(scaled_data[x - prediction_days:x, 0])
#         y_train.append(scaled_data[x, 0])

#     x_train, y_train = np.array(x_train), np.array(y_train)

#     x_train = np.reshape(x_train, (x_train.shape[0], x_train.shape[1], 1))

#     model = Sequential()
#     model.add(LSTM(units=50, return_sequences=True, input_shape=(x_train.shape[1], 1)))
#     model.add(Dropout(0.2))

#     model.add(LSTM(units=50, return_sequences=True))
#     model.add(Dropout(0.2))

#     model.add(LSTM(units=50))
#     model.add(Dropout(0.2))

#     model.add(Dense(units=1))

#     model.compile(optimizer="adam", loss='mean_squared_error')
#     model.fit(x_train, y_train, epochs=10, batch_size=32)
#     model.save(company)

#     return model

# def predict(company, offset, model):
#     off = {'1M': 120, '1W': 7, '1Y': 365} 
#     end = dt.datetime.now()
#     start = end - timedelta(days=off[offset])
#     end_str = end.strftime("%Y-%m-%d")
#     start_str = start.strftime("%Y-%m-%d")

#     data = yf.download(company, start=start_str, end=end_str)
#     scaler = MinMaxScaler(feature_range=(0, 1))
#     scaled_data = scaler.fit_transform(data['Close'].values.reshape(-1, 1))
#     x_train = []
#     x_train.append(scaled_data[-prediction_days:, 0])
#     real_data = np.array(x_train)
#     real_data = np.reshape(real_data, (real_data.shape[0], real_data.shape[1], 1))
#     prediction = model.predict(real_data)
#     prediction = scaler.inverse_transform(prediction)

#     return prediction

# if len(sys.argv) == 3 and sys.argv[2] in ['1W', '1M', '1Y']:
#     company = sys.argv[1]
#     offset = sys.argv[2]

#     if company not in os.listdir():  # Check if model is not already saved
#         model = get_data(company, offset)
#     else:
#         model = keras.models.load_model(company)

#     predicted = predict(company, offset, model)
#     print("DONE")
#     print(">>>>>>", predicted)
# else:
#     print("Usage: python script.py [company] [offset]")
