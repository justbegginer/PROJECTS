import random
import time

#import missing as missing


def get_example_text():
    file = open("source", "r")
    texts = []
    with file as f:
        #while f.:
            texts.append(f.readline())
    print(len(texts))
    challenge_text = texts[random.randint(0, len(texts)) - 1]
    return challenge_text

def start_challenge(example_text):
    print(example_text)
    time_start = time.time()
    result = input()
    time_end = time.time()
    return result, time_end - time_start

def get_accuracy(default_text, challenge_text):
    default_text_array = default_text.split(' ')
    challenge_text_array = challenge_text.split(' ')
    result = {'missing symbols': 0, 'wrong symbols': 0, 'extra symbols' : 0}
    for i in range(len(default_text_array)):
        if len(challenge_text_array) <= i: # если слов в ответе меньше, чем в примере, считаем ,что все символы этих слов пропущены
            for ii in range(i, len(default_text_array)):
                result['missing symbols'] += len(default_text_array[ii])
            break
        else:
            for ii in range(len(default_text_array[i])):
                if len(challenge_text_array[i]) <= ii: # если слово в ответе меньше, чем в примере, считаем ,что все символы слова пропущены
                    result['missing symbols'] += len(default_text_array[i]) - len(challenge_text_array[i])
                else:
                    if (challenge_text_array[i][ii] != default_text_array[i][ii]):
                        result["wrong symbols"] += 1
            if len(challenge_text_array[i]) > len(default_text_array[i]):
                result['extra symbols'] += len(challenge_text_array[i]) - len(default_text_array[i])

    if len(challenge_text_array) > len(default_text_array):
        for i in range(len(default_text_array), len(challenge_text_array)):
            result["extra symbols"] += len(challenge_text_array[i])
    total_world = 0
    total_errors = 0
    for i in range(len(default_text_array)):
        total_world += len(default_text_array[i])
    for key in result:
        total_errors += result[key]
    return result,  ((total_world - total_errors) / total_world)*100




def main():
    input("Введите что-нибудь, чтобы начать испытание")
    default_text = get_example_text()
    challenge_text =""
    time = 0.0
    (challenge_text, time) = start_challenge(default_text)
    accuracy, percent_accuracy = get_accuracy(default_text, challenge_text)
    print(f"Вы выполнили задание за {str(time)} секунд\n"
          f"===========> Ваша точность <==========")
    print(accuracy)
    print(str(percent_accuracy) + "% of accuracy")

main()