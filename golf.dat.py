# Golf Scores in Python
# https://github.com/MikeTechSecurity/GolfData.git
# Function to record player scores into a file.

def main(filename="golf.dat"):
    # Open the file in write mode. If the file doesn't exist, it will be created.
    with open(filename, 'w') as golf_file:
        print("Enter player names and their scores.")
        print("Type 'DONE' when you are finished.\n")
        
        # Continue to ask for input until the user is finished
        while True:
            player_name = input("Enter player's name (or 'DONE' to finish): ")
            # Check for the sentinel value 'DONE' to exit the loop
            if player_name == 'DONE':
                break
            
            # Get the player's score and ensure it's valid
            player_score = input(f"Enter score for {player_name}: ")
            # Write the player's name and score to the file, separated by a comma
            golf_file.write(f"{player_name},{player_score}\n")
    
    print("All scores have been recorded.")

# Execute the function to start the program
main()