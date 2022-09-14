# Travelbag
# Skelettkod till uppgiften
from curses.ascii import isdigit


travelbag = []

jagvetinte = [1, 2, 3, 4]



while True:
   menyval = input("1. Kolla i resväskan\n"
                   "2. Lägg sak i resväskan\n"
                   "3. Ta bort sak i resväskan\n"
                   "4. Avsluta program: \n")

   if travelbag.isdigit():
        travelbag = int(travelbag)
   
   
   if menyval == "1":
       print(*travelbag, sep=", ")

   elif menyval == "2":
       new_thing =input("Vad vill du lägga till i din resväska? \n")
       travelbag.append(new_thing)

   elif menyval == "3":
       remove_thing =input("Vad vill du ta bort i din resväska? \n")
       travelbag.remove(remove_thing)

   elif menyval != jagvetinte:
       print("Välj något mellan 1-4!")
   
   elif menyval == "4":
       break