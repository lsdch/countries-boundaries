#%%
import geopandas
import pandas as pd

features = geopandas.read_file("data/EEZ_land_union_v4_202410.json")

# Fix missing Antarctica metadata from the dataset,
# although it is defined in the ISO 3166 standard
features.loc[features['UNION'] == 'Antarctica', 'ISO_SOV1'] = 'ATA'
features.loc[features['UNION'] == 'Antarctica', 'SOVEREIGN1'] = 'Antarctica'

# Use Territory code if available, otherwise use Sovereign code
features['CODE'] = features['ISO_TER1'].replace('', None).fillna(features['ISO_SOV1'])

# Filter out territories that have ambiguous status: Joint regime or Overlapping claim)
filtered = features[features['POL_TYPE'].isin(['Joint regime (EEZ)', 'Overlapping claim']).eq(False)]

dissolved = filtered[['CODE', 'geometry']].dissolve(by=['CODE'])

print("Merged country boundaries:")
print(dissolved)


country_codes = pd.read_csv("data/country_codes.csv")[['name', 'alpha-2', 'alpha-3', 'country-code', 'region', 'sub-region']]

print("Processed dataset with ISO metadata:")
merged = country_codes.merge(dissolved, left_on='alpha-3', right_on='CODE', how='left')
print(merged)

result = geopandas.GeoDataFrame(merged)
result.plot()
result.to_file("output/countries.json", driver="GeoJSON")



# %%
