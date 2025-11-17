from collections import deque

graph = {}
graph["Вы"] = ["Алиса", "Боб", "Клэр"]
graph["Боб"] = ["Анудж", "Пегги"]
graph["Алиса"] = ["Пегги"]
graph["Клэр"] = ["Том", "Джонни"]
graph["Анудж"] = []
graph["Пегги"] = []
graph["Том"] = []
graph["Джонни"] = []

def person_is_seller(name):
    '''Функция возвращает True если продавец манго, False, если нет'''
    return name[-1] == 'м'

def search(name):
    '''Функция принимает на вход имя, и ищет продавца манго в графе'''
    search_queue = deque()
    search_queue += graph[name]
    searched = set()
    while search_queue:
        person = search_queue.popleft()
        if not person in searched:
            if person_is_seller(person):
                print(person + " - родавец манго!")
                return True
            else:
                search_queue += graph[person]
                searched.add(person)
    return False

if __name__ == '__main__':
    search("Вы")