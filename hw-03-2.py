import random

def get_numbers_ticket(min, max, quantity):
    try:        
        lottery_numbers = set() # збираємо виграші в множину
        if min > max:
            print ("Максимальне число повинно бути більше мінімального")
            return list(lottery_numbers)
        elif min <= 0:
            print ("Мінімальне число повинно бути більше нуля")
            return list(lottery_numbers)
        elif quantity > (max-min+1):
            print(f"Кількість білетів повинна бути меньше або дорівнювати {max-min+1}")
            return list(lottery_numbers)
        else:      
            while len(lottery_numbers) != quantity:
                    lottery_numbers.add(random.randint(min, max))   
            return list(sorted(lottery_numbers)) # переводимо в сортований список
        
    except:
        return list(lottery_numbers)
    

print("Ваші лотерейні числа:", (get_numbers_ticket(10, 14, 6)))



