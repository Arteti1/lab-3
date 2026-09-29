from functools import reduce
reviews_data = [
    {"product": "Ноутбук ASUS ROG", "rating": 5, "comment": "Тягне всі ігри на ультрах, топ за свої гроші"},
    {"product": "Мишка Logitech G Pro", "rating": 4, "comment": "Зручна, але з'явився даблклік через півроку"},
    {"product": "Навушники Apple AirPods Pro", "rating": 5, "comment": "Шумодав працює ідеально, звук кайф"},
    {"product": "Монітор Samsung Odyssey", "rating": 3, "comment": "Є биті пікселі з коробки, довелось міняти"},
    {"product": "Клавіатура HyperX Alloy", "rating": 5, "comment": "Механіка просто супер, натискання чіткі"},
    {"product": "Ноутбук ASUS ROG", "rating": 2, "comment": "Гріється як пічка, кулери гудуть"},
    {"product": "Смартфон iPhone 15", "rating": 4, "comment": "Камера вогонь, але батарея тримає слабкувато"},
    {"product": "Смартфон iPhone 15", "rating": 5, "comment": "Перейшов з Андроїда, iOS працює дуже плавно"},
    {"product": "Мікрофон HyperX QuadCast", "rating": 5, "comment": "Для стрімів та дискорду кращого не знайти"},
    {"product": "Крісло Anda Seat", "rating": 3, "comment": "Спина не болить, але екошкіра почала тріскатись"}
]

def add_review(reviews, review):
    """ Додає новий відгук. """
    reviews.append(review)
    print("Відгук додано успішно.")
def remove_review(reviews, index):
    """ Видаляє відгук. """
    if 0 <= index < len(reviews):
        del reviews[index]
        print("Відгук видалено")
    else:
        print("Невірний індекс.")


def update_review(reviews, index, key, value):
    """ Оновлює відгук. """
    if 0 <= index < len(reviews):
        reviews[index][key] = value
        print("Відгук оновлено успішно.")
    else:
        print("Невірний індекс.")

def filter_by_rating(reviews, min_rating):
    """Знаходить всі продажі з певним рейтингом."""
    return list(filter(lambda x: x["rating"] >= min_rating, reviews))

def extract_all_comments(reviews):
    """Витягує всі коментарі з бази."""
    return list(map(lambda x: x["comment"], reviews))

def calculate_average_rating(reviews):
    """Обчислює середній рейтинг."""
    if len(reviews) == 0:
        return 0
    # reduce накопичує суму всіх рейтингів у змінну acc
    total_rating = reduce(lambda acc, x: acc + x["rating"], reviews, 0)
    return total_rating / len(reviews)

def get_unique_products(reviews):
    """Отримує перелік унікальних товарів."""
    return set(x["product"] for x in reviews)

def count_reviews_per_product(reviews):
    """Рахує кількість відгуків для кожного товару."""
    frequency = {}
    for x in reviews:
        product_name = x["product"]
        if product_name in frequency:
            frequency[product_name] += 1
        else:
            frequency[product_name] = 1
    return frequency


def print_menu():
    print("\n==== Меню аналізу відгуків ====")
    print("1. Показати всі відгуки")
    print("2. Додати новий відгук")
    print("3. Видалити відгук")
    print("4. Оновити відгук")
    print("5. Фільтрувати за мінімальним рейтингом")
    print("6. Показати всі коментарі (map)")
    print("7. Середній рейтинг (reduce)")
    print("8. Унікальні товари (set)")
    print("9. Кількість відгуків на товар (dict)")
    print("0. Вийти")

def main():
    while True:
        print_menu()
        choice = input("Оберіть опцію: ")
        
        if choice == '1':
            for i, r in enumerate(reviews_data):
                print(f"{i}: {r}")
                
        elif choice == '2':
            prod = input("Назва товару: ")
            try:
                rat = int(input("Рейтинг (1-5): "))
                com = input("Коментар: ")
                add_review(reviews_data, {"product": prod, "rating": rat, "comment": com})
            except ValueError:
                print("Помилка: рейтинг має бути числом!")
                
        elif choice == '3':
            try:
                idx = int(input("Індекс для видалення: "))
                remove_review(reviews_data, idx)
            except ValueError:
                print("Помилка: індекс має бути числом!")
                
        elif choice == '4':
            try:
                idx = int(input("Індекс для оновлення: "))
                key = input("Ключ (product/rating/comment): ")
                val = input("Нове значення: ")
                # Якщо оновлюємо рейтинг, перетворюємо його на число
                if key == "rating":
                    val = int(val)
                update_review(reviews_data, idx, key, val)
            except ValueError:
                print("Помилка вводу індексу або рейтингу!")
                
        elif choice == '5':
            try:
                min_r = int(input("Мінімальний рейтинг: "))
                res = filter_by_rating(reviews_data, min_r)
                for r in res:
                    print(r)
            except ValueError:
                print("Помилка вводу!")
                
        elif choice == '6':
            comments = extract_all_comments(reviews_data)
            for c in comments:
                print(f"- {c}")
                
        elif choice == '7':
            avg = calculate_average_rating(reviews_data)
            print(f"Середній рейтинг: {avg:.2f}")
            
        elif choice == '8':
            uniq = get_unique_products(reviews_data)
            print(f"Унікальні товари: {uniq}")
            
        elif choice == '9':
            counts = count_reviews_per_product(reviews_data)
            for p, c in counts.items():
                print(f"{p}: {c} відгуків")
                
        elif choice == '0':
            print("Роботу програми завершено.")
            break
            
        else:
            print("Невірний вибір. Спробуйте ще раз.")

if __name__ == "__main__":
    main()