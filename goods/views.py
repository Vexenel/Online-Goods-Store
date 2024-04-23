from django.shortcuts import render


def catalog(request):
    context = {
        "title": "Home - Каталог",
        "goods": [
            {
                "image": "deps/images/goods/set of tea table and three chairs.jpg",
                "name": "Набор:Мышка и клавиатура",
                "description": "Комплект офисной переферии из мышки и клавиатуры.",
                "price": 150.00,
            },
            {
                "image": "deps/images/goods/set of tea table and two chairs.jpg",
                "name": "Монитор Asus",
                "description": "Игровой монитор ASUS TUF Gaming VG27AQ1A основан на IPS-панели с частотой обновления 170 Гц.",
                "price": 93.00,
            },
            {
                "image": "deps/images/goods/double bed.jpg",
                "name": "Стол компьютерный Aceline Office ",
                "description": "Стол компьютерный Aceline Office 05 обеспечивает удобную организацию рабочего пространства в офисе или дома. ",
                "price": 670.00,
            },
            {
                "image": "deps/images/goods/kitchen table.jpg",
                "name": "Кресло офисное Aceline",
                "description": "Кресло офисное Aceline ACCT B обладает обивкой из текстиля и пропускающей воздух сетки. ",
                "price": 365.00,
            },
            {
                "image": "deps/images/goods/kitchen table 2.jpg",
                "name": "Мышь беспроводная/проводная LAMZU Atlantis",
                "description": "Мышь беспроводная LAMZU Atlantis выполнена в черном корпусе симметричной формы, что делает ее комфортной для хвата правой и левой рукой. ",
                "price": 430.00,
            },
            {
                "image": "deps/images/goods/corner sofa.jpg",
                "name": "Стиральная машина Indesit BWUA",
                "description": "Стиральная машина Indesit BWUA 41051 WB RU с фронтальной загрузкой вмещает 4 кг белья.",
                "price": 610.00,
            },
            {
                "image": "deps/images/goods/bedside table.jpg",
                "name": "Кондиционер настенный сплит-система DEXP",
                "description": "Кондиционер DEXP AC-CH7ONF функционирует в нескольких режимах и подходит для установки в помещении площадью до 20 м². ",
                "price": 55.00,
            },
            {
                "image": "deps/images/goods/sofa.jpg",
                "name": "Коврик Lamzu Energon черный",
                "description": "Он изготовлен из нейлона, что гарантирует легкое скольжение и точное управление.",
                "price": 190.00,
            },
            {
                "image": "deps/images/goods/office chair.jpg",
                "name": "Стул офисный",
                "description": "Описание товара, про то какой он классный, но это стул, что тут сказать...",
                "price": 30.00,
            },
            {
                "image": "deps/images/goods/plants.jpg",
                "name": "Растение",
                "description": "Растение для украшения вашего интерьера подарит свежесть и безмятежность обстановке.",
                "price": 10.00,
            },
            {
                "image": "deps/images/goods/flower.jpg",
                "name": "Цветок стилизированный",
                "description": "Дизайнерский цветок (возможно искусственный) для украшения интерьера.",
                "price": 15.00,
            },
            {
                "image": "deps/images/goods/strange table.jpg",
                "name": "Прикроватный столик",
                "description": "Столик, довольно странный на вид, но подходит для размещения рядом с кроватью.",
                "price": 25.00,
            },
        ],
    }
    return render(request, "goods/catalog.html",context)


def product(request):
    return render(request, "goods/product.html")
