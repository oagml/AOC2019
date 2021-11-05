


lower_limit = 248345
upper_limit = 746315


def double(number):
    number_string = str(number)
    double_flag = False

    for i in range(1, len(number_string)):
        if number_string[i] == number_string[i-1]:
            if i != (len(number_string) -1):
                if number_string[i] != number_string[i+1]:
                    if i > 1 and number_string[i] != number_string[i-2]:
                        double_flag = True
                        break
                    if i == 1:
                        double_flag = True
                        break
            else:
                if number_string[i] != number_string[i-2]:
                    double_flag = True
                    break


    return double_flag

                
test = 112222
print(double(test))

def nodecrease(number):
    number_string = str(number)
    nodecrease_flag = True
    for i in range(1, len(number_string)):
        if int(number_string[i]) < int(number_string[i-1]):
            nodecrease_flag = False
            break

    return nodecrease_flag

counter = 0
for i in range(lower_limit, upper_limit):
    if (double(i) and  nodecrease(i)):
        counter += 1
print(counter)
