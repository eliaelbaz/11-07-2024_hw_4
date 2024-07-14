## start
long_string = ""

while True:
    string1 = input("Enter the first string: ");
    string2 = input("Enter the second string: ");
    print(string1 + " " + string2);
    if long_string:
        long_string += " " + string1 + " " + string2;
    else:
        long_string = string1 + " " + string2;
    if string1 == string2:
        break

print ("The long concatenated string is:");
print (long_string);
##End