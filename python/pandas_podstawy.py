import pandas as pd
df = pd.read_csv('pokemon_data.txt', delimeter='\t')

print(df.columns) #wypisze nazwy kolumn
df(['Name'[0:5]]) #wypisze  z kolumny name pierwsze 5, od indeksu 0 do 4
print(df[['Name','Type','HP']]) #wypisze wszystko z kolumn name,type,hp
print(df.iloc[1]) #wszystkie dane z 2 rzędu...... iloc[1:4] rzędy od 2 do 4 (indeksy od 1 do 3)
print(df.iloc[2,1]) #info z konkretnej pozycji [Rząd, Kolumna]


for index, row in df.iterrows():
    print(index,row) #przechodzi przez wszystkie rzędy i je wypisuje

df.loc[df['Type'] == "Fire"] #szukamy danych z konkretna wartościa, w tym przypadku wszystko
#co jest typu ognistego
df.describe() #mean,std,min,max itp

df.sort_values('Name', ascending=False) #sortujemy alfabetycznie od tyłu, normalnie bez tego po przecinku
df.sort_values(['Name','HP'], ascending=[1,0]) #sortujemy imiona alfabetycznie, ilosc hp descending(od max)

df['Total'] = df['HP'] + df['Attack'] + df['Speed'] #dodajemy kolumne total, ktora jest suma hp,atk,spd
df = df.drop(columns=['Total']) #nastepnie usuwam total
df['Total'] = df.iloc[:, 4:10].sum(axis=1) #znowu total, : -> wszystkie rzędy i kolumny od 4 do 9(indeksy)
#axis=1 poziomo czyli os x, axis=0 pionowo
df = df[['Total','Hp','Defense']] #zmiana kolejnosci kolumn

cols = list(df.columns.values)
df = df[cols[0:4] + [cols[-1]] + cols[4:12]] #rowniez zmiana ale bez wypisywania nazw, najpierw pierwsze
#4, potem ostatnia i wtedy reszta kolumn
df.to_csv('modified.csv') #tworzymy nowy plik modified.csv z danymi na których pracowaliśmy
df.to_csv('modified.csv',index=False) #to samo ale bez indeksów

df.loc[(df['Type'] == 'Grass') & (df['Type 2'] == 'Fire')] #tylko trawiasto-ogniste typy, 
#mozna tez dac warunek (df['HP'] > 70) czyli wszystkie z hp powyzej 70
df.reset_index(drop=True) #resetujemy wartosc indeksow w przypadku filtrowania, drop=true usuwamy calkowicie stare indeksy z danych

df.loc[~df['Name'].str.contains('Mega')] #pozbywamy się dzięki tyldzie wszystkich,które w nazwie zawierają 'Mega'
import re #regular expressions
df.loc[df['Type'].str.contains('fire|grass',flags=re.I,regex=True)] #wszystkie które mają typ ognisty lub
#trawiasty,, re.I ignoruje wielkość liter w razie gdybym typ zapisal przy niekotrych Fire a innych fire
df.loc[df['Name'].str.contains('^pi[a-z]*',flags=re.I,regex=True)] #wszystkie które zaczynaja sie na
#pi i potem mają dowolną ilosc liter od a do z,,, ^ zaczyna,,,,* 0 lub wiecej powtorzen
df.loc[df['Type'] == 'Fire', 'Type'] = 'Flamer' #w kolumnie type zmieni wszystkim typom fire na typ flamer
df.loc[df['Type'] == 'Fire', 'Legendary'] = True #tylko ogniste są teraz legendarne
df.loc[df['Total'] > 500, ['Generation','Legendary']] = ['TEST', 'test2'] #te ktore total maja wiecej niz 500
#wartosc w generation zmienia na test a wart. w legendary na test2

df.groupby(['Type']).mean() #srednia wszystkich danych ze względu na typ
df.groupby(['Type']).mean().sort_values('Defense',ascending=False) #to samo plus sortowanie od max do min defensywy
df.groupby(['Type']).sum() #to samo ale zamiast sredniej, sumy wszystkich postaci (np suma calego hp)
df.groupby(['Type']).count() #zlicza, np zlicza wszystkie robaki,ogniste

df['count'] = 1
df.groupby(['Type']).count()['count'] #zliczy wszystkie ale pominie kategorie typu hp,atak
df.groupby(['Type1','Type2']).count()['count'] #zliczy wszystkie,poda ile robakow(typ1) ma typ2
#ognisty,ziemisty itp itd

for df in pd.read_csv('modified.csv',chunksize=100000):
    print('CHUNK DF')
    print (df) #kawalek 100 tys rzędów
