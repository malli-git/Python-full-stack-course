Quiz = [
    {
        "question":"1.what is the captial of india?"
        "options":["A.Mumbai","B.Delhi","C.Vijayawada","D.Chennai"],
        "answer":"B"},
     {
        "question":"2.which language is used for web apps?"
        "options":["A.python","B.java","C.javascript","D.all of the above"],
        "answer":"D"},
     {
        "question":"3.what is 5 + 3?"
        "options":["A.5","B.8","C.7","D.6"],
        "answer":"B"},
     {
        "question":"4.which is fruit?"
        "options":["A.carrot","B.banana","C.beetroot","D.spinach"],
        "answer":"B"},
     {
        "question":"5.what does cpu stands for?"
        "options":["A.central unit","B.central processing unit","C.control unit","D.cpu"],
        "answer":"B"},
     {
        "question":"6.which number is even?"
        "options":["A.3","B.7","C.9","D.8"],
        "answer":"D"},
     {
        "question":"7.python is a ------language?"
        "options":["A.lowlevel language","BMachine","C.Highlevel language","D.Assembly"],
        "answer":"B"},
     {
        "question":"8.what is the output of 2 * 3?"
        "options":["A.4","B.6","C.7","D.8"],
        "answer":"B"},
     {
        "question":"1.what is the captial of Telangana?"
        "options":["A.Mumbai","B.Hyderbad","C.Vijayawada","D.Chennai"],
        "answer":"B"},
     {
        "question":"1.which data_type stores multiple values?"
        "options":["A.int","B.float","C.list","D.string"],
        "answer":"C"},
    ]

    score = 0

    for i in Quix:
        print(q['questions'])
        for option in q["options"]:
            print(options)


            user_answer = input("Enter your answer A/B/C/D):").upper()
            if user_answer == q["answer"]:
                print("correct\n")
                score +=1
                else:
                    print("wrong")

            print(f'your final score is {score}/10')
