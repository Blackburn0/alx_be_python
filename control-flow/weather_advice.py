weather = ["sunny", "rainy", "cold"]

today_weather = input("What's the weather like today? (sunny/rainy/cold):")

if today_weather == weather[0]:
    print("Wear a t-shirt and sunglasses.")
elif today_weather == weather[1]:
    print("Don't forget your umbrella and a raincoat.")
elif today_weather == weather[2]:
    print("Make sure to wear a warm coat and a scarf.")
else:
    print("Sorry, I don't have recommendations for this weather.")

