import game_data
import random
import art


score_count = 0
continue_game = True
print(art.logo)
first_one = random.choice(game_data.data)

while continue_game:
    second_one = random.choice(game_data.data)
    print(f"you're right! Current score: {score_count}")
    print(f"Compare A: {first_one['name']}, a {first_one['description']}, from {first_one['country']}")
    print(art.vs)
    print(f"Compare B: {second_one['name']}, a {second_one['description']}, from {second_one['country']}")
    your_choice = input("Who has more followers? Type 'A or 'B': ").lower()
    
    if your_choice == 'a' and first_one['follower_count'] > second_one['follower_count']:
        score_count += 1
        first_one = second_one
    elif your_choice == 'a' and first_one['follower_count'] < second_one['follower_count']:
        print(f"Sorry, that's wrong. Final score: {score_count}")
        continue_game = False
        
    if your_choice == 'b' and second_one['follower_count'] > first_one['follower_count']:
        score_count += 1
        first_one = second_one
    elif your_choice == 'b' and second_one['follower_count'] < first_one['follower_count']:
        print(f"Sorry, that's wrong. Final score: {score_count}")
        continue_game = False

