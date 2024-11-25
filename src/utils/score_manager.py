# score_manager.py

import json
import os
from src.core.settings import levels


SCORES_FILE = "scores.json"

class GameScore:
    def __init__(self, optimal_path_length):
        self.score = 100  # starting score
        self.modifications = 0
        self.path_length = 0
        self.optimal_path_length = optimal_path_length

    def add_modification(self):
        """Increment modifications and deduct points."""
        self.modifications += 1
        self.score -= 5  # Deduct points for each modification
        print(f"Modification made. Current score: {self.score}")

    def set_path_length(self, length):
        """Set the path length and calculate any penalty based on the optimal path."""
        self.path_length = length
        if length > self.optimal_path_length:  # Only penalize if path exceeds optimal length
            extra_steps = length - self.optimal_path_length
            self.score -= extra_steps * 2  # Deduct points for extra steps
            print(f"Path length set to {length}. Extra steps penalty applied. Current score: {self.score}")
        else:
            print(f"Path length set to {length}. No penalty applied as path is within optimal length.")

    def final_score(self):
        """Return the final score, ensuring it doesn’t go below zero."""
        return max(self.score, 0)


# Score Management Functions

import json
import os
from src.core.settings import levels

# Path to the scores file
SCORES_FILE = "scores.json"

class GameScore:
    def __init__(self, optimal_path_length):
        self.score = 100  # Starting score
        self.modifications = 0
        self.path_length = 0
        self.optimal_path_length = optimal_path_length

    def add_modification(self):
        """Increment modifications and deduct points."""
        self.modifications += 1
        self.score -= 5  # deduction for modification
        print(f"Modification made. Current score: {self.score}")

    def set_path_length(self, length):
        """Set the path length and calculate any penalty based on the optimal path."""
        self.path_length = length
        if length > self.optimal_path_length: # when length exceeds optimal length
            extra_steps = length - self.optimal_path_length
            self.score -= extra_steps * 2  # then educt points for extra steps
            print(f"Path length set to {length}. Extra steps penalty applied. Current score: {self.score}")
        else:
            print(f"Path length set to {length}. No penalty applied as path is within optimal length.")

    def final_score(self):
        """Return the final score, ensuring it doesn’t go below zero."""
        return max(self.score, 0)

# Score Management Functions

def load_scores():
    """Load scores from a file and ensure all levels have valid lists."""
    if os.path.exists(SCORES_FILE):
        with open(SCORES_FILE, "r") as file:
            try:
                scores = json.load(file)
                # init as lists
                for i in range(len(levels)):
                    level_key = str(i)
                    if not isinstance(scores.get(level_key), list):
                        scores[level_key] = []  # reset invalid 
            except json.JSONDecodeError:
                print("Error decoding scores file. Resetting to defaults.")
                scores = {str(i): [] for i in range(len(levels))}
    else:
        scores = {str(i): [] for i in range(len(levels))}  # init w/ empty lists
    
    return scores



def reset_scores():
    """Reset all scores to the original state."""
    initial_scores = {str(i): [] for i in range(len(levels))}
    with open(SCORES_FILE, "w") as file:
        json.dump(initial_scores, file)
    print("All scores have been reset to their original state.")


def get_player_rank(level_index, score):
    """Calculate the rank of the player's score for a specific level."""
    scores = load_scores()
    level_key = str(level_index)

    if level_key in scores:
        all_scores = scores[level_key]
        rank = 1
        for s in all_scores:
            if score < s:
                rank += 1
        return rank, len(all_scores)  #  rank, total players
    return 1, 1  # default 

def merge_sort_descending(array):
    """Sorts an array in descending order using merge sort."""
    if len(array) <= 1:
        return array  


    mid = len(array) // 2
    left_half = merge_sort_descending(array[:mid])
    right_half = merge_sort_descending(array[mid:])


    return merge_descending(left_half, right_half)

def merge_descending(left, right):
    """Merge two sorted arrays in descending order."""
    result = []
    while left and right:
        if left[0] >= right[0]:  # compare elements for descending order
            result.append(left.pop(0))
        else:
            result.append(right.pop(0))

    result.extend(left)
    result.extend(right)

    return result


def save_score(level_index, score):
    """Save the player's score for a specific level."""
    scores = load_scores()  

    level_key = str(level_index) 
    if level_key not in scores or not isinstance(scores[level_key], list):
        print(f"Fixing invalid score entry for level {level_index}.")
        scores[level_key] = []  #level key =list

    # add new score then sort
    scores[level_key].append(score)

    scores[level_key] = merge_sort_descending(scores[level_key])  

    # save back to the file
    with open(SCORES_FILE, "w") as file:
        json.dump(scores, file)
    print(f"Saved score {score} for Level {level_index + 1}")

def validate_scores(scores):
    """Ensure all scores in the file are lists."""
    for i in range(len(levels)):
        level_key = str(i)
        if not isinstance(scores.get(level_key), list):
            scores[level_key] = [] 
    return scores

class GameScore:
    def __init__(self):
        self.score = 100  # Starting score

    def deduct_hint_points(self):
        """Deduct points for using a hint."""
        deduction = 10  # Adjust as needed
        self.score = max(0, self.score - deduction)
        print(f"Hint used! {deduction} points deducted. Remaining score: {self.score}")



