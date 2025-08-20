def format_phone_number(a):
    i = 0
    while i < len(a):
        b = str(a[i]);
        if not b.isdigit():
            a.pop(i)
        else: i += 1
    if a[0] != '0' or len(a) != 10:
        print("invalid phone number" )
        return
    s = "".join(a)
    print(s)
a = input()
a = list(a)
format_phone_number(a)