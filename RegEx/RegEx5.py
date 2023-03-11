import sys; args = sys.argv[1:]
idx = int(args[0])-70

myRegexLst = [r"/^[a-z]*(?=\w*a)[a-z]*(?=\w*e)[a-z]*(?=\w*i)[a-z]*(?=\w*o)[a-z]*(?=\w*u)[a-z]*$/m", #70
              r"/^([b-d,f-h,j-n,p-t,v-z]*[aeiou]){5}[b-d,f-h,j-n,p-t,v-z]*$/m", #11
              r"/^[b-d,f-h,j-n,p-t,v-z](w)[b-d,f-h,j-n,p-t,v-z]$|^[a-z]*[b-d,f-h,j-n,p-t,v-z](w)[b-d,f-h,j-n,p-t,v-z]{2}[a-z]*$/m", #72
              r"/(?=[a-z]+$)^(?=([a-z])([a-z])([a-z])[a-z]*$)^[a-z]*\3\2\1$|^(a)$|^([a-z])\5$/m", #73
              r"/^[ac-s,u-z]*(tb|bt)+[ac-s,u-z]*$/m", #74
              r"/^[a-z]*([a-z])\1[a-z]*$/m", #75
              r"/[a-z]*([a-z])([a-z]*\1){5}[a-z]*$/m", #76
              r"/[a-z]*(([a-z])\2){3}[a-z]*$/m", #77
              r"/(?=[a-z]+$)(?=^\w*(\w*[^aeiou\W]){13}\w*$)^\w*$/m", #78
              r"/^(?=[a-z]+$)(?:([a-z])(?!([a-z]*\1[a-z]*\1)))+$/m"] #79

if idx < len(myRegexLst):
  print(myRegexLst[idx])

#Pooja Somayajula,4,2024
