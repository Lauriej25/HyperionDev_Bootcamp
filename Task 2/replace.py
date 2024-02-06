#Practical task 1 
#1 Replace all "!" from the sting with a single space 
#2 Then turn the sentence into all upper-case using upper()
#3 Print sentence backwards 
sentence = "The!quick!brown!fox!jumps!over!the!lazy!dog." 
sentence = sentence.replace("!"," ") #.replace to replace "!" with a space
print ("This is the sentence with '!' removed : {}".format(sentence))
print()
sentence = sentence.upper()
print(f"The sentence all in upper case : {sentence.upper()}") #.upper() to turn sentence to upper case
print()
print ("The sentence all lower case and written backwards :" ,f"{sentence.lower()}"[::-1] ) # using [::-1] to write the sentence backwards (-1 being the index for the last number) 
