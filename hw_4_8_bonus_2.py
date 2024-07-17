## start
print ("Enter IQ values for the control group before training (values must be between 30 and 300):");
sum_iq_before = 0;
count_iq_before = 0;
min_iq_before = float('inf');
max_iq_before = float('-inf');

while True:
    iq = int(input("Enter IQ value (before): "));
    if iq < 30 or iq > 300:
        break
    sum_iq_before += iq;
    count_iq_before += 1;
    min_iq_before = min(min_iq_before, iq);
    max_iq_before = max(max_iq_before, iq);

if count_iq_before > 0:
    avg_iq_before = sum_iq_before / count_iq_before;
    print (f"Before training - Average IQ: {avg_iq_before:.2f}, Minimum IQ: {min_iq_before}, Maximum IQ: {max_iq_before}");
else:
    avg_iq_before = None
    print ("No valid IQ values were entered before training.");

print ("One year of python training has been completed...");

print ("Enter IQ values for the control group after training (values must be between 30 and 300):");
sum_iq_after = 0;
count_iq_after = 0;
min_iq_after = float('inf');
max_iq_after = float('-inf');

while True:
    iq = int(input("Enter IQ value (after): "));
    if iq < 30 or iq > 300:
        break
    sum_iq_after += iq;
    count_iq_after += 1;
    min_iq_after = min(min_iq_after, iq);
    max_iq_after = max(max_iq_after, iq);

if count_iq_after > 0:
    avg_iq_after = sum_iq_after / count_iq_after;
    print(f"After training - Average IQ: {avg_iq_after:.2f}, Minimum IQ: {min_iq_after}, Maximum IQ: {max_iq_after}");

    if avg_iq_before is not None:
        iq_increase = avg_iq_after - avg_iq_before;
        print(f"Increase in average IQ: {iq_increase:.2f}");

        overall_min = min(min_iq_before, min_iq_after);
        overall_max = max(max_iq_before, max_iq_after);
        print(f"Overall - Minimum IQ: {overall_min}, Maximum IQ: {overall_max}");
else:
    print("No valid IQ values were entered after training.");
## End
