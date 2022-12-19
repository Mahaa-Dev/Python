score = int(input("Enter your marks: "))
if score >= 40:
    if score >= 90:
        print("you have achieved A grade ", score)
    if score >= 80 and score < 90:
        print("Grade B ", score)
    if score >= 70 and score < 80:
        print("Grade C ", score)
    if score >= 60 and score < 70:
        print("Grade D ", score)
    else:
        print("Grade F", score)
else:
    print("Try next year")

