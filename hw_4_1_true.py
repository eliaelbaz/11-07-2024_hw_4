## start - True
a = 5
b = 5
if a == b:
    print (f"was True for {a} {b}");
else:
    print (f"was False for {a} {b}");

a = 3
b = 4
c = 2
d = 5
if a + b and c + d:
    print (f"was True for {a} {b} {c} {d}");
else:
    print (f"was False for {a} {b} {c} {d}");

a = 7
b = 2
c = 1
d = 0
if a >= b or c > d:
    print (f"was True for {a} {b} {c} {d}");
else:
    print (f"was False for {a} {b} {c} {d}");

a = 6
b = 6
c = 3
d = 4
if a >= b or c < d:
    print (f"was True for {a} {b} {c} {d}");
else:
    print (f"was False for {a} {b} {c} {d}");

a = 2
b = 2
c = 1
d = 1
if a == b and c <= d:
    print (f"was True for {a} {b} {c} {d}");
else:
    print (f"was False for {a} {b} {c} {d}");

a = 1
b = 2
c = 3
d = 4
if True and a + b + c + d:
    print (f"was True for {a} {b} {c} {d}");
else:
    print (f"was False for {a} {b} {c} {d}");

a = 8
b = 3
if a != b:
    print (f"was True for {a} {b}");
else:
    print (f"was False for {a} {b}");

a = 0
b = 0
c = 5
if a != b and a <= c or a <= b or True:
    print (f"was True for {a} {b} {c}");
else:
    print (f"was False for {a} {b} {c}");

a = 0
b = 0
c = 7
if a != b and a <= c or a <= b or False:
    print (f"was True for {a} {b} {c}");
else:
    print (f"was False for {a} {b} {c}");

a = 9
b = 3
c = 2
d = 1
if b != 0 and d != 0 and a % b == 0 and c % d == 0:
    print (f"was True for {a} {b} {c} {d}");
else:
    print (f"was False for {a} {b} {c} {d}");

## End
