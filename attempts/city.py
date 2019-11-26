def hotel_cost(nights):
    #print("Cost")
    #print(140*nights)
    return 140*nights
def plane_ride_cost(city):
    if city == "Charlotte":
        return hotel_cost(183)
    elif city == "Tampa":
        #print("In here")
        return hotel_cost(220)
    elif city == "Pittsburgh":
        return hotel_cost(222)
    elif city == "Los Angeles":
        return hotel_cost(475)
    else:
        return 0
def rental_car_cost(days):
    #print "in rental"
    if days >= 7:
        return days*40-50
    elif days >= 3:
        return days*40-20
    else:
        return days*40
def trip_cost(city,days,spending_money):
    return spending_money + rental_car_cost(days) + hotel_cost(days) + plane_ride_cost(city)
def validcity(city):
    citylist = ["Tampa","Charlotte","Pittsburgh","Los Angeles"]
    if city == "":
        return False
    else:
        if city in citylist:
            return True
        if city not in citylist:
            return False
##print trip_cost("Tampa",5,800)
city = raw_input("Enter city name:")
days = int(raw_input("Enter number of days:"))
spending_money = int(raw_input("Enter the additional amount:"))
type(days)
type(spending_money)
'''city = "Tampa"
days = 9
spending_money = 100'''
total = trip_cost(city,days,spending_money)
#print total
if validcity(city):
    print "Your trip would cost $%d in total" %total
else:
    print "Invalid city code. Your trip would cost $%d in total" %total

