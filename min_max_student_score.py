student_scores = {'Ivan':5.00, 'Alex':3.50, 'Maria':5.50, 'Georgy':5.00}
for k,v in student_scores.items():
    if v == max(student_scores.values()):
        print(f"{k} - {v:.2f}")
    elif v == min(student_scores.values()):
        print(f"{k} - {v:.2f}")
