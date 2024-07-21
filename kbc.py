#KBC
questions = [
    "1. What is the capital of India?",
    "2. Which river is considered the holiest in India?",
    "3. Who was the first Prime Minister of independent India?",
    "4. What is the national animal of India?",
    "5. In which year did India gain independence from British rule?",
    "6. Which Indian city is known as the Silicon Valley of India?",
    "7. Who is known as the Father of the Indian Nation?",
    "8. What is the official currency of India?",
    "9. Which Indian state has the highest population?",
    "10. Which monument in India is considered one of the Seven Wonders of the World?"
]

options = [
    ["1. Mumbai", "2. New Delhi", "3. Kolkata", "4. Chennai"],
    ["1. Yamuna", "2. Godavari", "3. Ganga", "4. Brahmaputra"],
    ["1. Sardar Patel", "2. Lal Bahadur Shastri", "3. Jawaharlal Nehru", "4. Indira Gandhi"],
    ["1. Lion", "2. Tiger", "3. Elephant", "4. Peacock"],
    ["1. 1945", "2. 1947", "3. 1950", "4. 1952"],
    ["1. Hyderabad", "2. Pune", "3. Bangalore", "4. Chennai"],
    ["1. Jawaharlal Nehru", "2. Subhas Chandra Bose", "3. Mahatma Gandhi", "4. B. R. Ambedkar"],
    ["1. Dollar", "2. Euro", "3. Rupee", "4. Yen"],
    ["1. Maharashtra", "2. Bihar", "3. West Bengal", "4. Uttar Pradesh"],
    ["1. Qutub Minar", "2. India Gate", "3. Red Fort", "4. Taj Mahal"]
]

answers = ["2", "3", "3", "2", "2", "3", "3", "3", "4", "4"]
levels=["5000","10000","50000","100000","250000","500000","1000000","2500000","5000000","10000000"]
for i in range(10):
    quest = questions[i]
    print(quest)
    for option in options[i]:
        print(option)
    ans1 = input("Enter the right choice (1/2/3/4): ")
    for level in levels[i]:
        if ans1 == answers[i]:
            print(f"u won {levels[i]}")
        else:
            print("u r out")
        break
        
