from extract import extract_data
from transform import transform_data
from load import load_data

def main():

    print("Extraindo dados...")
    df = extract_data()

    print(df.head())

    print("Transformando dados...")
    df = transform_data(df)

    print(df.head())

    print("Carregando dados...")
    load_data(df)

    print("Pipeline completo executado!")

if __name__ == "__main__":
    main()