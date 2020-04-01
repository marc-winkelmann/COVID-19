import pandas as pd

germanyCurrent = pd.read_csv('https://opendata.arcgis.com/datasets/917fc37a709542548cc3be077a786c17_0.csv')

germanyCurrent.to_csv('C:/Users/Marc/PycharmProjects/COVID-19/Data/covid-19_germany_current.csv', sep=';', encoding='utf-8', index=False)

germanyTimeline = pd.read_csv('https://opendata.arcgis.com/datasets/dd4580c810204019a7b8eb3e0b329dd6_0.csv')

germanyTimeline.to_csv('C:/Users/Marc/PycharmProjects/COVID-19/Data/covid-19_germany_timeline.csv', sep=';', encoding='utf-8', index=False)