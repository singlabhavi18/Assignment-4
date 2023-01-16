marks = float(input("Enter marks: "))
if 0 <= marks < 25:
    print("Grade - F")
elif 25 <= marks < 45:
    print("Grade - E")
elif 45 <= marks < 50:
    print("Grade - D")
elif 50 <= marks < 60:
    print("Grade - C")
elif 60 <= marks < 80:
    print("Grade - B")
elif marks < 0:
    print("Invalid marks")
else:
    print("Grade - A")
