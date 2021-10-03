import requests
import xmltodict
from json import loads, dumps


contest = input()

participants = requests.get(f'http://127.0.0.1:7777/view/participants', params={'contest': contest})
dict_participants = xmltodict.parse(participants.text)['participants']['participant']
participants_info = loads(dumps(dict_participants))

participants_data = []

if type(participants_info) == dict:
    participant_data = {}
    login = participants_info.get('@login',)
    participant_data['login'] = login

    submissions = requests.get(f'http://127.0.0.1:7777/view/submissions', params={'contest': contest, 'login': login})
    dict_submissions = xmltodict.parse(submissions.text)['submissions']['submission']
    submissions_info = loads(dumps(dict_submissions))

    fines = tasks = 0
    if type(submissions_info) == dict:
        if submissions_info.get('@verdict',) == 'OK':
            tasks += 1
            fines += int(submissions_info.get('@timestamp',))

    elif type(submissions_info) == list:

        for submission in submissions_info:
            if submission.get('@verdict',) == 'OK':
                tasks += 1
                fines += int(submission.get('@timestamp',))

    participant_data['tasks'] = tasks
    participant_data['fines'] = fines

    participants_data.append(participant_data)

elif type(participants_info) == list:

    for participant in participants_info:
        participant_data = {}
        login = participant.get('@login',)
        participant_data['login'] = login

        submissions = requests.get(f'http://127.0.0.1:7777/view/submissions', params={'contest': contest, 'login': login})
        dict_submissions = xmltodict.parse(submissions.text)['submissions']['submission']
        submissions_info = loads(dumps(dict_submissions))

        fines = tasks = 0
        if type(submissions_info) == dict:
            if submissions_info.get('@verdict',) == 'OK':
                tasks += 1
                fines += int(submissions_info.get('@timestamp',))

        elif type(submissions_info) == list:

            for submission in submissions_info:
                if submission.get('@verdict',) == 'OK':
                    tasks += 1
                    fines += int(submission.get('@timestamp',))

        participant_data['tasks'] = tasks
        participant_data['fines'] = fines

        participants_data.append(participant_data)

more_tasks = less_fines = 0
winner_tasks = []
winner_fines = []
for participant_data in participants_data:
    tasks = participant_data.get('tasks',)
    fines = participant_data.get('fines',)
    if tasks:
        if tasks > more_tasks:
            more_tasks = tasks
            winner_tasks = [participant_data.get('login',)]

            if fines >= less_fines and less_fines == 0:
                less_fines = fines
                winner_fines.append(participant_data.get('login',))

            elif fines < less_fines:
                less_fines = fines
                winner_fines = [participant_data.get('login',)]
            
            elif fines == less_fines:
                winner_fines.append(participant_data.get('login',))

        elif tasks == more_tasks:
            winner_tasks.append(participant_data.get('login',))

            if fines >= less_fines and less_fines == 0:
                less_fines = fines
                winner_fines.append(participant_data.get('login',))

            elif fines < less_fines:
                less_fines = fines
                winner_fines = [participant_data.get('login',)]
            
            elif fines == less_fines:
                winner_fines.append(participant_data.get('login',))

winners = []

if len(winner_tasks) > 1:

    if len(winner_fines) > 1:
        for i in winner_fines:
            winners.append(i)
    else:
        winners = winner_fines

else:
    winners = winner_tasks

print(len(winners))
for winner in sorted(winners):
    print(winner)
