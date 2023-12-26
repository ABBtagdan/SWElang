from goto import with_goto
@with_goto
def main():
 n= 0 
 div=(- 1 )
 print("ALLA TAL UNDER 1000000000 DELBARA MED?")
 div= float(input())
 print("--------------------")
 while  n < 1000000000 :
  n= n + 1 
  x= 0 
  while  x < n :
   a= div 
   while  x + a < n :
    a= a * 2 
   if  a == div :
    x= x + a 
   if  a != div :
    x= x + a / 2 
  if  x == n :
   print( n )
main()
