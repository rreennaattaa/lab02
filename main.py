import requests


city = "Moscow,RU"
appid = "3204ada786bdca3246d4f15e6c3095ab"

res = requests.get(
	"http://api.openweathermap.org/data/2.5/weather",
	params={'q': city, 'units': 'metric', 'lang': 'ru', 'APPID': appid}
)
data = res.json()

print("Город:", city)
print("Погодные условия:", data['weather'][0]['description'])
print("Температура:", data['main']['temp'])
print("Минимальная температура:", data['main']['temp_min'])
print("Максимальная температура", data['main']['temp_max'])
print(f"Скорость ветра - {data['wind']['speed']} м/c")
print(f"Видимость {data['visibility']}м")
print()

res = requests.get("http://api.openweathermap.org/data/2.5/forecast",
params={'q': city, 'units': 'metric', 'lang': 'ru', 'APPID': appid})
data = res.json()
print("Прогноз погоды на неделю:")
for i in data['list']:
	print(
		"Дата <",
		i['dt_txt'],
		"> \r\nТемпература <",
		'{0:+3.0f}'.format(i['main']['temp']),
		"> \r\nПогодные условия <",
		i['weather'][0]['description'],
		">",
		f"\r\nСкорость ветра - {i['wind']['speed']} м/c",
		f"\r\nВидимость {i['visibility']}м"
	)
	print("____________________________")
