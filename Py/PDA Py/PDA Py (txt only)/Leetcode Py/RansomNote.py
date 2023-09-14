#check if the letters of a ransom note can be constructed from a magazine

ransom = input()
magazine = input()

def ransomNote(r, m):
    if len(r)>len(m):
        return False
    else:
        for x in r:
            for y in m:
                if x == y:
                    return True
                else:
                    return False

if ransomNote(ransom, magazine):
    print ("yes")
else:
    print ("no")