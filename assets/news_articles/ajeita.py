import json
from datetime import datetime, timedelta
from collections import Counter
import random

# Carregar os dados do arquivo JSON
with open('news_data.json', 'r', encoding='utf-8') as file:
    news_data = json.load(file)

# Definir o intervalo de datas
start_date = datetime.strptime("01/01/2006", "%d/%m/%Y")
end_date = datetime.strptime("07/06/2006", "%d/%m/%Y")

# Atualizar o atributo "date" para um dia aleatório entre start_date e end_date
date_range = (end_date - start_date).days
for news in news_data:
    random_days = random.randint(0, date_range)
    random_date = start_date + timedelta(days=random_days)
    news["date"] = random_date.strftime("%d/%m/%Y")

# Contar autores e bibliografias
authors = [news.get("author", "Unknown") for news in news_data]
bibliographies = [news.get("bibliography", "Unknown") for news in news_data]

author_counts = Counter(authors)
bibliography_counts = Counter(bibliographies)

# Exibir autores distintos e suas quantidades
print("Autores distintos e suas quantidades:")
for author, count in author_counts.items():
    print(f"{author}: {count}")

# Exibir bibliografias distintas e suas quantidades
print("\nBibliografias distintas e suas quantidades:")
for bibliography, count in bibliography_counts.items():
    print(f"{bibliography}: {count}")

# Salvar os dados atualizados de volta no arquivo JSON
with open('news_data.json', 'w', encoding='utf-8') as file:
    json.dump(news_data, file, ensure_ascii=False, indent=4)