def total(a=5, *nummern, **telefonbuch):
    print('a', a)
    
    #iteriere durch alle Items in einem tuple
    for eine_nummer in nummern:
        print('einzelnes Item', eine_nummer)
        
    #iteriere durch alle Items im dictionary    
    for name, nummer in telefonbuch.items():
        print(name,nummer)

total(10,1,2,3,Jack=1123,John=2231,Inge=1560)
