min01=float(input("Introduce la cantidad de minutos: "))
min02=min01%60
h=(min01-min02)/60

if h==1:
    textHora="hora"
else:
    textHora="horas"

if min01==1:
    textMinuto="minuto"
else:
    textMinuto="minutos"

if min02==1:
    textMinuto2="minuto"
else:
    textMinuto2="minutos"

print("{} {} son {} {} y {} {} ".format(min01,textMinuto,h,textHora,min02,textMinuto2))
