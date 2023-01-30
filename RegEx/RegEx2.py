import sys; args = sys.argv[1:]
idx = int(args[0])-40

myRegexLst = [r"/^[xo.]{64}$/i", #40
              r"/^[xo]*\.[xo]*$/i", #41
              r"/^\.|\.$|\.o*x+$|^x+o*\./i", #42
              r"/^.(..)*$/s", #43
              r"/^(1[01]|0)([10]{2})*$/", #44
              r"/\w*(i[aeou]|u[aeio]|a[eiou]|o[aeiu]|e[aiou])\w*/i", #45
              r"/^(1?0+)*1*$/", #46
              r"/^[bc]*(a[bc]|[bc])*$/", #47
              r"/^[bc]*(a[bc]*a[bc]*)+$|^[bc]+$/", #48
              r"/^(1[02]*1|2)(2|0|1[02]*1)*$/"] #49

if idx < len(myRegexLst):
  print(myRegexLst[idx])

#Pooja Somayajula,4,2024
