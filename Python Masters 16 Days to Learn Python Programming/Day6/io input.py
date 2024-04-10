# file = open("test1.txt", "w")
# file.write("i am the new text")
# file.close()


from pathlib import Path

base = Path.home()
guide = Path(base,"Europe", "france",Path("Paris","Eiffel_tower.txt"))
# guide2 = guide.with_name("Nodre Dame.txt")
# print("base" , base)
print(guide.parent)
# print(guide2)
