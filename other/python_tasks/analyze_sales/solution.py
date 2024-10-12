def analyze_sales(input_strings):
    results = []
    porog = int(lines[-1])
    products = lines[0:-1]
    for product in products:
        product_list = product.split(',')
        product_name = product_list[0]
        product_prices = product_list[1:]
        sum_price = 0
        for price in product_prices:
            sum_price += int(price)
        average = round(sum_price/len(product_prices), 1)
        if average > porog:
            results.append((product_name, average))
    if not results:
        print("Нет данных")
    else:
        results = sorted(results, key=lambda t: (t[1], t[0]), reverse=True)
        results = [f'{name},{price:.1f}' for (name, price) in results]
    return results


lines = [
    "Яблоко,100,200,150",
    "Банан,50,60,55",
    "Апельсин,80,90,85",
    "Манго,120,130,110",
    "70"
]

for product in analyze_sales(lines):
    print(product)

# output:
# Яблоко,150.0
# Манго,120.0
# Апельсин,85.0

# lines = []
# while True:
#     try:
#         line = input()
#         if line == "":
#             break
#     except EOFError:
#         break
#     lines.append(line)

# for product in analyze_sales(lines):
#     print(product)
