#loose life
def lose_live_generator():
    lives = 3
    while lives > 0:
        yield f"You have {lives} lives left"
        lives -= 1
    yield "Game Over"

# Create the generator
lose_live = lose_live_generator()
print(next(lose_live))  # Output: "You have 3 lives left"
print(next(lose_live))  # Output: "You have 2 lives left"
print(next(lose_live))  # Output: "You have 1 live left"
print(next(lose_live))