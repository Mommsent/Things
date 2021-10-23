
name="Zed Show"
age=35
height=180
heignt_in_metr=height/100
weight=80
wight_in_tonns=weight/1000
eyes="Blue"
teeth="White"
hair="brown"
total= age+height+weight

print (f"Lets speak about person named {name}.")
print (f"He`s weigt {weight} kg.")
print (f"It`s not so many")
print (f"If conversed to tonn, recived {wight_in_tonns}, and height to metrs, recived {heignt_in_metr}.")
print (f"He ha`s {eyes} eyes and {hair} hair.")
print (f"He`s teeth usually {teeth}, although he loves drink coffe.")
print (f"If I`m add {age},{height} and {weight}, i will get {total}")
print (f"Mary had little lamb.")
print ("He`s wool be white as {}.".format('snow'))
print (f"Everywhere, then Mary go,")
print (f"Little lamb always followed for her.")
print ("." * 10)
end1="B"
end2="a"
end3="d"
end4="d"
end5="e"
end6="G"
end7="a"
end8="i"

print(end1+end2+end3+end4+end5,end=" ")
print(end6+end7+end8)

d_artagnan="\t My name D`Artanyan."
athos="This sring\n divided into two."
porthos="I`m \\ - \\ mushketer!"

aranus="""
Hints:
\t* Graf from Gaskon
\t* connected My lady
\t* Baron\n\t* Order General
"""

print (d_artagnan)
print (athos)
print (porthos)
print (aranus)
def stats_and_other ():
    print(''' Dick ''')
    print (f"Anather string\n \t And tab) named {name}")
    print ("how old are you?", end='')
    age= input()
    print ("How do your height?", end='' )
    height= input()
    print ("How do you weight?", end='')
    weight=input()
    print (f"Your age is {age}, your height {height} and weight {weight}")

def my_stats ():
    my_age= input("How old are you? ")
    my_height=input("How height are you? ")
    my_weight= input("How weight are you? ")
    return (f"Your age is {my_age}, your height {my_height} and weight {my_weight}")
