kuha = float(input("Mikä on kuhasi pituus senttimetreinä?"))
if kuha<37:
    cm = 37 - kuha
    print("Laske kuha takaisin järveen. Alimmasta sallitusta"
          " pyyntimitasta puuttuu " + str(cm)+ " senttimetriä")
if kuha>=37:
    print("Kuhasi ei ole alamittainen.")