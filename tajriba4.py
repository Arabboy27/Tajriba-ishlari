K=int(input("366 dan katta bolmagan sonlarni kiriting: "))
if K%7==0 :
 print(K,"Haftaning yakshanba kuni")
elif K%7==1 :
 print(K,"Haftaning dushanba kuni")
elif K%7==2:
 print(K,"Haftaning seshanba kuni")
elif K%7==3:
 print(K,"Haftaning chorshanba kuni")
elif K%7==4 :
 print(K,"Haftaning payshanba kuni")
elif K%7==5 :
 print(K,"Haftaning juma kuni")
else :
 print(K,"Haftaning shanba kuni")