students = {
    "Daniel": 92,
    "Mukenya":78,
    "Nyongesa":56,
    "Mkate":41,
    "Junior":99,
    "Sikuku":34
}
#91 - 100 = A+
#81 - 90 = A
#71 - 80 = B+
#61 - 70 = B
#51 - 60 = C
#41 - 50 = D
#Below 40 = F
grading = {}

for stude in students:
    alama = students[stude]
    if alama >90:
        grading[stude] = "A+"

    elif alama > 80:
        grading[stude] = "A"

    elif alama > 70:
        grading[stude] = "B+"

    elif alama > 60:
        grading[stude] = "B"

    elif alama > 50:
        grading[stude] = "C"

    elif alama > 40:
        grading[stude] = "D"

    else:
        grading[stude] = "F"

print(grading)
print("Shukran, a sample of grading program not much innit")