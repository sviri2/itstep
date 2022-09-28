# from unicodedata import name


# print("hallo world")
# print("BESIKI TSAKADZE")
# name = "BESIKI TSAKADZE"
# print(name)
def show_sequence(n):
    if n < 0:
        final_str = ""
        my_sum = 0
        for i in range(n+1):
            final_str += str(i) + "+"
            my_sum += i
            final_str = final_str[:-1]
            final_str += "="
            final_str += str(my_sum)
        return final_str
    elif n == 0:
        return "0=0"
    elif n < 0:
        return "{}<0".format(n)