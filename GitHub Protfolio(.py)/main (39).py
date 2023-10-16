print("WebSite Rating")
print()
website_name = input("Website Name: ")
website_URL = input("Enter URL: ")
discription = input("Write any discription: ")
Rating = input("Rate it out of(5/5):")
print()
print()
WebSite_rating = {"Name":website_name,"URL":website_URL,"Desription":discription,"Rating":Rating}
for i, j in WebSite_rating.items():
  print(f"{i}: {j}")