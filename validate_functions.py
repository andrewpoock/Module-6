# prints test score if it is valid input
def score_input(name, score, message):
    if 100 >= int(score) >= 0:
        return name + ': ' + str(score)
    else:
        raise ValueError
        print(message)


if __name__ == '__main__':
    try:
        print(score_input('Final', 95, 'input not valid'))
    except:
        raise ValueError("Value Error")
