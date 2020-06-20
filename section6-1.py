# My Debugging file

from section6_ex import calcul1, calcul2

# Initialize empty arrays

array_len = 10000
var1 = list(map(lambda i: 1.0, range(array_len)))
var2 = list(map(lambda i: 2.0, range(array_len)))
var3 = list(map(lambda i: 3.0, range(array_len)))
var4 = list(map(lambda i: 4.0, range(array_len)))
wth_test = 0
print(var1)
print(var2)
print(var3)
print(var4)


# Define two functions:

def function_1(input):
    # Function 1
    for i in range(array_len):
        var2[i] = 2 * var1[i]
        var1[i] = calcul1(i, input)
        global wth_test
        wth_test += i
    return var1 + var2


def function_2(input):
    # Function 2
    for j in range(array_len):
        var3[j] = calcul2(j, input)
        var4[j] = 2 * var3[j]
        global wth_test
        wth_test += j
    return var3 + var4


# print(function_1(1))
# print(function_2(2))

Output1 = function_1(1) + function_2(2)
Output2 = function_1(3) + function_2(4)
Output3 = function_1(4) + function_2(5)

print(Output1, type(Output1))
print(Output2, type(Output2))
print(Output3, type(Output3))
print('watch test > ', wth_test)
