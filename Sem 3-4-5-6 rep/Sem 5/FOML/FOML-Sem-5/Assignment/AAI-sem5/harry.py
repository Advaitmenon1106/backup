from easy_logic import *

rain = Symbol("rain") #Its raining
hagrid = Symbol("hagrid") #Harry visited Hagrid
dumbledore = Symbol("dumbledore") #Harry visited dumbledore


sentence1 = Implication(Not(rain), hagrid)
sentence2 = Or(hagrid, dumbledore)
sentence3 = Not(And(hagrid,dumbledore))
sentence4 = dumbledore

knowledge = And(sentence1, sentence2)
knowledge.add(sentence3)
knowledge.add(sentence4)
print(knowledge)

model_check(knowledge, rain)

#Another way to do the same

knowledge = And(
    Implication(Not(rain), hagrid),
    Or(hagrid, dumbledore),
    Not(And(hagrid, dumbledore)),
    dumbledore
)

print(model_check(knowledge, rain))
