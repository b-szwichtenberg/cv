####ZAD 1
#Złączenie wszystkich miesięcy w jeden plik
import pandas as pd
import os

df = pd.read_csv("./Data/Sales_May_2021.csv")
files = [file for file in os.listdir('./Data')]
all_months_data = pd.DataFrame()

for file in files:
    df = pd.read_csv("./Data/"+file)
    all_months_data = pd.concat([all_months_data, df])

all_months_data.to_csv("all_data.csv",index=False)

all_data = pd.read_csv("all_data.csv")
all_data.head()

#####ZAD 2
#Jaki miesiąc był najlepszy pod względem zarobków? Ile wynosiły wtedy zarobki?
#daty są podane w formie mm/dd/yyyy więc zrobimy kolumne z samym miesiacem zeby latwiej sie liczylo
all_data['Month'] = all_data['Order Date'].str[0:2] #bierzemy dwa pierwsze znaki z całej daty i tworzymy
#z tego kolumnę miesiąc
all_data['Month'] = all_data['Month'].astype('int32') #chcemy zmienic typ danych miesiąca z string do int
#ale najpierw musimy wyczyścic dane : / z wartości NaN

nan_df = all_data[all_data.isna().any(axis=1)]
all_data = all_data.dropna(how='all') #i potem wracamy do tej zmiany na int
#niestety kolejny błąd, pozbywamy się 'Or'

temp_df = all_data[all_data["Order Date"].str[0:2] == 'Or'] #zmieniamy te błędy zeby je znalezc
all_data = all_data[all_data["Order Date"].str[0:2] != 'Or'] #bierzemy wszystko oprocz tych bledow
# i wkoncu wracamy do zmiany na int, no i wracamy do naszego podstawowego pytania

#poniewaz na liscie sa produkty ktore byly kupowane w roznych ilosciach w jednej transakcji
#musimy zrobic kolejna kolumne z ogolnym wydatkiem,np ktos kupil 2 kable (cena kabla to 12ziko) wiec
#musimy podliczyc wydatek 2x12=24

#wczesniej jednak zmieniamy pewne dane liczbowe z stringa w int/float
all_data['Quantity Ordered'] = pd.to_numeric(all_data['Quantity Ordered'])
all_data['Price Each'] = pd.to_numeric(all_data['Price Each'])

all_data['Sales']= all_data['Quantity Ordered'] * all_data['Price Each']
all_data.head() #sales to kupiona ilość razy cena za jeden produkt

#w koncu glowne pytanie, w jakim miesiacu najwiecej wydano i jaka to kwota
results = all_data.groupby('Month').sum() #grupujemy miesiące i sumujemy pozostale dane dla nich czyli,np
#ile w kwietniu kupiono rzeczy,wydano lacznie,wydano za 1 produkt, na koncu wysylamy do variables 'result'



#wykresik sobie narysujemy
import matplotlib.pyplot as plt
months = range(1,13)
plt.bar(months,results['Sales'])
#plt.show() najprostsze 
plt.xticks(months)
plt.ylabel('Sales in PLN')
plt.xlabel('Month Number') 
plt.show()
#ladniejsza wersja z oddzielonym miejscem i etykietami


#######ZAD 3
#wracamy do naszych danych, tym razem-> Jakie miasto miało największą ilosc transakcji?
#najpierw musimy stworzyc kolumne 'miasto', posiadamy kolumne z pelnym adresem zakupu
all_data['City'] = all_data['Purchase Address'].apply(lambda x: x.split(',')[1])
#zauwazamy ze miasto zawsze jest w srodku adresu i adres jest rozdzielony przecinkiem
all_data['State'] = all_data['Purchase Address'].apply(lambda x: x.split(',')[2])
#istnieją miasta o takiej samej nazwie ale w innym stanie/wojewodztwie wiec bierzemy indeks 2(stan i kod pocztowy)
results = all_data.groupby('City').sum() #wczesniej wrzucamy state do city



#########ZAD 4
#W jakim czasie wyświetlać reklamy by zmaksymalizować prawdopodobieństwo zakupów?
#mamy jedną kolumnę z datą i godziną zakupu
all_data['Order Date'] = pd.to_datetime(all_data['Order Date']) #zmieniamy typ danych z string na time
all_data['Hour'] = all_data['Order Date'].dt.hour
all_data['Minute'] = all_data['Order Date'].dt.minute #tworzymy kolumne z godzina i minutą

hours = [hour for hour, df in all_data.groupby('Hour')]
plt.plot(hours,all_data.groupby(['Hour']).count())
all_data.groupby(['Hour']).count()
plt.xticks(hours)
plt.grid()
plt.show()


########ZAD 5
##Jakie produkty są sprzedawane najczęściej razem?
#musimy zobaczyc jakie rozne produkty mają to samo id transakcji
df = all_data[all_data['Order ID'].duplicated(keep=False)] #zostawiamy transakcje tylko gdy ide sie powtorza
df['Grouped'] = df.groupby('Order ID')['Product'].transform(lambda x: ','.join(x))
#grupujemy wszystkie produkty ktore maja takie samo order id w kolumnie grouped
#przez to utworzylismy duplikaty, np rząd w ktorym opisany byl kabel zakupiony w order id - 1
#oraz latarka tez w order id -1, to oba rzędy będą posiadały te same wartości w kolumnie grouped,musimy to usunac
df = df[['Order ID','Grouped']].drop_duplicates()
#liczymy jakie pary najczęściej występują
from itertools import combinations, product
from collections import Counter
count = Counter()

for row in df['Grouped']:
    row_list = row.split(',')
    count.update(Counter(combinations(row_list,2)))

count.most_common(10)

product_group = all_data.groupby('Product')
quantity_ordered = product_group.sum()['Quantity Ordered']
