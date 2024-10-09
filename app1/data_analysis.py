def find(city='all',typ='all',season='all'):
    import pandas as pd
    import numpy as np

    data=pd.read_csv(r"app1/places.csv")
    data.reset_index(inplace=True)
    data.columns= ['City','Type','Place','Season','Information']
    data.drop_duplicates(subset='Place',inplace=True)
    if city!='all':
        data=data[data['City']==city]
    flag_typ=True
    flag_season=True
    flag_season
    if typ=='all':
        flag_typ=False
    if season=='all':
        flag_season=False
    places=[]
    infos=[]
    if (not flag_typ) and (flag_season):
        temp = pd.concat([data[data['Season']==season],data[data['Season']=='All Year']]).drop_duplicates().iloc[:,[2,4]]
        places=np.array(temp.iloc[:,0]).flatten()
        infos=np.array(temp.iloc[:,1]).flatten()
    elif (flag_typ) and (not flag_season):
        temp = data[np.array(data['Type']==typ) * (np.array(data['Season']=='All Year'))].iloc[:,[2,4]]
        places=np.array(temp.iloc[:,0]).flatten()
        infos=np.array(temp.iloc[:,1]).flatten()
    elif (not flag_typ) and (not flag_season):
        temp = data[data['Season']=='All Year'].iloc[:,[2,4]]
        places=np.array(temp.iloc[:,0]).flatten()
        infos=np.array(temp.iloc[:,1]).flatten()
    else:
        temp = data[(np.array(data['Season']==season) + np.array(data['Season']=='All Year')) * np.array(data['Type']==typ)].iloc[:,[2,4]]
        places=np.array(temp.iloc[:,0]).flatten()
        infos=np.array(temp.iloc[:,1]).flatten()
    return places,infos
