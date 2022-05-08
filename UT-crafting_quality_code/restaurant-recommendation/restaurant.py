s = "ali"
s = "kogok"
for i in range(len(s) // 2):
  if s[i] != s[len(s) - i]:
    print( False)
    
print(True)