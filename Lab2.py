

def display_main_menu():
    print("Enter some numbers separated by commas:")

def get_user_input():
    user_input = input() ## Obtains the user input from the console
    float_list = []
    print("You entered: " + user_input)
    string_list = user_input.split(",") ## This splits the input string by commas into a list of strings

    # Converts the list into a list of floats
    for s in string_list:
          float_list.append(float(s))

    return float_list

def cal_average_temperature(num_list):
      #calculate the total sum of the list
      total = sum(num_list)

      #calculate the average temperature
      average = total / len(num_list)
      return average

def calc_min_max_temperature(num_list):
      # calculate the minimum value

        minimum = min(num_list)

      # calculate the maximum value
        maximum = max(num_list)
        
        return (minimum, maximum)


def main():
    print("ET0735 (DevOps for AIoT) - Lab 2 - Introduction to Python")
    display_main_menu()
    num_list = get_user_input()

if __name__ == "__main__":
            main()