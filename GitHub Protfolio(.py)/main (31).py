myAgenda = []

def printList():
  print() #this is just to add an extra space between items
  for item in myAgenda:
    print(item)
  print() #this is just to add an extra space between items

while True:
  item = input("What's next on the Agenda?: ")
  myAgenda.append(item)
  printList()