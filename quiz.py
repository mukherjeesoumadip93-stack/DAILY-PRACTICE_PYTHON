print("welcome to the quiz showdown")
name=input("enter your name:")

questions=(("What is the capital of France?"),
           ("Which planet is known as the Red Planet?"),
           ("Who wrote 'Romeo and Juliet'?"),
           ("What is the largest ocean on Earth?"),
           ( "Which language is primarily used for data science?"))

options=(("A.Berlin","B.Madrid","C.Paris","D.Rome"),
         ("A. Venus", "B. Mars", "C. Jupiter", "D. Saturn"),
         ("A. Charles Dickens", "B. William Shakespeare", "C. Mark Twain", "D. Jane Austen"),
         ("A. Atlantic Ocean", "B. Indian Ocean", "C. Arctic Ocean", "D. Pacific Ocean"),
         ("A. Python", "B. HTML", "C. CSS", "D. XML"))
guesses=[]
i=0
score=0
answers=("C", "B","B","D","A")

for item in questions:
    print(item,end=" ")
    print()
    for option in options[i]:
        print(option)

    guess=input("enter your choice:").upper()
    guesses.append(guess)
    if guess==answers[i]:
        print("Correct")
        score+=1
    else:
        print("incorrect")
        print(f"correct answer: {answers[i]}")
    i+=1
    print()
    print("_______________________")

print(f"{name},your total score is:{score}")




