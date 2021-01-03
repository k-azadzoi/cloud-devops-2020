# Solution to the Hacker Rank problem "Finding the percentage"

# This section was already given to us in the problem
if __name__ == '__main__':
    n = int(input())
    student_marks = {}
    for _ in range(n):
        name, *line = input().split()
        scores = list(map(float, line))
        student_marks[name] = scores
    query_name = input()

    student_scores = student_marks[query_name]  # Looks for the scores of a student
    total_score = sum(student_scores)   # Adds all the scores together
    avg_score = total_score / 3     # Divides total_score by 3
    print("{0:.2f}".format(avg_score))  # Prints out the avg score with decimal places
