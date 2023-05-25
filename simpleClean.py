import pandas as pd

import re

data = pd.read_csv('data.csv')

dataFrame = pd.DataFrame(data)

##drop null values
dataFrame.dropna(inplace = True)

##drop duplicates
dataFrame.drop_duplicates(inplace = True)

##convert column names to lower
dataFrame.columns = map(str.lower, dataFrame.columns)

##convert column values to lower if string
dataFrame = dataFrame.applymap(lambda x: x.lower() if type(x) == str else x)

##remove special characters
dataFrame = dataFrame.applymap(lambda x: re.sub('[^A-Za-z0-9]+', '', x) if type(x) == str else x)


dataFrame.to_csv('cleanData.CSV')
