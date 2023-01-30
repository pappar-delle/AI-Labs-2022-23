import sys; args = sys.argv[1:]
idx = int(args[0])-50

myRegexLst = [r"/\w*(\w)\w*\1\w*/i", #50
              r"/\w*(\w)\w*(\1\w*){3}/i", #51
              r"/^([01])([10]*\1)*$/", #52
              r"/(?=\b\w{6}\b)\w*cat\w*/i", #53
              r"/(?=\b\w{5,9}\b)(?=\w*bri\w*)\w*ing\w*/i", #54
              r"/\b(?!\w*cat\w*)\w{6}\b/i", #55
              r"/\b(?!\w*(\w)\w*\1\w*)\w+\b/i", #56
              r"/(?!.*10011.*)^[01]*$/", #57
              r"/\b\w*([aeiou])(?!\1)[aeiou]\w*\b/i", #58
              r"/^(1(?!11)(?!01)|0)*$/"] #59

if idx < len(myRegexLst):
  print(myRegexLst[idx])

#Pooja Somayajula,4,2024
