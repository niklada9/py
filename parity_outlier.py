# You are given an array (which will have a length of at least 3,
# but could be very large) containing integers. The array is either entirely
# comprised of odd integers or entirely comprised of even integers except for
# a single integer. Write a method that takes the array as an argument
# and returns this "outlier"

def find_outlier(integers: object) -> object:
    # odd_true = False
    # odd_answer = 0
    even_true: bool = False
    even_answer = 0
    answer_not_even = False
    answer = 0
    i: int
    for i in integers:
        if i % 2 == 0:
            even_answer = i
            if not even_true:
                even_true = True
            else:
                answer_not_even = True
        odd_answer = i
        if answer_not_even:
            answer = odd_answer
        else:
            answer = even_answer
    return answer
    print(answer)

    # return None


lst = [2, 4, 6, 8, 10, 3]
find_outlier(lst)
lst = [2, 4, 0, 100, 4, 11, 2602, 36]
find_outlier(lst)
lst = [160, 3, 1719, 19, 11, 13, -21]
# find_outlier[2, 4, 6, 8, 10, 3]
# find_outlier[2, 4, 0, 100, 4, 11, 2602, 36]
# find_outlier[160, 3, 1719, 19, 11, 13, -21]
