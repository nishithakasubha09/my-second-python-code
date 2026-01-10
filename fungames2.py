
Crime = ("Good Girl Bad Bood","As Good As Dead", "One Of Us Is Lying", "The Silent Patient")

Mystery = ("The Brothers Hawthorne", "The Grandest Game",  "Games Untold", "Glorious Rivals")

Hitler = ("The Boy in the striped pj's", "The Book thief", "All the light we cannot see")

StandAlones = (" The Girl Who Was Supposed to Die", "The Silent Patient")

# TBR means What do u want to read also means To Be Read

print ("Welcome to my book recommendation program!")

TBR = input ("Please select a Genre \n Crime \n Mystery \n Hitler times \n StandAlones \n")

TBR = TBR.lower().strip()

if (TBR == "crime"):
    print (Crime)

elif (TBR == "mystery"):
    print (Mystery)

elif (TBR == "hitler times"):
    print (Hitler)

elif (TBR == "standalones"):
    print (StandAlones)

else:
    print ("Sorry, we don't have that genre.")
