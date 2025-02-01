import requests
from PIL import Image
from io import BytesIO

# URL изображения
image_url = ""  # Замените на URL вашего изображения
image_url_arr = ["https://images.techinsider.ru/upload/img_cache/fe5/fe5f1d8d32b7f9384103a6a4b9d750a4_cropped_666x658.webp",
                 "https://images.techinsider.ru/upload/img_cache/a2d/a2db3d27774b5902f5be11e3cf2ed1e8_cropped_666x713.webp",
                 "https://images.techinsider.ru/upload/img_cache/4c0/4c0e9c7dcab50a042deaf80b4be2e833_cropped_666x719.webp",
                 "https://images.techinsider.ru/upload/img_cache/ef5/ef5a1ec5e421ec5962f3cd100b1b4398_cropped_666x933.webp",
                 "https://images.techinsider.ru/upload/img_cache/8cb/8cbad86b80d91d75618cfdee913778cc_cropped_666x664.webp",
                 "https://images.techinsider.ru/upload/img_cache/ff7/ff76775fd52c9ba2edabf9f26b466411_cropped_666x500.webp",
				 "https://images.techinsider.ru/upload/img_cache/f5b/f5bd1af0e38602f54f135ed07a01483a_cropped_666x761.webp",
				 "https://images.techinsider.ru/upload/img_cache/f95/f95f46aa2b36d173110a2b49d847c1bb_cropped_666x883.webp",
				 "https://images.techinsider.ru/upload/img_cache/979/979520e7827923bbb8bdb24279403452_cropped_666x832.webp",
				 "https://images.techinsider.ru/upload/img_cache/e03/e038316f548a36d582475228ad05d641_cropped_1332x832.webp"]

# Получение изобраения по URL
img_num = 0

while img_num != 9:
    response = requests.get(image_url_arr[img_num])
    if response.status_code == 200:
        img = Image.open(BytesIO(response.content))
        img.show()
        img_num += 1
    else:
        print(f"Не удалось загрузить изображение. Статус код: {response.status_code}")
        break
	