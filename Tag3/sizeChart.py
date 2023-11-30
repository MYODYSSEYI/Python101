'''
Die Amazon Größentabelle für oberteile.

Hersteller  D   Brust-umfang(cm)
XXS	        32	80	
XS          34  83
S	        36	88	
M	        38	93	
L	        40	98
XL	        42	103	
2XL	        44	109
3XL	        46	115	
'''

BrustUmfang = int(input("Wie groß ist Ihr Brust Umfang in cm?\n"))

def Ausgabe(BrustUmfang, vGr, vDGr):
    print(f"Deine Größe ist, {vGr} bzw. {vDGr}")

if BrustUmfang >= 80:
    Ausgabe(BrustUmfang, "XXS", 32)   
elif BrustUmfang >= 83: 
    Ausgabe(BrustUmfang, "XS", 34)
elif BrustUmfang >= 88: 
    Ausgabe(BrustUmfang, "S", 36)   
elif BrustUmfang >= 93:
    Ausgabe(BrustUmfang, "M", 38)      
elif BrustUmfang >= 98:
    Ausgabe(BrustUmfang, "L", 40)
elif BrustUmfang >= 103: 
    Ausgabe(BrustUmfang, "XL", 42)
elif BrustUmfang >= 109:
    Ausgabe(BrustUmfang, "XXL", 44)
elif BrustUmfang >= 115:
    Ausgabe(BrustUmfang, "XXXL", 46)
else:
    print("That's a NONO!")





