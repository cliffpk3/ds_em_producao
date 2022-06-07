import pickle
import inflection
import pandas as pd
import numpy as np
import math
import datetime

class Rossmann(object):
    def __init__(self):
        self.home_patch='C:/Users/carli/Documents/#Python/comunidade_ds/repos/ds_em_producao/'
        self.competition_distance_scaler = pickle.load(open(self.home_patch+'parameter/competition_distance_scaler.pkl', 'rb'))
        self.competition_time_month_scaler = pickle.load(open(self.home_patch+'parameter/competition_time_month_scaler.pkl', 'rb'))
        self.promo_time_week_scaler = pickle.load(open(self.home_patch+'parameter/promo_time_week_scaler.pkl', 'rb'))
        self.year_scaler = pickle.load(open(self.home_patch+'parameter/year_scaler.pkl', 'rb'))
        self.store_type_scaler = pickle.load(open(self.home_patch+'parameter/store_type_scaler.pkl', 'rb'))
    
    def data_cleaning(self, df2):
        snakecase = lambda x: inflection.underscore(x)
        df2.columns = list(map(snakecase, df2.columns))
        #df2.drop(['sales','customers'], axis=1) #???<<<
        df2['date'] = pd.to_datetime(df2['date'])
        df2['competition_distance'] = df2['competition_distance'].apply(lambda x: 200000.0 if math.isnan(x) else x)
        df2['competition_open_since_month'] = df2.apply(lambda x: x['date'].month if math.isnan(x['competition_open_since_month']) else x['competition_open_since_month'], axis=1)
        df2['competition_open_since_year'] = df2.apply(lambda x: x['date'].year if math.isnan(x['competition_open_since_year']) else x['competition_open_since_year'], axis=1)
        df2['promo2_since_week'] = df2.apply(lambda x: x['date'].week if math.isnan(x['promo2_since_week']) else x['promo2_since_week'], axis=1)
        df2['promo2_since_year'] = df2.apply(lambda x: x['date'].year if math.isnan(x['promo2_since_year']) else x['promo2_since_year'], axis=1)
        calendar = {1: 'Jan', 2: 'Feb', 3: 'Mar', 4: 'Apr', 5: 'May', 6: 'Jun', 7: 'Jul', 8: 'Aug', 9: 'Sep', 10: 'Oct', 11: 'Nov', 12: 'Dec'}
        df2['promo_interval'].fillna(0, inplace=True)
        df2['calendar'] = df2['date'].dt.month.map(calendar)
        df2['is_promo'] = df2[['promo_interval','calendar']].apply(lambda x: 0 if x['promo_interval'] == 0 else 1 if x['calendar'] in x['promo_interval'].split(',') else 0, axis=1)        
        df2['competition_open_since_month'] = df2['competition_open_since_month'].astype(int)
        df2['competition_open_since_year'] = df2['competition_open_since_year'].astype(int)
        df2['promo2_since_week'] = df2['promo2_since_week'].astype(int)
        df2['promo2_since_year'] = df2['promo2_since_year'].astype(int)        
        return df2
    
    def feature_engineering(self,df3):
        df3['year'] = df3['date'].dt.year
        df3['month'] = df3['date'].dt.month
        df3['day'] = df3['date'].dt.day
        df3['week_of_year'] = df3['date'].dt.isocalendar().week
        df3['year_week'] = df3['date'].dt.strftime('%Y-%W')
        df3['competition_since'] = df3.apply(lambda x: datetime.datetime(year=x['competition_open_since_year'], month=x['competition_open_since_month'], day=1), axis=1)
        df3['competition_time_month'] = ((df3['date'] - df3['competition_since'])/30).apply(lambda x: x.days).astype(int)
        df3['promo_since'] = df3['promo2_since_year'].astype(str) + '-' + df3['promo2_since_week'].astype(str)
        df3['promo_since'] = df3['promo_since'].apply(lambda x: datetime.datetime.strptime(x+'-1','%Y-%W-%w') - datetime.timedelta(days=7))
        df3['promo_time_week'] = ((df3['date'] - df3['promo_since'])/7).apply(lambda x: x.days).astype(int)
        df3['assortment'] = df3['assortment'].apply(lambda x: 'basic' if x == 'a' else 'extra' if x == 'b' else 'extended')
        df3['state_holiday'] = df3['state_holiday'].apply(lambda x: 'public holiday' if x == 'a' else 'easter_holiday' if x == 'b' else 'christmas' if x == 'c' else 'regular_day')
        df3 = df3[df3['open'] != 0]
        df3.drop(['open','promo_interval','calendar'], axis=1, inplace=True)
        return df3
    
    def data_preparation(self,df6):
        df6['competition_distance'] = self.competition_distance_scaler.transform(df6[['competition_distance']].values)
        df6['competition_time_month'] = self.competition_time_month_scaler.transform(df6[['competition_time_month']].values)
        df6['promo_time_week'] = self.promo_time_week_scaler.transform(df6[['promo_time_week']].values)
        df6['year'] = self.year_scaler.transform(df6[['year']].values)
        df6 = pd.get_dummies(df6,prefix=['state_holiday'], columns=['state_holiday'])
        df6['store_type'] = self.store_type_scaler.transform(df6['store_type'])
        assortment_dict = {'basic':1, 'extra':2, 'extended':3}
        df6['assortment'] = df6['assortment'].map(assortment_dict)
        df6['day_of_week_sin'] = df6['day_of_week'].apply(lambda x: np.sin(x*(2.*np.pi/7)))
        df6['day_of_week_cos'] = df6['day_of_week'].apply(lambda x: np.cos(x*(2.*np.pi/7)))
        df6['month_sin'] = df6['month'].apply(lambda x: np.sin(x*(2.*np.pi/12)))
        df6['month_cos'] = df6['month'].apply(lambda x: np.cos(x*(2.*np.pi/12)))
        df6['day_sin'] = df6['day'].apply(lambda x: np.sin(x*(2.*np.pi/30)))
        df6['day_cos'] = df6['day'].apply(lambda x: np.cos(x*(2.*np.pi/30)))
        df6['week_of_year_sin'] = df6['week_of_year'].apply(lambda x: np.sin(x*(2.*np.pi/52)))
        df6['week_of_year_cos'] = df6['week_of_year'].apply(lambda x: np.cos(x*(2.*np.pi/52)))
        
        cols_selected = ['store','promo','store_type','assortment','competition_distance',
                                'competition_open_since_month','competition_open_since_year',
                                'promo2','promo2_since_week','promo2_since_year',
                                'competition_time_month','promo_time_week','day_of_week_sin',
                                'day_of_week_cos','month_sin','month_cos','day_sin','day_cos',
                                'week_of_year_cos','week_of_year_sin']
        
        return df6[cols_selected]
    
    def get_prediction(self, model, original_data, test_data):
        #Prediction
        pred = model.predict(test_data)
        
        #join pred into original data
        original_data['prediction'] = np.expm1(pred)
        return original_data.to_json(orient='records', date_format='iso')