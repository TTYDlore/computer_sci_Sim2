print("1. What is the overall trend of the total poputlation of California") #x,y chart
print("2. How close were the pesadents in height ") #histogram
print("3. how much space do all cites in California take up ") #box polt
population_df = pd.read_csv("state-population.csv", index_col="population")
height_df = pd.read_csv("president_heights.csv")
sapce_df = pd.read_csv("california_cities.csv")
population_df