def main():
    plist = []

    begin = int(input('Enter a number greater than 1: '))
    end = int(input('Enter a number greater than begin: '))
    
    if begin > 1 and begin < end:
        for x in range(begin, end+1):
            is_prime = True
            if x <=1:
                is_prime = False
            for i in range (2, int(x**.5) + 1):
                if x % i == 0:
                    is_prime = False
                    break
            if is_prime:
                plist.append(x)
    print(*plist)


    return plist


if __name__ == '__main__':
    main()
