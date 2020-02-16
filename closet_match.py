a = [8,9,13,17]
b = [4,8,10,20]
out = 18

least = ''
most_list = []
exact = []
prev_list = []
i = 0
def split_list(a, b):
    input_len = len(b)
    indx = int(input_len/2)-1
    sum = a[indx] + b[indx]
    if exact:
        return exact
    if sum < out:
        #print("input_len", input_len)
        for i in range(indx, input_len):
            sum = a[indx] + b[i]
            if sum == out:
                exact.append(sum)
                break
            elif sum < out:
                prev_list.append(sum)
            else:
                most_list.append(sum)
                x = a[indx:]
                y = b[indx:]
                split_list(x, y)
    elif sum > out:
        for i in range(indx+1):
            sum = a[0] + b[i]
            print(a[0], b[i])
            #print("sum", sum)
            if sum == out:
                exact.append(sum)
                break
            elif sum < out:
                prev_list.append(sum)
            else:

                most_list.append(sum)
                x = a[:indx]
                y = b[:indx]
                split_list(x,y)


split_list(a, b)
if exact:
    print("Found exact match", exact[0])
elif most_list:
    print("Max - ",most_list[0])
elif prev_list:
    print("MIn - ", prev_list[0])




