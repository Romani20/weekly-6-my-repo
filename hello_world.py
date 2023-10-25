def getTheStateOfTheWorld(array):
    a = ''
    if array.count("war") > array.count("peace"):
        a = "Bye bye world"
    else:
        a = "Hello world"
    return a
    
situation = ["war", "war"]
print(getTheStateOfTheWorld(situation))

situation1 = ["peace", "war"]
print(getTheStateOfTheWorld(situation1))