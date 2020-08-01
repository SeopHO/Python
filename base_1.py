#1.data types and variable
a_num=2
print(type(a_num)) #int

a_float=2.65 
print(type(a_float)) #float

a_boolean_1=False 
a_boolean_2=True
print(type(a_boolean_1)) #bool

a_none=None #Not True, Not False Just None(Empty,Not exist) and Only have Python.
print(type(a_none)) #NoneType

a_string="Hello world!" 
a_='A'
print(type(a_string)) #string

#2.List and Tuple
a_list=["one","two","three","four"]
print(a_list)
print(type(a_list)) #list type

#'Python standard library' Search!
print("three"in a_list) #True
print("ten"in a_list) #True
print(a_list[2])
check=len(a_list)
print(check) #4

#**Mutable is can change Value
#**Immutable is can't change value
#LIST is Mutable.

a_list.append("FIVE")
print(a_list)
a_list.reverse()
print(a_list)

#3.Tuples(cant change) and Dicts
a_list_a=("one","two","three","four")
print(type(a_list_a))#list

#dict(dictonary)
player = {
    "name":"hoho",
    "age":"21",
    "fav_game":["lol","minecraft"] #dict in list.
}
print(player)
print(type(player)) #dict
player["Upadata"] = True #dict Add
print(player)



