from flask import Flask, render_template, abort

# ИСПРАВЛЕНИЕ 1: Используем __name__
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

# --- Данные о родителях ---
parents_data = [
    {
        "slug": "Ponchik",
        "name": "Ponchik Banburu Plush*RU",
        "breed": "Британская короткошерстная",
        "color": "Голубой (BRI a)",
        "image": "images/ponchik_dad.JPG",
        "description": "Этот котик из дружественного питомника. Очень красивый котик с отличным, плотным костяком, кобби типа. Шерсть густая и красивого светлоголубого тона. Пончик очень ласковый и общительный. Имея отличную родословную, он является достойным продолжателем британского рода в нашем питомнике.",
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
        "slug": "otrada",
        "name": "CH. TIRLIKET OTRADA",
        "breed": "Британская короткошерстная",
        "color": "Голубой (BRI a)",
        "image": "images/otrada_mom.jpg",
        "description": "Otrada Tirliket - это удивительная красотка, которая родилась в нашем питомнике. Она унаследовала всё лучшее от своих родителей: обаятельный характер, яркие глаза и замечательную шубку. Её внешний вид вызывает восхищение, а личность - теплоту и доброту.",
        "full_description": [
            "Дата рождения: 07.07.23.",
            "Группа крови - B.",
            "RKD - негатив",
            "Не несет ген ДШ (гентест)."
        ],
        "gallery_images": [
            "images/otrada/otrada_1.JPG",
            "images/otrada/otrada_2.JPG",
            "images/otrada/otrada_3.JPG"
        ]
    },
    {
        "slug": "tiki_tak",
        "name": "Tirliket Tiki-Tak",
        "breed": "Британская короткошерстная",
        "color": "Лиловый (BRI c)",
        "image": "images/tiki_tak_mom.jpg",
        "description": "Tirliket Tiki-Tak - молодая и нежная кошечка, родившаяся в нашем питомнике с целью продолжения племенной работы. Она безумно ласкова и общительна, обладает отличной родословной. Эта красавица станет замечательным дополнением вашей семьи и продолжит славные традиции нашего питомника!",
        "full_description": [
            "Дата рождения: 20.08.24",
            "Группа крови: A/b"
        ],
        "gallery_images": [
            "images/tiki_tak/tiki_tak_1.JPG",
            "images/tiki_tak_mom.jpg"
        ]
    }
]


# Маршрут для главной страницы (index)
@app.route('/')
def index():
    # Передаем в шаблон список котят и родителей
    return render_template('index.html', kittens=kittens_data, parents=parents_data)


# Динамический маршрут для профилей родителей
@app.route('/parent/<string:parent_slug>/')
def parent_profile(parent_slug):
    # Ищем родителя в нашем списке данных по его 'slug'
    parent_to_show = None
    for p in parents_data:
        if p['slug'] == parent_slug:
            parent_to_show = p
            break

    # Если родитель с таким slug не найден, показываем ошибку 404
    if parent_to_show is None:
        abort(404)

    # Если нашли - отображаем его персональную страницу
    return render_template('parent_profile.html', parent=parent_to_show)


# --- Запуск приложения ---
# ИСПРАВЛЕНИЕ 2: Используем __name__ и '__main__'
if __name__ == '__main__':
    app.run(debug=True)