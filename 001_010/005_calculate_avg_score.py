def grade_score(avg_score):
    if avg_score >= 8.5:
        return "Excelent"
    if avg_score >= 7.5:
        return "Very good"
    if avg_score >= 5.5:
        return "Good"
    if avg_score >= 4.5:
        return "Avegare"
    return "Bad"


scores = [10, 9, 6, 7]
avg_score = sum(scores) / len(scores)

grade = grade_score(avg_score)
print("The student has", avg_score, "and at the", grade, "level")
