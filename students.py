def rate_performance(score):
    if score >= 80:
        return "Distinction"
    elif score >= 60 and score < 70:
        return "Credit"
    elif score >= 40 and score < 50:
        return "Fair"
    else:
        return "Fail"

def main():
    score = float(input("Enter the student's score: "))
    result = rate_performance(score)
    print("Student's performance:", result)

if __name__ == "__main__":
    main()


