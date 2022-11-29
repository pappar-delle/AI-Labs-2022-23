import sys; args = sys.argv[1:]
idx = int(args[0])-30

myRegexLst = [r"/^10[01]$|^0$/",
              r"/^[01]*$/",
              r"/0$/",
              r"/\b\w*[aeiou]\w*[aeiou]\w*\b/im",
              r"/^1[10]*0$|^0$/",
              r"/^[01]*110[01]*$/",
              r"/^.{2,4}$/s",
              r"/^\d{3} *-? *\d{2} *-? *\d{4}$/",
              r"/^.*?d\w*/mi",
              r"/^0[01]*?0$|^1[01]*?1$|^[01]?$/"]

if idx < len(myRegexLst):
  print(myRegexLst[idx])

#Pooja Somayajula,4,2024
