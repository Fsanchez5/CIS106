last_names = ["Sanchez", "Sosa", "Bernal", "Cisneros", "Rodriguez", 
  "Chavez", "Garcia", "Perez", "Gomez", "Bonilla"]

def display_names(names):
   for name in names:
       print(name)


def display_names_reverse(names):
     for name in reversed(names):
         print(name)
 
print("Names in original order:")
display_names(last_names)

print("\nNames in reverse order:")
display_names_reverse(last_names)