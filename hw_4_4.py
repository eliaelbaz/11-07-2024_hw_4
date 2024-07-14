## start


print ("All numbers from 10 to 20:");
for num in range (10, 21):
    print(num, end=' ');

print ("\nAll numbers from 10 to 20 with a step of 2:");
for num in range(10, 21, 2):
    print(num, end=' ');

gap: int = int(input("\nPlease enter the gap: "));
print(f"All numbers from 10 to 20 with a step of {gap}:");
for num in range(10, 21, gap):
    print(num, end=' ');

start_point: int = int(input("\nPlease enter the start point: "));
end_point: int = int(input("Please enter the end point: "));
gap: int = int(input("Please enter the gap: "));

print (f"All numbers from {start_point} to {end_point} with a step of {gap}:");
for num in range(start_point, end_point + 1, gap):
    print(num, end=' ');

## End