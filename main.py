import requests

# Задание 1

def find_unique_names(mentors_list: list):
    all_names_list = []
    for one_list in mentors_list:
        for mentor in one_list:
            name = mentor.split()[0]
            all_names_list.append(name)
    unique_names = set(all_names_list)
    res = sorted(unique_names)
   
    return res


def sort_course_by_duration(courses_list:list, mentors_list:list, durations):
    course_list = []
    for course, mentor, duration in zip(courses_list, mentors_list, durations):
         course_dict = {"title":course, "mentors":mentor, "duration":duration}
         course_list.append(course_dict)
       
    durations_dict = {}
    for id, course in enumerate(course_list):
        key = course['duration']
        durations_dict.setdefault(key, [])
        durations_dict[key].append(id) 
    durations_dict = dict(sorted(durations_dict.items()))
    list_of_durations = []
    for k, v in durations_dict.items():
        for i in v:
            list_of_durations.append(f'{course_list[i]["title"]} - {k} месяцев')
    
    return list_of_durations

def find_three_popular_names(mentors_list):
    all_names_list = []
    for one_list in mentors_list:
        for mentor in one_list:
            name = mentor.split()[0]
            all_names_list.append(name)
    unique_names = set(all_names_list)
    popular = []
    for unique_name in unique_names:
        popular.append([unique_name, all_names_list.count(unique_name)])
    popular.sort(key=lambda x:x[1], reverse=True)
    top_3 = popular[0:3]
    res = [f'{str(top[0])}: {str(top[1])} раз(а)' for top in top_3]
    return res

# Задание 2

def add_folder_yandex(token_yandex: str, name_of_folder: str):
    url_folder = 'https://cloud-api.yandex.net/v1/disk/resources'
    response = requests.put(url_folder, headers ={'Authorization': 'OAuth {}'.format(token_yandex)}, params = {'path' : name_of_folder})
    return response.status_code

def check_folder_yandex(token_yandex: str, name_of_folder: str):
    url_folder = 'https://cloud-api.yandex.net/v1/disk/resources'
    response = requests.get(url_folder, headers ={'Authorization': 'OAuth {}'.format(token_yandex)}, params = {'path' : name_of_folder})
    return response.status_code

