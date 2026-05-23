def transform_data(df):

    df = df.dropna()

    df = df.drop_duplicates()

    print("Transform concluido!")

    return df
