import openai
import os

client = openai.OpenAI(api_key=os.environ.get("OPENAI_API_KEY", "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"))

while True:
    # Step 1: Ask the user what they want to do
    print("Welcome to the AI-powered study tool!")
    print("What would you like to do?")
    print("(1) Study")
    print("(2) Take a Free Response Question")
    print("(3) Answer Context based Questions")
    print("(4) Get Questions and Rubric")
    choice = input("Enter the number of your choice: ")

    if choice == "1":
        while True:
            topic = input("Enter a topic to study: ")
            combined_input = f"Explain {topic}"

            response = client.chat.completions.create(
                model="gpt-3.5-turbo",
                messages=[
                    {"role": "system", "content": "You are a helpful assistant."},
                    {"role": "user", "content": combined_input},
                ],
                temperature=0,
            )

            print(f"Study Content: {response.choices[0].message.content}")
            
            another_choice_study = input("\nDo you want to continue or Go back to Main Menu? Enter '1' to continue or '2' to go to Main Menu: ")
            if another_choice_study == '2':
                break

    if choice == "2":
        while True:
            topic = input("Enter a topic for the Free Response Quiz: ")
            question = f"Write one question about {topic}"

            response = client.chat.completions.create(
                model="gpt-3.5-turbo",
                messages=[
                    {"role": "system", "content": "You are a helpful assistant."},
                    {"role": "user", "content": question},
                ],
                temperature=0,

            )
            received_question = response.choices[0].message.content
            print(f"Question: {received_question}")
            
            answer = input("Enter your answer: ")
            combined_input = f"Is the answer to the question '{received_question}': {answer}?"
            response = client.chat.completions.create(
                model="gpt-3.5-turbo",
                messages=[
                    {"role": "system", "content": "You are a helpful assistant."},
                    {"role": "user", "content": combined_input},
                ],
                temperature=0,
            )
            
            print(f"Grading: {response.choices[0].message.content}")

            another_choice_frq = input("\nDo you want to continue or Go back to Main Menu? Enter '1' to continue or '2' to go to Main Menu: ")
            if another_choice_frq == '2':
                break
        

    if choice == "3":
        while True:
            

            topic = input("Enter a topic for the context-based quiz: ")

            paragraph = f"Generate a paragraph about {topic}"
            response = client.chat.completions.create(
                model="gpt-3.5-turbo",
                messages=[
                    {"role": "system", "content": "You are a helpful assistant."},
                    {"role": "user", "content": paragraph},
                ],
                temperature=0,
            )
            received_paragraph = response.choices[0].message.content
            print(f"Content: {received_paragraph}")
            

            context = f"Generate a context-based question about {paragraph}"
            
            response = client.chat.completions.create(
                model="gpt-3.5-turbo",
                messages=[
                    {"role": "system", "content": "You are a helpful assistant."},
                    {"role": "user", "content": context},
                ],
                temperature=0,
            )

            
            context_quiz = response.choices[0].message.content
            
            print(f"Context Based Question: {context_quiz}")

            student_answer = input("Write your answer")
            combined_input = f"Here is a passage '{context}'. Based on the passage, is the answer to the question '{context_quiz}', {student_answer} correct?"

            response = client.chat.completions.create(
                model="gpt-3.5-turbo",
                messages=[
                    {"role": "system", "content": "You are a helpful assistant."},
                    {"role": "user", "content": combined_input},
                ],
                temperature=0,
            )
            
            print(f"Grading: {response.choices[0].message.content}")

            another_choice_context = input("\nDo you want to continue or Go back to Main Menu? Enter '1' to continue or '2' to go to Main Menu: ")
            if another_choice_context == '2':
                break


            
    

    if choice == "4":
        while True:
            topic = input("Enter a topic: ")
            question = f"Give me a question about {topic}?"

            response = client.chat.completions.create(
                model="gpt-3.5-turbo",
                messages=[
                    {"role": "system", "content": "You are a helpful assistant."},
                    {"role": "user", "content": question},
                ],
                temperature=0,
            )
            received_question = response.choices[0].message.content
            print(f"Question: {received_question}")

            input_answer = input("Enter your answer: ")

            rubric = f"Generate a rubric for the question :'{received_question}'"



            response = client.chat.completions.create(
                model="gpt-3.5-turbo",
                messages=[
                    {"role": "system", "content": "You are a helpful assistant."},
                    {"role": "user", "content": rubric},
                ],
                temperature=0,
            )

            print(f"Rubric: {response.choices[0].message.content}")

            another_choice_rubric = input("\nDo you want to continue or Go back to Main Menu? Enter '1' to continue or '2' to go to Main Menu: ")
            if another_choice_rubric == '2':
                break

    another_choice = input("\nDo you want to continue or quit? Enter '1' to continue or '2' to quit: ")
    if another_choice == '2':
        break