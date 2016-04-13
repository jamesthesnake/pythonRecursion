

def find_numAs_rec(s,g):
     newStart=1
     value=0
     i=0
     if len(s)!=0:  
       if s[i]==g:
            value=1
       else:
            pass
     else:
          return value
     s=s[newStart:len(s)]
     numAs= value+find_numAs_rec(s,g)
     return numAs

s=raw_input("Ask for  string")
g=raw_input("Ask for character")
print find_numAs_rec(s,g)
