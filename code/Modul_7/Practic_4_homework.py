from statistics import mean
team1_num = 5
team2_num = 6

#Использование %

print('В команде Мастера кода участников: %d !' % team1_num)
print('Итого сегодня в командах участников: %d и %d !' % (team1_num, team2_num))

#Использование format():

score_2 = 42
team1_time = 18015.2
print('Команда Волшебники данных решила задач: {} !'.format(score_2))
print('Волшебники данных решили задачи за {} с !'.format(team1_time))

#Использование f-строк:

score_1 = 40
team2_time = 350.4

print(f'Команды решили {score_1} и {score_2} задач.')
def challenge_result(score_1, score_2, team1_time, team2_time):
    if score_1 > score_2 or score_1 == score_2 and team1_time > team2_time:
        print('Победа команды Мастера кода!')
    elif score_1 < score_2 or score_1 == score_2 and team1_time < team2_time:
        print('Победа команды Волшебники Данных!')
    else:
        print('Ничья!')

challenge_result(score_1, score_2, team1_time, team2_time)

tasks_total = score_1 + score_2
time_avg = mean([team1_time, team2_time])
print(f'Сегодня было решено {tasks_total} задач, в среднем по {time_avg} секунды на задачу!')
