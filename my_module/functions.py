from openai import OpenAI
client = OpenAI()


def llm(question):
    completion = client.chat.completions.create(
        model="gpt-3.5-turbo",
        messages=[
            {"role": "user", "content": question},
        ],
        max_tokens=200,
        temperature=0.99
    )
    answer = completion.choices[0].message.content

    return answer


preset = "You are the most chill cs professor in the world, Professor Foo Barstein. You are talking to me, a student in your class."


def gptchat(type=None, subject=None, preset=preset):
    if (type == "joke"):
        if (subject):
            response = llm(preset + "tell me a funny joke about " + subject)
        else:
            response = llm(preset + "tell me a funny joke")
    elif (type == "haiku"):
        if (subject):
            response = llm(preset + "tell me a haiku about " + subject)
        else:
            response = llm(preset + "tell me a haiku")
    elif (type == "compliment"):
        if (subject):
            response = llm(preset + "tell me a compliment about " + subject)
        else:
            response = llm(preset + "tell me a compliment")
    elif (type == "email"):
        if (subject):
            response = llm(preset + "write an email about " + subject)
        else:
            response = llm(preset + "write a random email to send to my boss")
    else:
        if (subject):
            response = llm(preset + subject)
        else:
            response = llm(preset + "say something random")
    return response


def cowtalk(type='joke'):
    words = gptchat(type).split()
    # Create a new list that includes 'moo' after every three words
    moo_words = []
    for i in range(0, len(words), 3):
        moo_words.extend(words[i:i+3])  # Add the next three words
        moo_words.append('moo')         # Follow them with 'moo'
    
    # Convert the list back into a string and remove the last 'moo' if it is extra
    moo_sentence = ' '.join(moo_words).rstrip(' moo')
    return moo_sentence


def onewordperline(type=False):
    words = gptchat(type).split()  # Split the response into words
    max_word_length = max(len(word) for word in words)
    output_lines = []

    for i in range(max_word_length):
        line = ''
        for word in words:
            if i < len(word):
                line += (word[i] + ' ')
            else:
                line += ('  ')  # Add two spaces for alignment
        output_lines.append(line)
    return '\n'.join(output_lines)


def changepreset():
    new_preset = input("Enter the new preset: ")
    global preset  # Use the 'preset' variable defined outside the function
    preset = new_preset


def main():
    # result = onewordperline()
    # Do something with the result if needed, for example:
    # print(result)
    pass


if __name__ == "__main__":
    main()
