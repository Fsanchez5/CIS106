def calculate_mpg(miles, gallons):
  if gallons == 0:
      return 0.0  
  return miles / gallons

def main():
  trip_count = 0
  while True:
      try:
          destination = input("Enter destination city (or 'stop' to end): ")
          if destination.lower() == 'stop':
              break
          miles = float(input("Enter miles travelled: "))
          gallons = float(input("Enter gallons used: "))
          mpg = calculate_mpg(miles, gallons)
          print(f"Destination: {destination}, Miles: {miles:.2f}, MPG: {mpg:.2f}")
          trip_count += 1
      except ValueError:
          print("Invalid input. Please enter numerical values for miles and gallons.")

  print(f"Total number of trips entered: {trip_count}")