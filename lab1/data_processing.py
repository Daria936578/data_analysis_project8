import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Загрузка данных из CSV файла
data = pd.read_csv('lab1/sample_data.csv')

# Проверка типов данных и общий обзор
print("Информация о данных:")
print(data.info())

# Проверка пропущенных значений
print("\nПропущенные значения в данных:")
print(data.isnull().sum())

# Вывод первых строк данных
print("\nПервые результаты данных:")
print(data.head())

# Визуализация распределения калорийности
plt.figure(figsize=(8, 4))
sns.histplot(data['калорийность'], bins=10)
plt.title('Распределение калорийности продуктов')
plt.xlabel('Калории')
plt.ylabel('Количество продуктов')
plt.show()

# Визуализация распределения белков по категориям
plt.figure(figsize=(8, 4))
sns.boxplot(x='категория', y='белки', data=data)
plt.title('Распределение белков по категориям')
plt.xlabel('Категория')
plt.ylabel('Белки (г)')
plt.xticks(rotation=45)
plt.show()
