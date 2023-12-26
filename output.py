from goto import with_goto
@with_goto
def main():
 x= 0 
 print("n: ")
 n= 0 
 n= float(input())
 label .iteration
 while  n > 1 :
  x= n 
  goto .xDelbarMed2
 goto .slut
 label .checkaDelbarhet
 if  x != 1 :
  x= 0 
  n= 3 * n + 1 
 if  x == 1 :
  n= n / 2 
 print( n )
 goto .iteration
 label .xDelbarMed2
 CONTROLLNUMBER= 1 
 x= x / 2 
 while  x >= CONTROLLNUMBER :
  CONTROLLNUMBER= CONTROLLNUMBER * 2 
 while  CONTROLLNUMBER > x :
  CONTROLLNUMBER= CONTROLLNUMBER - 1 
 print("#----#")
 x= x / CONTROLLNUMBER 
 goto .checkaDelbarhet
 label .slut
main()
