# Разработать программу для анализа лог-файлов веб-сервера с целью выявления основных паттернов использования ресурса. 
# Программа должна читать файл логов, анализировать данные о посещаемости сайта, определять наиболее посещаемые страницы 
# и анализировать источники трафика. В результате формируется отчет с детальной статистикой использования сайта.


# ip,ident,auth,timestamp,http request,status,size,referrer,user,agent

import pandas as pd
import re


log_pattern = r'(\d+\.\d+\.\d+\.\d+) - - \[(.*?)\] "(GET|POST|PUT|DELETE|HEAD) (.*?) (HTTP\/\d\.\d)" (\d+) (\d+) "(.*?)"\s*"(.*?)"'
logs = []
with open('task15.txt', 'r') as file:
    for line in file:
        match = re.match(log_pattern, line.strip())
        if match:
            logs.append({
                "IP": match.group(1),
                "Timestamp": match.group(2),
                "URL": match.group(4),
                "Referrer": match.group(8),
                "User-Agent": match.group(9)
            })

df = pd.DataFrame(logs)

df['Timestamp'] = pd.to_datetime(df['Timestamp'], format='%d/%b/%Y')
print(df)

url_counts = df['URL'].value_counts()
print("Наиболее посещаемые страницы:")
for url, count in url_counts.items():
    print(f"{url}: {count}")


date_counts = df['Timestamp'].value_counts()
print("Посещаемость по дням:")
for date, count in date_counts.items():
    print(f"{date}: {count}")