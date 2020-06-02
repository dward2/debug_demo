
def define_things():
    global l3
    l3 = 7



def read_in_data(filename):
    out_list = list()
    with open(filename, 'r') as in_file:
        x = in_file.readlines()
        for line in x:
            out_list.append(line.strip("\n"))
    return out_list


def output_results(dataset):
    k = 0
    while k < l3:
        med_name = dataset[k]
        print("{}: {}".format(k, med_name))
        k += 1


if __name__ == '__main__':
    define_things()
    dataset_2 = read_in_data("data_ex2.txt")
    output_results(dataset_2)
    print("End program")

