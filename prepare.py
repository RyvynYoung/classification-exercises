# prep the iris data
def prep_iris(df):
    # Drop the species_id and measurement_id columns
    df = df.drop(columns=['species_id', 'measurement_id'])
    
    # Rename the species_name column to just species
    df = df.rename(columns={'species_name': 'species'})
    
    # encode the species column
    df_dummies = pd.get_dummies(df[['species']], drop_first=True)
    df = pd.concat([df, df_dummies], axis=1)
    
    return df

# prep the titantic data
