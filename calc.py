print("""
created by: 
 _____          _               _            
|  ___|_ _ _ __| |__   __ _  __| |
| |_ / _` | '__| '_ \ / _` |/ _` |
|  _| (_| | |  | | | | (_| | (_| |
|_|  \__,_|_|  |_| |_|\__,_|\__,_|
 ___     _                   _    
 _ _|___| | ____ _ _ __   __| | __ _ _ __ _____   __
 | |/ __| |/ / _` | '_ \ / _` |/ _` | '__/ _ \ \ / /
 | |\__ \   < (_| | | | | (_| | (_| | | | (_) \ V / 
 ___|___/_|\_\__,_|_| |_|\__,_|\__,_|_|  \___/ \_/                                                                                   

 Welcome
      Nigga !
     """)

x = None
while x is None:
    try:
        x = float(input('Entry first number: '))
    except ValueError:
        print ("HEY! You must write fucking number".format(x))

y = None
while y is None:
    try:
        y = float(input('Entry second number: '))
    except ValueError:
        print ("HEY! You must write fucking number too".format(y))

qwe= [1,2,3,4,5]
sual = input(""" 
1-Collection - Toplama
2-Extraction - Cikma
3-Impact - Carpma
4-Chamber - Bolme
5-Getting force - Kuvvet alma
""")

while sual != qwe:
   print("You choosed wrong and fucked program")
   #break

if sual == "1":
    print("Response: ", x + y)

elif sual == "2":
    print("Response: ", x - y)

elif sual == "3":
    print("Response: ", x * y)

elif sual == "4":
    print("Response: ", x / y)

elif sual == "5":
    print("Response: ", x ** y)
else:
    print("Fuck off back and choose correct !")
