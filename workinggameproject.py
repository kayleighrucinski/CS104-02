#List creation and searching
end=False
names=[]
for x in range (0,10):
  aname=input("Enter a name:")
  names.append(aname)
while not end:
  print("At any time you may type End with a capital and no spaces to end your search")
  print(names)
  search=input("Enter a name to look for:")
  if search==("End"):
    end=True
  elif search in names:
    print(search, "was found")
  elif search not in names:
      print (search, "was not found")
      
  
