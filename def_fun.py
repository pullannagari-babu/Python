cars = [
    {"make":"ford","model":"cooper","mileage":2113,"fuel_consumed":23},
    {"make":"volvo","model":"cooper","mileage":123,"fuel_consumed":31}
    ]
def car_mileage(car):
    performance=car["mileage"] / car["fuel_consumed"] 
    return performance

def car_name(car):
    name=f"{car['make']} {car['model']}"
    return name
    

def print_car_info(car):
    name=car_mileage(car)
    performance=car_mileage(car)
    
    print(f"{name} does {performance} miles per km")
    
    
for car in cars:
    print_car_info(car)
