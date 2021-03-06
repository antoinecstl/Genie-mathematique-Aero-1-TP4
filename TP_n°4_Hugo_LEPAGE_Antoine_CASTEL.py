"""
Hugo LEPAGE et Antoine CASTEL
"""
import TP3annexe as tp3
import tp2annexe as tp2
import matplotlib.pyplot as plt

def Secante(f, x0, x1, epsilon, Nitermax):
    
    n=0
    en=(abs(x1-x0))
    l_n=[n]
    l_xn=[x0]
    l_en=[en]
    
    while en>epsilon and n<=Nitermax :
        n=n+1
        x2=(x0*f(x1)-x1*f(x0))/(f(x1)-f(x0))
        x0=x1
        x1=x2
        en=(abs(x1-x0))
        l_n.append(n)
        l_xn.append(x1)
        l_en.append(en)

    return l_n,l_en,l_xn



def Dichotomie (f,a0,b0,epsilon,Nitermax) :
    
    n=0
    a=a0
    b=b0
    en=(abs(b-a))
    l_n=[n]
    l_xn=[a]
    l_en=[en]

    while en>epsilon and n<=Nitermax :
       m=(a+b)/2
       n+=1
       if f(a)*f(m)<=0 :
           b=m
       else :
           a=m
       en=(abs(b-a))
       l_n.append(n)
       l_xn.append(a)
       l_en.append(en)
       
    return l_n,l_en,l_xn


def point_fixe(g,X0,epsilon,Nitermax):
    #Fonction appliquant la méthode du point fixe.
    
    n=0
    x1=X0
    en=abs(g(x1)-x1)
    l_n=[n]
    l_xn=[x1]
    l_en=[en]
    
    while en>epsilon and n<Nitermax:
        x2=g(x1)
        n+=1
        en=abs(x2-x1)
        x1=x2
        l_n.append(n)
        l_xn.append(x1)
        l_en.append(en)
        
    return l_n,l_en,l_xn

    

def Newton (f,fder,X0,epsilon,Nitermax):
    #Fonction appliquant la méthode de Newton.

    n=0
    x1=X0
    en=abs(-(f(x1)/fder(x1)))
    l_n=[n]
    l_xn=[x1]
    l_en=[en]    

    while en>epsilon and n<Nitermax:
        x2=x1-(f(x1)/fder(x1))
        n+=1 
        x1=x2
        en=abs(-(f(x1)/fder(x1)))
        l_n.append(n)
        l_xn.append(x1)
        l_en.append(en)
    return l_n,l_xn,l_en
    
data = Dichotomie(tp3.f1,0,2,1e-10,5e4)
data1 = Secante(tp3.f1,0,2,1e-10,5e4)
data2 = Newton(tp3.f1,tp3.fd1,1,1e-10,5e4)
data3 = point_fixe(tp2.g11,0,1e-10,5e4)
plt.semilogy(data[0],data[1])
plt.semilogy(data1[0],data1[1])
plt.semilogy(data2[0],data2[2])
plt.semilogy(data3[0],data3[1])
plt.title('f(x)=x**4+3*x-9')
plt.xlabel('Nombre itération')
plt.ylabel('Erreur')
plt.legend(['Dichotomie','Secante','Newton',"Point fixe"])
plt.show()

data01 = Dichotomie(tp3.f6,0,2,1e-10,5e4)
data11 = Secante(tp3.f6,0,2,1e-10,5e4)
data21 = Newton(tp3.f6,tp3.fd6,1,1e-10,5e4)
data31 = point_fixe(tp2.g3,1.5,1e-10,5e4)
plt.semilogy(data01[0],data01[1])
plt.semilogy(data11[0],data11[1])
plt.semilogy(data21[0],data21[2])
plt.semilogy(data31[0],data31[1])
plt.title('f(x)=x*exp(x)-7')
plt.xlabel('Nombre itération')
plt.ylabel('Erreur')
plt.legend(['Dichotomie','Secante','Newton',"Point fixe"])
plt.show()

data011 = Dichotomie(tp3.f10,0,2,1e-10,5e4)
data111 = Secante(tp3.f10,0,2,1e-10,5e4)
data211 = Newton(tp3.f10,tp3.fd10,1,1e-10,5e4)
data311 = point_fixe(tp2.g10,2,1e-10,5e4)
plt.semilogy(data011[0],data011[1])
plt.semilogy(data111[0],data111[1])
plt.semilogy(data211[0],data211[2])
plt.semilogy(data311[0],data311[1])
plt.title('f(x)=log(x**2+4)*exp(x)-10')
plt.xlabel('itération')
plt.ylabel('Erreur')
plt.legend(['Dichotomie','Secante','Newton',"Point fixe"])
plt.show()


#print(Dichotomie(y0,0,2,1e-10,5e4),'d1') 

print(Newton(tp3.f3,tp3.fd1,1,1e-10,5e4))  
   
#print(Dichotomie(y2,0,2,1e-10,5e4),'d3')    
   
#print(Secante(y0,0,2,1e-10,5e4),'s1')

#print(Secante(y1,0,2,1e-10,5e4),'s2')

#print(Secante(y2,0,2,1e-10,5e4),'s3')