from flask import Flask, render_template, abort

app = Flask(__name__)

# --- Данные о котятах (в реальном проекте это будет база данных) ---
kittens_data = [
    {
        "id": 1,
        "name": "Барон",
        "age": "3 месяца",
        "price": "Цена по запросу.",
        "image": "images/kitten1.jpg",
        "description": "Ласковый и игривый котик, окрас - голубой. Приучен к лотку и когтеточке."
    },
    {
        "id": 2,
        "name": "Марта",
        "age": "2.5 месяца",
        "price": "Цена по запросу.",
        "image": "images/kitten2.jpg",
        "description": "Очаровательная кошечка, окрас - лиловый. Очень любит сидеть на руках."
    },
    {
        "id": 3,
        "name": "Снежок",
        "age": "3.5 месяца",
        "price": "Цена по запросу.",
        "image": "images/kitten3.jpg",
        "description": "Спокойный и умный котик, окрас - серебристая шиншилла. Станет верным другом."
    }
]

parents_data = [
    {
        "slug": "Ponchik",
        "name": "Ponchik Banburu Plush*RU",
        "breed": "Британская короткошерстная",
        "color": "Голубой (BRI a)",
        "image": "images/ponchik_dad.JPG",
        "description": "Этот котик из дружественного питомника. Очень красивый котик с отличным, плотным костяком, кобби типа. Шеhсть густая и красивого светлоголубого тона. Пончик очень ласковый и общительный. Имея отличную родословную, он является достойным продолжателем британского рода в нашем питомнике.",
        "full_description": ["Д.р 17 / 11 / 2019 г",
                             "Родители:",
                             "F : Ch. Mauriccio Cats Justinian (BRI a)",
                             "M : Ch. Emma Banburu Plush(BRI a)",
                             "Заводчик : Домакова Ирина",
                             "Владелец : Домакова Ирина",
                             "Тесты :",
                             "Группа крови А/b( ДНК тест)",
                             "Генотип : SS (не несет аллель длинношерстности) (ДНК тест)",
                             "PKD - NN (не несет аллель заболевания) (ДНК тест)",
                             "FeLV - негатив",
                             "FIV - негатив",
                             "HCM - normal"
                             ],
        "gallery_images": [
            "images/ponchik/ponchik1.JPG",
            "images/ponchik/ponchik2.JPG",
            "images/ponchik/ponchik3.JPG"
        ]
    },
    {
        "slug": "bella",
        "name": "Бэлла",
        "title": "Чемпион породы (CH)",
        "breed": "Британская короткошерстная",
        "color": "Лиловый (BRI c)",
        "image": "images/mom-cat.jpg",
        "description": "Элегантная и заботливая кошка, передающая котятам свои лучшие черты: круглую мордочку и яркие глаза.",

        # ИСПРАВЛЕНИЕ 2: Добавили недостающие ключи, чтобы структура была одинаковой
        # Они могут быть пустыми, но должны присутствовать
        "full_description": [
            "Бэлла - наша гордость.",
            "Обладает прекрасной родословной и отличными выставочными оценками."
        ],
        "gallery_images": [
            # Пока можно оставить пустым, если фото для галереи нет
            # "images/bella_gallery/1.jpg"
        ]
    }
]


# Маршрут для главной страницы (index)
@app.route('/')
def index():
    # Теперь передаем в шаблон список родителей
    return render_template('index.html', kittens=kittens_data, parents=parents_data)


# =============================================
# === НОВЫЙ ДИНАМИЧЕСКИЙ МАРШРУТ ДЛЯ РОДИТЕЛЕЙ ===
# =============================================
@app.route('/parent/<parent_slug>/')
def parent_profile(parent_slug):
    # Ищем родителя в нашем списке данных по его 'slug'
    parent_to_show = None
    for p in parents_data:
        if p['slug'] == parent_slug:
            parent_to_show = p
            break

    # Если родитель с таким slug не найден, показываем ошибку 404
    if not parent_to_show:
        abort(404)

    # Если нашли - отображаем его персональную страницу
    return render_template('parent_profile.html', parent=parent_to_show)


# --- Запуск приложения ---
if __name__ == '__main__':
    # debug=True позволяет видеть ошибки прямо в браузере и автоматически перезапускает сервер при изменениях в коде
    app.run(debug=True)
