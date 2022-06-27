#ini adalah sebuah program fisika dari python saya membuat dengan python simple
print("welcome difisika geming ♊")



def kinematika():
    print("masukan angka anda🥰")
    V0 = int(input("masukan V0 anda: "))
    a = int(input('masukan percepatan: '))
    t = int(input("masukan waktu anda: "))
    vt = (V0**2) + (a*t)
    print("hasil: ", vt)
def momentum():
    print("masukan angka anda😇")
    F = int(input("masukan gaya anda: "))
    delta = int(input("masukan delta anda: "))
    t = int(input("masukan waktu anda: "))
    I = F * delta*t 
    print("hasilnya", I)
    
    
while True:
    useState = int(input("silakan pilih angka anda\n\n\n\n1. kinematika\n\n2. implus\n\n\na. pilih no mu: "))
    if(useState == 1):
        kinematika()
    elif(useState == 2):
        momentum()
    else:
        break
        
    
