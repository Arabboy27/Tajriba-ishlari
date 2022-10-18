N=int(input("sonni kiriting:"))
soat=N//3600
qoldiq=N%3600
minut=qoldiq//60
sekunt=qoldiq%60
print(soat,"soat")
print(minut,"minut")
print(sekunt,"sekunt")