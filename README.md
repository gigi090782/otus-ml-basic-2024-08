"# otus-ml-basic-2024-08" 

Учимся работе с данными - от загрузки до моделирования

Цель:
В этом домашнем задании вам предстоит поработать с достаточно небольшим, но интересным датасетом по раку груди. Признаками в этом наборе данных являются различные измерения образований в груди, такие как радиус, симметричность, и т.д. Целевая переменная - диагноз, является ли новообразование злокачественным или нет.


Описание/Пошаговая инструкция выполнения домашнего задания:
Часть 1. EDA


Скачайте датасет по ссылке: https://www.kaggle.com/uciml/breast-cancer-wisconsin-data
Посмотрите на базовые статистики датасета: средние, медианы, и т.д.
Постройте гистограммы/распределения признаков, при этом используйте целевую переменную, чтобы сгруппировать и раскрасить гистограммы.
Постройте heatmap для матрицы корреляций, есть ли признаки, которые сильно скоррелированы? Какие это признаки?
Постройте для сильно скоррелированных признаков попарные scatterplot-ы, действительно ли наблюдается линейная зависимость?
Используя boxplots и группировку по целевой переменной, попробуйте предположить, по каким признакам наиболее удобно было бы отделить злокачественные новообразования от доброкачественных.

Также очень приветствуется ваша инициатива по визуализациям и исследовании данных :)


Часть 2. Моделирование при помощи kNN


Разбейте данные на train-test, отложив 30% выборки для тестирования.

Приведите все непрерывные переменные к одному масштабу при помощи стандартизации. Кратко поясните, почему стандартизация здесь нужна.

Постройте модель kNN "из коробки" без настройки параметров. Оцените метрики качества бинарной классификации (accuracy, precision, recall, f1_score), постройте ROC-кривую и посчитайте площадь под ней.

Теперь проведите настройку параметра числа соседей на кросс-валидации. Снова оцените результаты, стало ли лучше? :)