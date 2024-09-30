import os
os.system('cls')

bankomat = {
    "Xizmatlar":["1-Kartaga mablag` qo`shish", "2-Kartadan mablag` yechish", "3-Telefon raqamga mablag` o`tqazish"],
    "G`azna"   :10000000, 
    "Plastik_kartalar":[["9860260112326715","0000",820000],
                        ["9860260112326716","0000",100000],
                        ["9860260112326717","0000",2200000]],
    "Telefon_raqmlar": [770229876,
                        941891525,
                        973999876,
                        979199239,]                
}

def plastik_check():
    p_raqam = input("Plastik raqamni kiriting: ")
    for i in bankomat["Plastik_kartalar"]:        
        if p_raqam==i[0]:
             p_kod = input("Plastik kodini kiriting: ")
             if p_kod != i[1]:
                    print("Kod notog`ri!!!")
                    return False
             else:
                return i                          
        # else:
        #     print("Plastik raqam notog`ri!!!")
        #     return False
    print("Plastik raqam notog`ri!!!")                
                
                        
    return False 

 
                 

def mablag_qoshish():
    plastik = plastik_check()
    if plastik:
        print(f"Plastikda {plastik[2]} so`m bor")
        pul = int(input("Pulni kiriting: "))
        bankomat["G`azna"]+=pul
        plastik[2]+= pul
        print(f"Plastik balansi: {plastik[2]}") 

    return 

def mablag_yechish():
    plastik = plastik_check()
    if plastik:
        print(f"Plastikda {plastik[2]} so`m bor")  
        pul_y = int(input("Yechiladigan summani kiriting: "))
        if pul_y <= plastik[2] :
            if  pul_y <= bankomat["G`azna"]:
                bankomat["G`azna"]-=pul_y
                plastik[2] -= pul_y        
                print(f"200 000 so`mlik = {pul_y//200000} ta")
                print(f"100 000 so`mlik = {pul_y%200000//100000} ta")
                print(f"50 000 so`mlik  = {pul_y%200000%100000//50000} ta")
                print(f"20 000 so`mlik  = {pul_y%200000%100000%50000//20000} ta")
                print(f"10 000 so`mlik  = {pul_y%200000%100000%50000&20000//10000} ta")
                print(f"5 000 so`mlik   = {pul_y%200000%100000%50000&20000%10000//5000} ta")
                print(f"Plastigingizda {plastik[2]} qoldi")
            else:
                print("Bankomatdagi  pul sizga berish uchun yetarli emas:(")
        else:
            print("Plastikdagi  pul sizga berish uchun yetarli emas:(")         
                
            
    return

def t_raqam_tolov():
    t_raqam = int(input("Telefon raqamingizni kiriting:"))
    for n in bankomat["Telefon_raqmlar"]:                
        if t_raqam == n:          
            k_summa = int(input("Telefon raqamga necha pul kiritasiz: "))
            plastik = plastik_check()            
            if not plastik:return False            
            if plastik[2]< k_summa:
                print("Mablag` yetarli emas")

                
                return False
            plastik[2] = plastik[2]-k_summa
            print(f"Telefoningizga {k_summa} o`tkazildi.\n Kartangizda balans {plastik[2]} ")
            return


    print(f"Bu {t_raqam} notog`ri!!!")
    return False



    

           

# print(*bankomat["Xizmatlar"])
ish_xolati = True # Bu Bankomatning mijozga xizmat ko`rsatish xolati`

while ish_xolati:
    print("Ko'rsatiladigan xizmat turlari: ")
    for i in bankomat["Xizmatlar"]:
        print(i)
    xizmat_turi =input("Xizmat turi raqamini kiriting: ") 
    if xizmat_turi==str(1):
        mablag_qoshish()
        
    elif xizmat_turi==str(2):
        mablag_yechish()

    #print(bankomat["G`azna"],bankomat["Plastik_kartalar"][0])
    elif xizmat_turi==str(3):
        t_raqam_tolov()
    
    break

 

import os


# s ="testhello"
# a1=[]
# a2=[]
# for i in s:
#     print(i)
#     a1.append(s.count(i))
#     a2.append(i)
# print(dict(zip(a2,a1)))




#1
# my_list=[34,56,67,555]
# s = []
# for i in my_list:
#     if i%2!=0 and i%3!=0:
#         s.append(i)
# print(s)

#2
# a = str(input())
# if a[0]==a[-1]:
#     print(f"{a} palidrom so`z")
    
# else:
#     print(f"{a} palidrom so`z emas")
    
#3
# a = int(input("Son: "))
# for i in a:
#     if len(i)==3:
#         print("3 xonali son bu")