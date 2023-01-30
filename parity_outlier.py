# You are given an array (which will have a length of at least 3,
# but could be very large) containing integers. The array is either entirely
# comprised of odd integers or entirely comprised of even integers except for
# a single integer. Write a method that takes the array as an argument
# and returns this "outlier"

def find_outlier(integers: object) -> object:
    odd_more_than_one: bool = False
    even_more_than_one: bool = False
    answer_not_even: bool = False
    answer_not_odd: bool = False
    odd_answer = 0
    even_answer = 0
    answer = 0
    i: int
    for i in integers:
        if i % 2 == 0:
            if not even_more_than_one:
                even_answer = i
                even_more_than_one = True
            else:
                answer_not_even = True
        else:
            if not odd_more_than_one:
                odd_answer = i
                odd_more_than_one = True
            else:
                answer_not_odd = True

        if answer_not_even and not answer_not_odd:
            answer = odd_answer
        elif answer_not_odd and not answer_not_even:
            answer = even_answer
        else:
            pass
            # print('wrong input')
            # answer = even_answer
    print(answer)
    return answer

    # return None


lst = [2, 4, 6, 8, 10, 3]
find_outlier(lst)
lst = [2, 4, 0, 100, 4, 11, 2602, 36]
find_outlier(lst)
lst = [160, 3, 1719, 19, 11, 13, -21]
find_outlier(lst)
# find_outlier[2, 4, 6, 8, 10, 3]
# find_outlier[2, 4, 0, 100, 4, 11, 2602, 36]
# find_outlier[160, 3, 1719, 19, 11, 13, -21]
