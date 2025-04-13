def load_data(filename):
  last_names = []
  scores = []

  with open(filename, 'r') as file:
      for line in file:
          name, score = line.strip().split()
          last_names.append(name)
          scores.append(int(score))

  return last_names, scores


def display_highest_score(names, scores):
  high_var = 0
  high_index = 0

  for i in range(len(scores)):
      if scores[i] > high_var:
          high_var = scores[i]
          high_index = i

  print(f"Highest Score: {scores[high_index]} by {names[high_index]}")


def display_lowest_score(names, scores):
  low_var = 999
  low_index = 0

  for i in range(len(scores)):
      if scores[i] < low_var:
          low_var = scores[i]
          low_index = i

  print(f"Lowest Score: {scores[low_index]} by {names[low_index]}")


def main():
  filename = "data.txt"
  names, scores = load_data(filename)

  print("Loaded Data:")
  for i in range(len(names)):
      print(f"{names[i]} - {scores[i]}")

  print("\nResults:")
  display_highest_score(names, scores)
  display_lowest_score(names, scores)

main()