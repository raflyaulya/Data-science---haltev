import tensorflow as tf
from tensorflow.keras import layers
import pandas as pd
import numpy as np
from sklearn.model_selection import train_test_split


df = pd.read_csv('D:\Machine Learning\something fun\googleplaystore.csv')
df = df.dropna()

print('\n =================       FEATURE ENGINEERING       =============== \n')
print('===== Type columns expand =======')

for elem in df['Type'].unique():
    df[str(elem)] = df['Type'] == elem

print('===== Category columns expand =======')

for elem in df['Category'].unique():
    df[str(elem)] = df['Category'] == elem

print('===== Price columns changes =======')
df['Price'] = df['Price'].apply(lambda x: x.replace('$', ''))
df['Price'] = df['Price'].astype('float')

print('===== Reviews columns changes =======')
df['Reviews'] = df['Reviews'].astype('int')

print('===== Last updated columns changes =======')
df['Last Updated'] = pd.to_datetime(df['Last Updated'])

print('===== Installs columns changes =======')
df['Installs'] = df['Installs'].apply(lambda x: x.replace(',', ''))
df['Installs'] = df['Installs'].apply(lambda x: x.replace('+', ''))
df['Installs'] = df['Installs'].apply(lambda x: int(x))

print('===== OBJECT => CATEGORY  =======')
cat = ['App', 'Category', 'Type', 'Content Rating', 'Genres']

for var in cat:
    df[cat] = df[cat].astype('category')

print('===== SIZE columns changes =======')
df['Size'] = df['Size'].apply(lambda x: x.replace('M', ''))
df['Size'] = df['Size'].apply(lambda x: x.replace('k', ''))
df['Size'] = df['Size'].apply(lambda x: x.replace('Varies with device', 'NaN'))
df['Size'] = df['Size'].apply(lambda x: float(x))

df['Size'] = df['Size'].fillna(0)
meansize = df['Size'].mean()
df['Size'] = df['Size'].fillna(meansize)


print('===== Content Rating columns changes =======\n')
for elem in df['Content Rating'].unique():
    df[str(elem)] = df['Content Rating'] == elem


col = df[['Reviews', 'Size','Installs', 'Price', 'Everyone', 'Teen',
          'Everyone 10+', "Mature 17+",'Adults only 18+',
          'Unrated', 'ART_AND_DESIGN', 'AUTO_AND_VEHICLES', 'BEAUTY', 
          'BOOKS_AND_REFERENCE','BUSINESS', 'COMICS', 'COMMUNICATION', 
          'DATING', 'EDUCATION','ENTERTAINMENT', 'EVENTS', 'FINANCE', 
          'FOOD_AND_DRINK','HEALTH_AND_FITNESS', 'HOUSE_AND_HOME', 
          'LIBRARIES_AND_DEMO','LIFESTYLE', 'GAME', 'FAMILY', 'MEDICAL',
          'SOCIAL', 'SHOPPING', 'PHOTOGRAPHY', 'SPORTS', 'TRAVEL_AND_LOCAL', 
          'TOOLS', 'PERSONALIZATION','PRODUCTIVITY', 'PARENTING', 'WEATHER', 
          'VIDEO_PLAYERS', 'NEWS_AND_MAGAZINES', 'MAPS_AND_NAVIGATION', 'Free', 'Paid']]

X = col.values.astype(np.float32)
y= df['Rating'].values.astype(np.float32)


print('\n=========================================================')
print('=============     TENSORFLOW MODEL       ================')

X_train, X_test, y_train, y_test = train_test_split(X, y , test_size=0.3, random_state=101)
X_train, X_test = X_train / 255.0, X_test / 255.0

model = tf.keras.Sequential([
  layers.Dense(64, activation='relu'),
  layers.Dense(64, activation='softmax'),
  layers.Dense(1)
])

model.compile(loss = tf.keras.losses.MeanSquaredError(),
                      optimizer = tf.keras.optimizers.Adam(),
                      metrics='mean_squared_error')
model.fit(X_train, y_train, epochs=10)

test_acc = model.evaluate(X_test, y_test)
train_acc = model.evaluate(X_train, y_train)
print('\nTrain accuracy score:', train_acc)
print('Test accuracy:', test_acc)

# Use the model for prediction
predictions = model.predict(X_test[:5])
print('Predictions:', predictions.flatten())
print('True labels:', y_test[:5])



print('\n\n==================================================')
print('==============     NORMALIZE       ===============')

X_train, X_test, y_train, y_test = train_test_split(X, y , test_size=0.3, random_state=101)

normalize = layers.Normalization()
normalize.adapt(X_train)
norm_model = tf.keras.Sequential([
    normalize,
    layers.Dense(64, activation='relu'),
    layers.Dense(64, activation='softmax'),
    layers.Dense(1)
])

norm_model.compile(loss=tf.keras.losses.MeanSquaredError(),
                   optimizer=tf.keras.optimizers.Adam(),
                   metrics='mean_squared_error')

norm_model.fit(X_train, y_train, epochs=10)

test_acc = model.evaluate(X_test, y_test)
train_acc = model.evaluate(X_train, y_train)
print('Train accuracy score:', train_acc)
print('Test accuracy score:', test_acc)

# Use the model for prediction
predictions = model.predict(X_test[:5])
print('Predictions:', predictions.flatten())
print('True labels:', y_test[:5])