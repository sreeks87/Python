shopping_list = ["banana", "orange", "apple"]

stock = {
    "banana": 6,
    "apple": 0,
    "orange": 32,
    "pear": 15
}
    
prices = {
    "banana": 4,
    "apple": 2,
    "orange": 1.5,
    "pear": 3
}

# Write your code below!
def compute_bill(food):
    total = 0
    for each_item in  food:
        if stock[each_item] >0:
            total = total + prices[each_item]*food[each_item]
            stock[each_item] = stock[each_item]-food[each_item]
    return total
print compute_bill({"banana":2,"orange":5})
