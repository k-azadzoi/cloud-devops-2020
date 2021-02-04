# Given the participants' score sheet for your University Sports Day, you are required to find the runner-up score.
# You are given  scores. Store them in a list and find the score of the runner-up.

# Print the runner-up score

'''
Sample Input
5
2 3 6 6 5

Sample Output
5
'''


def runner_up_score(array):
    remove_duplicates = set(array)  # converts the array into a set data type, the set type removes duplicates
    sorted_array = sorted(remove_duplicates)  # sorted method to convert the set into an array of integers
    print(sorted_array[-2])  # prints the second element from the right


runner_up_score([2, 3, 6, 6, 5])
runner_up_score([25, 20, 84, 84, 90, 92, 77, 30, 77, 25])
