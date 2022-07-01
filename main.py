from macquisition import macquisition as mac
from mwrangling import mwrangling as mwr
from manalysis import manalysis as man

input_year = int(input("Introduzca el año de fabricación:"))

def main():
    df_raw = mac.acquisition("./data/vehicles.csv")
    df_wrangled = mwr.wrangling(df_raw, input_year)
    final_message = man.analysis(df_wrangled, "Make", "Combined MPG", "./data/finalresult.csv")
    print(final_message)

if __name__ == '__main__':
    main()