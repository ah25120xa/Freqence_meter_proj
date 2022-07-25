from cmath import pi



def retro():
     v=input("press 1 to go to the principal page and 2 to the resonance page :")
     if "1"in v:
          code()
     elif "2"in v:
         resonance()

def resonance():
    print("""CHOOSE : 1-frequence
         2-capacite
         3-inductance""")
    w=input()
    if "1" in w:
      c=extract_data (input("Enter the capacitance:C="))
      l=extract_data (input("Enter the inductance:L="))
      t0=2*pi*(c*l)**(1/2)
      f=1/t0
      print("T0=",t0)
      print("f=",f)
      retro()
    elif "2" in w:
      f=extract_data (input("Enter the frequence f:f="))
      l=extract_data (input("Enter the inductance:L="))
      c=1/(l*4*(f*pi)**2)
      print ("c=",c)
      retro()
    elif "3" in w:
      f=extract_data (input("Enter the frequence f:f="))
      c=extract_data (input("Enter the capacitance:C="))
      l=1/(c*4*(f*pi)**2)
      print ("l=",l)
      retro()

def extract_data(calibre) :
 b=0
 power1=["u","m","n","p","f","k","M","g","t"]
 power ={"u":10**-6,"m":10**-3,"n":10**-9,"p":10**12,"f":10**-15,"k":10**3,"M":10**6,"g":10**9,"t":10**12}
 for i in range(len (power1)):
  if power1[i] in calibre:
     d=""
     for o in range (len(calibre)-1):
      d+=calibre[o]
     calibre=float(d)*power.get(power1[i])
     b+=1
     break
  elif b>=1 :
     calibre=float(calibre)
 return abs(float(calibre))


def code(z):
 def looping(): 
  print (" MAKE SURE THAT THE CALIBRE ARE THE RANGE OF THE FREQUENCE")
  print("for",k,"V")
  print ("Enter a number :")
  print (" 1- Calculate the voltage frequence Vf ")
  print (" 2- Calculate the proper periode T0 and frequence f")
  print (" 3_Resonance ")
  a=input()
  if "7Y" in a: 
      code(3)
  elif "1" in a :
   r=input("Enter the resistence of the R:R=")
   c=input("Enter the capacity of the condensateur:C=")
   f=input("Enter the frequence f:f=")
   tau=extract_data(r)*extract_data(c)
   t0=1/extract_data(f)
   vf=(tau/t0)*k
   print ("tau=",tau,"s")
   print ("T0=",t0,"s")
   print("Vf=",vf,"v")
   y=input("TO REST press 0, to close the window press any tow keys : ")
   if y=="0":
      looping()

  elif "2" in a :
   vf=input("Enter the voltage frequence :Vf=")
   c=input("Enter the capacitance:C=")
   r=input("Enter the resistance:R=")
   tau=extract_data(r)*extract_data(c)
   t0=(k*tau)/extract_data(vf)
   f=1/t0
   print("tau=",tau,"s")
   print("T0=",t0,"s")
   print ("f=",f,"Hz")
   y=input("TO REST press 0, to close the window press any tow keys : ")
   if y=="0":
      looping()
  elif "3" in a :
     resonance()
 if z ==3 :
      k=float (input("Secret settings input E :E="))
      assert k>0
      looping()
 else :
     k=12
     looping()
     

def exept():
  try :
    code(0)
  except:
    print ("ERROR CHEK INPUT")
    exept()
exept()