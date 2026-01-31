from typing import List

def score_evaluation_pipeline(scores: List[int]):
    for score in scores:
        if score < 50:
            print("Fail")
            continue
        print("Pass")

if __name__ == "__main__":
    try:
        user_input = input("Enter scores (space-separated): ")
        scores = list(map(int, user_input.split()))     
        score_evaluation_pipeline(scores)
    except ValueError:
        print("Invalid input. Please enter space-separated integers.")