def madlib():
    adj1 = input("Adjective: ")

    noun1 = input("Noun: ")
    noun2 = input("Noun: ")
    noun3 = input("Noun: ")
   
    body_part = input("Body part: ")

 
    verb_past = input("Verb (past tense): ")

    spell1 = input("Spell: ")
    spell2 = input("Spell: ")


    madlib = f"A {adj1} glow burst suddenly across the enchanted sky above them as an edge of \
dazzling sun appeared over the sill of the nearest {noun1}. The light hit both of their {body_part} \
at the same time, so that Voldemort’s was suddenly a flaming {noun2}. Harry heard the high voice \
shriek as he too {verb_past} his best hope to the heavens, pointing Draco’s {noun3}:\n\
\"{spell1}!\"\n\
\"{spell2}!\"\n\""
print(madlib)