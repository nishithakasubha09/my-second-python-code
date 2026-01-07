
Crime = ("Good Girl Bad Bood","As Good As Dead", "One Of Us Is Lying", "The Silent Patient")

Mystery = ("The Brothers Hawthorne", "The Grandest Game",  "Games Untold", "Glorious Rivals")

Hitler = ("The Boy in the striped pj's", "The Book thief", "All the light we cannot see")

StandAlones = (" The Girl Who Was Supposed to Die", "The Silent Patient")

# WDUWR means What do u want to read

WDUWR = input ("Please select a Genre \n Crime \n Mystery \n Hitler times \n StandAlones")

WDUWR = WDUWR.lower().strip()

if (WDUWR == "crime"):
    print (Crime)

elif (WDUWR == "mystery"):
    print (Mystery)

elif (WDUWR == "hitler times"):
    print (Hitler)

elif (WDUWR == "standalones"):
    print (StandAlones)

else:
    print ("Sorry, we don't have that genre.")