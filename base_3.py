#5.if

player={
    "name":"seopho",
    "age":21,
    "fav_game_type":["heeling","simple"],
}
p_name=player["name"]
p_age=player["age"]
p_ga_ty=player["fav_game_type"]


def Que(Q_name=p_name,Q_age=p_age,Q_ga_ty=p_ga_ty):
    print(f"He name is {Q_name}?")
    if Q_name == p_name:
        print("Yes")
    else:
        print("NO")
    print(f"He is {Q_age}?")
    if Q_age == p_age:
        print("Yes")
    else:
        print("NO")
    print(f"He fav game type is {Q_ga_ty}?")
    if Q_ga_ty==p_ga_ty[0] or Q_ga_ty==p_ga_ty[1]:
        print("Yes")
    else:
        print("NO") 

Que(Q_name="seop",Q_age=21,Q_ga_ty="simple")

#6.for

for test in p_ga_ty:
    if test == "simple":
        break
    else:
        print(test)

for letter in "HELLO WORLD":
    if letter == 'R':
        break
    else:
        print(letter)

        
