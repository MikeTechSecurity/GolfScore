# Golf Scores in Python
# https://github.com/MikeTechSecurity/GolfScore.git
# Function to display all scores and the best score from the file.

def main(filename="golf.dat"):
    # Initialize best_score to infinity to easily find the lowest score
    best_score = float('inf')
    best_player_name = ""
    
    try:
        # Open the file in read mode.
        with open(filename, 'r') as golf_file:
            print("Golf Scores:")
            print("-------------")
            # Read each line from the file
            for line in golf_file:
                # Split the line into name and score based on the comma
                player_name, player_score = line.strip().split(',')
                # Convert the score from string to integer
                player_score = int(player_score)
                # Print the player's name and score
                print(f"{player_name}: {player_score}")
                
                # Check if the current score is the best (lowest) score
                if player_score < best_score:
                    best_score = player_score
                    best_player_name = player_name

        # After reading all records, check if we found a best score
        if best_score < float('inf'):
            print("\nBest Score:")
            print(f"{best_player_name} with a score of {best_score}")
        else:
            print("No scores to display.")
    # Catch the error if the file doesn't exist
    except FileNotFoundError:
        print(f"No records found in {filename}. Please make sure to record scores first.")

# Execute the function to start the program
main()