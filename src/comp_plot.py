#! /usr/bin/python3
"""
plot two lists of values
"""
from matplotlib import pyplot as plt


def compare_plot(lst_rsa, lst_pjct, res_lst):
    """
        Plot the accessibility values obtained by our program and the ones
        given by naccess
        Arguments :
            lst_rsa : list of naccess residus accessibility
            lst_pjct : list of our residus accessibility
            res_lst : list of residu names
    """
    compare = []
    for i in range(len(lst_rsa)-(len(lst_rsa)-len(lst_pjct))):
        compare.append(abs(lst_rsa[i]-lst_pjct[i]))
    plt.plot(lst_rsa, label="Naccess result")
    plt.plot(lst_pjct, label="Our result")
    plt.plot(compare, label="Difference")
    plt.xticks(range(len(lst_rsa)), res_lst)
    plt.xlabel("Residus")
    plt.ylabel("Accessibility")
    plt.legend()
    plt.show()


if __name__ == "__main__":
    import comp_plot
    print(help(comp_plot))
