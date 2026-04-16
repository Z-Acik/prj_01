import pandas as pd

def clean_cargo_csv(input_file, output_file):
    try:

        df = pd.read_csv(input_file, header=None, sep=';', engine='python', on_bad_lines='skip')

        df = df.iloc[:, :11]
        df.columns = ['Eingel_Dat', 'Eingel_Zeit', 'Ausgel_Dat', 'Ausgel_Zeit', 'Land_Code',
                      'Stueck', 'Collis', 'Gewicht', 'Kunde', 'Zusatz', 'Sendungstyp']

        df = df[df['Eingel_Dat'].astype(str).str.contains(r'\.', na=False)]
        df['Stueck'] = pd.to_numeric(df['Stueck'], errors='coerce').fillna(0).astype(int)
        df['Gewicht'] = pd.to_numeric(df['Gewicht'], errors='coerce').fillna(0.0)

        df.to_csv(output_file, index=False, sep=';', encoding='utf-8-sig')
        print(f"Datei '{output_file}' wurde erstellt.")

    except Exception as e:
        print(f"Fehler: {e}")

if __name__ == "__main__":
    clean_cargo_csv('cargo.csv', 'cargo_data.csv')
