"""
TESTS is a dict with all of your tests.
Keys for this will be the categories' names.
Each test is a dict with
    "input" -- input data for a user function
    "answer" -- your right answer
    "explanation" -- not necessarily a key, it's used for an additional info in animation.
"""


TESTS = {
    "Basics": [
        {
            "input": [[1, 1, 1, 1]],
            "answer": [4]
        },
        {
            "input": [[1, 1, 2, 2]],
            "answer": [2, 4]
        },
        {
            "input": [[1, 1, 2, 1]],
            "answer": [2, 2, 1]
        },
        {
            "input": [[3, 3, 3, 4, 4, 5, 6, 6]],
            "answer": [9, 8, 5, 12]
        },
        {
            "input": [[1]],
            "answer": [1]
        },
        {
            "input": [[]],
            "answer": []
        }
    ],
    "Extra": [
        {
            "input": [[1,4,4,4,0,4,3,3,1]],
            "answer": [1,12,0,4,6,1]
        },
        {
            "input": [[1,1,7,7,3]],
            "answer": [2,14,3]
        }
    ]
}
