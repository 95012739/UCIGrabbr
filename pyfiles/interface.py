#instructions

#What Dataset
#Bucket name 
    # - can this be an existing bucket

#How much data? What columns?

#Call interact?

def usr_input():
    dataset=str(input("\nWhat Dataset: "))
    buck = str(input("\nWhat Bucket: "))
    spcl = int(input("\nAny Special Instructions? Type 0 if none: "))
    if spcl == 0:
        return
    else:
        print(dataset + buck)
    #....

