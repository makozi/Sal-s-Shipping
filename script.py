# Premium Ground Shipping Flat charge: $125.00
cost_premium_ground= 125.00

def cost_ground_shipping(weight):
  if weight <=2:
    price_per_pound=1.50
  elif weight <=6:
    price_per_pound=3.00
  elif weight <=10:
    price_per_pound=4.00
  else:
    price_per_pound= 4.75
  return 20 + (price_per_pound * weight)

# Testing the function
# print(cost_ground_shipping(8.4))



def cost_drone_shipping(weight):
  if weight <=2:
    price_per_pound=4.50
  elif weight <=6:
    price_per_pound=9.00
  elif weight <=10:
    price_per_pound=12.00
  else:
    price_per_pound= 14.25
  return 0.00 + (price_per_pound * weight)

# Testing the function
# print(cost_drone_shipping(1.5))

def cheapest_shipping_method(weight):
  ground= cost_ground_shipping(weight)
  drone= cost_drone_shipping(weight)
  premium=cost_premium_ground
  
  if ground< premium and ground < drone:
    method= 'Standard Ground'
    cost = ground
    
  elif drone < premium and drone <ground:
    method= 'Drone'
    cost = drone
    
  else:
    method= 'Premium Ground'
    cost = premium

  print("The cheapest option available is $%.2f  with %s shipping" % (cost, method))
  
  
# cheapest_shipping_method(4.8)
# cheapest_shipping_method(41.5)
