from goto import with_goto
@with_goto
def main():
 factN= 0 
 factRES= 1 
 count= 0 
 n= 1 
 r= 1 
 goto .loop0
 label .loop0
 print("------")
 print( n )
 print("------")
 if  n <= 100 :
  goto .loop1
 goto .slut
 label .loop1
 print( r )
 if  r <= n :
  goto .eval
 r= 1 
 n= n + 1 
 goto .loop0
 label .eval
 val= 0 
 factN= n 
 J= 0 
 goto .fact
 label .J0
 val= factRES 
 if  val <= 1000000 :
  r= r + 1 
  goto .loop1
 factN= r 
 J= 1 
 goto .fact
 label .J1
 val= val / factRES 
 if  val <= 1000000 :
  r= r + 1 
  goto .loop1
 factN= n - r 
 J= 2 
 goto .fact
 label .J2
 val= val / factRES 
 if  val <= 1000000 :
  r= r + 1 
  goto .loop1
 count= count + 1 
 r= r + 1 
 goto .loop1
 label .fact
 factRES= 1 
 i= 2 
 while  i <= factN :
  factRES= factRES * i 
  i= i + 1 
 goto .JUMP
 label .JUMP
 if  J == 0 :
  goto .J0
 if  J == 1 :
  goto .J1
 if  J == 2 :
  goto .J2
 label .slut
 print( count )
main()
