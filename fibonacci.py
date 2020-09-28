import logging
import output_fib

def fibinnaci(a, b, fib_list):
    output_fib.output_fib()
    next_number = a + b
    fib_list.append(next_number)
    logging.debug("fib_list is {}".format(fib_list))
    count = 0
    if next_number < 10:
        fibinnaci(b, next_number, fib_list)
        count += 1
    else:
        logging.info("sequence ending")
    return fib_list


def main():
    fib_list = []
    fib_list = fibinnaci(0, 1, fib_list)
    print(fib_list)


if __name__ == '__main__':
    logging.basicConfig(filename="sequence.log", filemode='w',
                        level=logging.DEBUG)
    main()