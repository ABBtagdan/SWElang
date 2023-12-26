from goto import with_goto
@with_goto
def main():
 print("SPELARE 1: VÄLJ NUMMER")
 x= 0 
 x= float(input())
 i= 0 
 while  i < 100 :
  print("")
  i= i + 1 
 guess=(- 10876 )
 tries= 0 
 while  guess != x :
  print("SPELARE 2, GISSA PÅ SPELARE 1:s NUMMER")
  guess= float(input())
  tries= tries + 1 
 print("RÄTT!, DET TOG SÅ HÄR MÅNGA FÖRSÖK: ")
 print( tries )
main()
