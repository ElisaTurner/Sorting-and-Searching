# This program will ask for five numbers and sort them in order of
# smallest to largest while using the bubble sort algorithm
# This can also be done by using .sort()

def main():
    while True:
        print("Welcome to the Caesar Cipher Encryptor!\n")
        print("Give me five numbers, and I'll sort them from smallest to largest!\n")

        user_input = input("Please enter 5 numbers separated by commas: ")
        numbers = [int(num) for num in user_input.split(",")]  # Convert input to integers

        sorted_numbers = bubble_sort(numbers)
        print(f"Sorted numbers: {sorted_numbers}")

        # Ask if user wants to continue
        another = input("Do you want to check another set of numbers? (yes/no): ").lower()
        if another != 'yes':
            break

        
def bubble_sort(numbers):
    numbers_length = len(numbers)
    
    for i in range(numbers_length - 1):
        flag = 0
        
        for j in range(numbers_length - i - 1):
            if numbers[j] > numbers[j+1]:
                numbers[j], numbers[j+1] = numbers[j+1], numbers[j]
                flag = 1
        
        if flag == 0:
            break
    
    return numbers
    

        
# Call the main function
main()
