reddit = ("u/", "replied", "reddit", "Reddit")
byjus = ("Byju's", "BYJU's" )
khanacad = ("Khan", "Academy" "learning")
horror = ("horror", "Sci-Fi", "Thrillers", "Thriller", "Mystery", "mystery")
freq = {}
with open("C:/Users/Kavita manoj/OneDrive/Desktop/MU PY/MU Training Cases/Goodreads5.txt") as f:
    def addToGoodreads():
        lines = f.readlines()
        for x in lines:
            for y in range (0, len(horror)):
                flag = horror[y]
                if x.find(flag) != -1:
                    print ("Horror")
                    if x in freq:
                        freq[x] +=1
                    else:
                        freq[x] = 1
                else :
                    print ("Not horror")

print (freq)
