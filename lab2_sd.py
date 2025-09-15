a = 9
b = 8
c = 12
d = 33
e = 5
u=(a+b+c+d+e)/5
print(u)
sq1=(a-u)*(a-u)
sq2=(b-u)*(b-u)
sq3=(c-u)*(c-u)
sq4=(d-u)*(d-u)
sq5=(e-u)*(e-u)
sql_total=sq1+sq2+sq3+sq4+sq5
variance=sql_total/5
sd=variance**(1/2)
print(sd)       



