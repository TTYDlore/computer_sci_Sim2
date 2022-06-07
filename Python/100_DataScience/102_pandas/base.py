movies_df['Year'].plot(kind='hist', title='Realse date');
movies_df.plot(kind='scatter', x='Year', y='Metascore', title='Year vs Metascore');
Meta = movies_df['Metascore']
metascoremean = Meta.mean()
print(" ")
print("The avarage metascore is " + str(metascoremean))