import time
import hashlib


class User:

    def __init__(self, nickname, password, age):
        self.nickname = nickname
        self.password = self.hash_password(password)
        self.age = age

    def __str__(self):
        return f'{self.nickname}'

    def __eq__(self, other):
        return self.nickname == other.nickname

    def hash_password(self, password):  # https://docs.python.org/3/library/hashlib.html
        return hashlib.sha256(password.encode()).hexdigest()




class Video:

    def __init__(self, title, duration, adult_mode: bool = False):
        self.title = title
        self.duration = duration
        self.time_now = 0
        self.adult_mode = adult_mode

    def __str__(self):
        return self.title

    def __eq__(self, other):
        return self.title.lower() == other.title.lower()


class UrTube:
    def __init__(self):
        self.users = []
        self.videos = []
        self.current_user = None

    def log_in(self, nickname, password):
        password = hashlib.sha256(password.encode()).hexdigest()
        for user in self.users:
            if nickname == user.nickname and password == user.password:
                self.current_user = user
                print(f"Пользователь {nickname} вошёл в систему.")


    def register(self, nickname, password, age):
        new_user = User(nickname, password, age)
        if new_user in self.users:
            print(f"Пользователь {nickname} уже существует.")

        else:
            self.users.append(new_user)

            self.current_user = new_user
            print(f'Пользователь {new_user} вошел в систему')

    def log_out(self):
        self.current_user = None
        print(f'Пользователь вышел из системы')

    def add(self, *videos):
        for video in videos:
            if video not in self.videos:
                self.videos.append(video)

    def get_videos(self, search):
        titles = []

        for video in self.videos:
            if search.lower() in str(video).lower():
                titles.append(video.title)
        return titles

    def watch_video(self, title):
        if not self.current_user:
            print("Войдите в аккаунт, чтобы смотреть видео")
            return

        for video in self.videos:
            if video.title == title:
                if video.adult_mode and self.current_user.age < 18:
                    print("Вам нет 18 лет, пожалуйста покиньте страницу")
                    return



        for second in range(video.time_now + 1, video.duration + 1):
            print(second, end=' ')
            time.sleep(1)
        print("Конец видео")
        video.time_now = 0
        return





ur = UrTube()
v1 = Video('Лучший язык программирования 2024 года', 200)
v2 = Video('Для чего девушкам парень программист?', 10, adult_mode=True)

# Добавление видео
ur.add(v1, v2)

# Проверка поиска
print(ur.get_videos('лучший'))

print(ur.get_videos('ПРОГ'))


# Проверка на вход пользователя и возрастное ограничение
ur.watch_video('Для чего девушкам парень программист?')
ur.register('vasya_pupkin', 'lolkekcheburek', 13)
ur.watch_video('Для чего девушкам парень программист?')
ur.register('urban_pythonist', 'iScX4vIJClb9YQavjAgF', 25)
ur.watch_video('Для чего девушкам парень программист?')


# Проверка входа в другой аккаунт
ur.register('vasya_pupkin', 'F8098FM8fjm9jmi', 55)
print(ur.current_user)


# Попытка воспроизведения несуществующего видео
ur.watch_video('Лучший язык программирования 2024 года!')
