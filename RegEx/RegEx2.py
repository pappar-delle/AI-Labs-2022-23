#In Q40-42, An Othello board is any string of length 64 made up of only the characters in "xX.Oo".  An Othello edge is any string of length 8 made up of only the charaters in "xX.Oo".  A hole means a period.

#Q40: Write a regular expression that will match on an Othello board represented as a string.
#Q41: Given a string of length 8, determine whether it could represent an Othello edge with exactly one hole.
#Q42: Given an Othello edge as a string, determine whether there is a hole such that if X plays to the hole (assuming it could), it will be connected to one of the corners through X tokens.  Specifically, this means that one of the ends must be a hole, or starting from an end there is a sequence of at least one x followed immediately by a sequence (possibly empty) of o, immediately followed by a hole.
#Q43: Match on all strings of odd length.
#Q44: Match on all odd length binary strings starting with 0, and on even length binary strings starting with 1.
#Q45: Match all words having two adjacent vowels that differ.
#Q46: Match on all binary strings which DON’T contain the substring 110.
#Q47: Match on all non-empty strings over the alphabet {a, b, c} that contain at most one a.
#Q48: Match on all non-empty strings over the alphabet {a, b, c} that contain an even number of a's.
#Q49: Match on all positive, even, base 3 integer strings.

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
