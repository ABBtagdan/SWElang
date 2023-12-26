from goto import with_goto
@with_goto
def main():
 n= 0 
 sum= 0 
 check3=(- 1 )
 check5=(- 1 )
 label .loop0
 n= n + 1 
 while  n < 1000 :
  goto .checkaDelbarhet
 goto .slut
 label .checkaDelbarhet
 check3= n 
 check5= n 
 while  check3 >= 3 :
  check3= check3 - 3 
 if  check3 == 0 :
  sum= sum + n 
  goto .loop0
 while  check5 >= 5 :
  check5= check5 - 5 
 if  check5 == 0 :
  sum= sum + n 
 goto .loop0
 label .slut
 print( sum )
main()
