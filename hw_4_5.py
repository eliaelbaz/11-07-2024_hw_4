## start

print ("Enter IQ values for the control group before training (values must be between 30 and 300)");

sum_iq_before = 0;
count_iq_before = 0;

while True:
    iq: int = int(input("Enter IQ value (before): "));
    if iq < 30 or iq > 300:
        break
    sum_iq_before += iq;
    count_iq_before += 1;

if count_iq_before > 0:
    average_iq_before = sum_iq_before / count_iq_before;
    print(f"Average IQ before training: {average_iq_before:.2f}");
else:
    print("No valid IQ values were entered before training.");

print("One year of python training has been completed...");

print("Enter IQ values for the control group after training (values must be between 30 and 300):");

sum_iq_after = 0;
count_iq_after = 0;

while True:
    iq = int(input("Enter IQ value (after): "));
    if iq < 30 or iq > 300:
        break
    sum_iq_after += iq;
    count_iq_after += 1;

if count_iq_after > 0:
    average_iq_after = sum_iq_after / count_iq_after;
    print(f"Average IQ after training: {average_iq_after:.2f}");

    if count_iq_before > 0:
        iq_increase = average_iq_after - average_iq_before;
        print(f"Increase in average IQ: {iq_increase:.2f}");
else:
    print("No valid IQ values were entered after training.");
##End