from goto import with_goto
@with_goto
def main():
 n1= 0 
 n2= 1 
 n3= 1 
 sum= 0 
 while  n2 < 4000000 :
  n3= n1 + n2 
  n1= n2 
  n2= n3 
  x= 0 
  print( n2 )
  while  x < n2 :
   a= 2 
   while  x + a < n2 :
    a= a * 2 
   if  a == 2 :
    x= x + a 
   if  a != 2 :
    x= x + a / 2 
   print( x )
  print("-------")
  if  x == n2 :
   sum= sum + n2 
 print( sum )
main()
