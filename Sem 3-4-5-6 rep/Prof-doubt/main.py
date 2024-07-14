import player
import team
#Main
query=input("""Select query type:
            - Player
            - Team""").lower()
if query=="player":
    format=input('''Enter format: 
             - Test
             - ODI
             - T20
             - All formats''').lower()
    role=input('''Enter role:
           - Batting
           - Bowling
           - Allround ''').lower()

    qparams={'class' : '11',
        'type' : 'allround'}
    if format=="test":
        qparams['class']=1
    elif format=="odi":
        qparams['class']=2
    elif format=="t20":
        qparams['class']=3

elif query=="team":
    format=input('''Enter format: 
             - Test
             - ODI
             - T20
             - All formats''').lower()
    qparams={'class' : '11',
        'type' : 'allround'}
    if format=="test":
        qparams['class']=1
    elif format=="odi":
        qparams['class']=2
    elif format=="t20":
        qparams['class']=3

pid=(int(input("Enter player id")))
p=player.Player(pid)
cricdata=player.Player.innlist(p,qparams)
print(cricdata)