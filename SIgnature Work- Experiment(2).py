# Import necessary libraries
import os  # Import the os module
from datetime import datetime
import tkinter as tk   # Import the tkinter library for creating a GUI interface
import csv   # Import the csv library for handling CSV files
import time   # Import the time library for handling time
from datetime import datetime   # Import the datetime class from the datetime library
from tkinter import messagebox  # Import messagebox to create message boxes or dialogs

# Initialize global variables
participant_id = ""  # Participant ID
test1_score = 0  # Manipulation Check Score
test2_speed = 0  # Experiment Part 1 typing Speed(WPM - Word Per Minutes)
test2_accuracy = 0  # Experiment Part 1 typing Accuracy Rate
test3_speed = 0  # Experiment Part 2 typing Speed(WPM - Word Per Minutes)
test3_accuracy = 0  # Experiment Part 2 typing Accuracy Rate
typing_data = []  # List to store typing data
current_typing = ""  # Current text being typed
typing_start_time = 0  # Typing start time
typing_end_time = 0  # Typing end time
typing_text = ""  # Typed text
typing_reference_text = ""  # Reference text
typing_timer = None  # Timer
current_question = 0  # Current question index

# Define a set of questions
questions = [
    {"question": "What is the primary goal of this study?", "options": ["A. To measure typing speed", "B. To conduct a post-experiment survey", "C. To explore the effects of short video viewing on cognitive performance", "D. To provide monetary compensation"], "correct_answer": "C"},
    {"question": "What is the focus of Stage 1 in the experiment?", "options": ["A. Playing computer games", "B. Training with BCI devices", "C. Watching movies"], "correct_answer": "B"},
    {"question": "What will be measured during the typing tasks in Stage 2 of the experiment?", "options": ["A. Participants' heart rate", "B. Participants' typing speed and accuracy", "C. Participants' ability to solve puzzles"], "correct_answer": "B"}
]

current_time_1 = 0  # Start time point for the experiemnt 
current_time_2 = 0  # Start time point for Manipulation Check 
current_time_3 = 0  # Start time point for Experiment Part 1
current_time_4 = 0  # Start time point for Experiment Part 2

# Function to get the current time
def get_current_time():
    current_time = time.time()
    dt_object = datetime.fromtimestamp(current_time)
    formatted_datetime = dt_object.strftime("%Y-%m-%d %H:%M:%S")
    return formatted_datetime

# Prepare participant ID interface
def prepare_interface():
    global participant_id
    root = tk.Tk()
    root.title("Typing Experiment")
    root.geometry("600x600")
    label = tk.Label(root, text="Please enter your participant ID:")
    label.pack()
    id_entry = tk.Entry(root)
    id_entry.pack()

    # "Next" button click event handler
    def next_button_click():
        global participant_id
        participant_id = id_entry.get()
        if participant_id:
            root.destroy()
            start_interface()
    next_button = tk.Button(root, text="Next", command=next_button_click)
    next_button.pack()
    root.mainloop()

# Start interface
def start_interface():
    global participant_id, current_time_1
    root = tk.Tk()
    root.title("Start Interface")
    root.geometry("600x600")
    label = tk.Label(root, text=f"Participant ID: {participant_id}")
    label.pack()

    # "Back" button click event handler
    def back_button_click():
        root.destroy()
        prepare_interface()
    back_button = tk.Button(root, text="Back", command=back_button_click)
    back_button.pack()

    # "Start" button click event handler
    def start_button_click():
        global current_time_1
        current_time_1 = get_current_time()
        root.destroy()
        explanation_interface()
    start_button = tk.Button(root, text="Start", command=start_button_click)
    start_button.pack()
    root.mainloop()

# Explanation interface for the experiment
def explanation_interface():
    root = tk.Tk()
    root.title("Experiment Explanation")
    root.geometry("600x600")
    scroll = tk.Scrollbar(root)
    scroll.pack(side=tk.RIGHT, fill=tk.Y)
    text = tk.Text(root, wrap=tk.WORD, yscrollcommand=scroll.set)
    text.pack()
    
    explanation_text = """
    Participant Information and Experiment Explanation

    Dear Participant,

    Thank you for your interest in participating in our study investigating the effects of short video addiction on cognitive performance. Before we proceed, we want to provide you with a clear understanding of the experiment's procedures and what you can expect during your participation.

    Objective of the Study:
    The primary goal of this study is to explore how addiction to watching short videos, particularly on platforms like TikTok, may influence an individual's ability to concentrate on cognitive tasks, such as typing.

    Experiment Overview:
    The experiment will consist of two stages.

    Stage 1 - BCI Device Training:
    In this initial stage, you will be introduced to Brain-Computer Interface (BCI) devices, which are non-invasive tools used to measure electrical activity in the brain. You will participate in a simple task that involves controlling the movement of a cursor on a computer screen using your thoughts. This stage is designed to help you become comfortable with the BCI equipment and improve your skills in using it.

    Stage 2 - Typing Tasks:
    This is the main phase of the experiment, and it will be divided into two sets: Set 1 and Set 2.

    Set 1: You will be required to type a passage from Act 1 of the play "Hamlet" on a computer keyboard. Your typing accuracy and speed will be measured during this task.

    Set 2: Similar to Set 1, you will type another passage from Act 2 of "Hamlet." However, there will be a 10-minute break between two 15-minute typing periods. During this break, you will have two options:

    - Rest quietly in your chair.
    - Use your own smartphone to watch short videos on TikTok.

    Important Points to Note:

    - You will be wearing the BCI equipment throughout Stage 2 to collect EEG data.
    - We will be monitoring your typing performance, including the number of words typed and any errors made.
    - The EEG data collected will help us understand brain activity during cognitive tasks and breaks.

    Post-Experiment Survey:
    After completing both sets of typing tasks, you will be asked to fill out a brief survey. This survey will inquire about your perceived level of concentration during the typing tasks and any distractions you experienced.

    Compensation:
    As a token of our appreciation for your time and effort, you will receive a monetary compensation of 50 RMB at the end of the study.

    Ethical Considerations:
    Your participation is voluntary, and your personal information will be kept confidential. Your rights and responsibilities as a participant will be fully explained, and you can withdraw from the study at any time without any consequences.

    Objective Concealment:
    To avoid potential bias in the data, we will not disclose the specific objectives of the study until the end.

    Conclusion:
    We are excited to have you participate in this study, as your involvement will contribute to a better understanding of the impact of short video addiction on cognitive processes. If you have any questions or concerns before or during the experiment, please do not hesitate to ask our research team.

    Thank you for your participation, and we look forward to conducting this experiment with you.
    """

    # Add the text
    text.insert(tk.END, explanation_text)
    # Configure a tag for bold text
    text.tag_configure("bold", font=("Arial", 12, "bold"))
    # Apply the bold tag to the relevant portions of the text
    text.tag_add("bold", "1.0", "1.end")  # Participant Information and Experiment Explanation
    text.tag_add("bold", "5.0", "5.end")  # Objective of the Study
    text.tag_add("bold", "8.0", "8.end")  # Experiment Overview
    text.tag_add("bold", "10.0", "10.end")  # Stage 1 - BCI Device Training
    text.tag_add("bold", "14.0", "14.end")  # Stage 2 - Typing Tasks
    text.tag_add("bold", "16.0", "16.end")  # Set 1:
    text.tag_add("bold", "18.0", "18.end")  # Set 2:
    text.tag_add("bold", "22.0", "22.end")  # Important Points to Note:
    text.tag_add("bold", "26.0", "26.end")  # Post-Experiment Survey:
    text.tag_add("bold", "28.0", "28.end")  # Compensation:
    text.tag_add("bold", "30.0", "30.end")  # Ethical Considerations:
    text.tag_add("bold", "32.0", "32.end")  # Objective Concealment:
    text.tag_add("bold", "34.0", "34.end")  # Conclusion:
    # Make the text read-only
    text.config(state=tk.DISABLED)
    scroll.config(command=text.yview)

    # "Go to Next Part" button click event handler
    def goto_next_page():
        root.destroy()
        manipulation_check_interface()
    next_button = tk.Button(root, text="Go to Next Part", command=goto_next_page)
    next_button.pack()

    # Automatically proceed to the next page after 10 minutes
    root.after(600000, goto_next_page)
    root.mainloop()

# Manipulation check test interface
def manipulation_check_interface():
    global current_time_2
    current_time_2 = get_current_time()

    # Define a set of questions
    questions = [
        {
            "question": "What is the primary goal of this study?", 
            "options": ["A. To measure typing speed", "B. To conduct a post-experiment survey", "C. To explore the effects of short video viewing on cognitive performance", "D. To provide monetary compensation"], 
            "correct_answer": "C"
         },
        {
            "question": "What is the focus of Stage 1 in the experiment?", 
            "options": ["A. Playing computer games", "B. Training with BCI devices", "C. Watching movies"], 
            "correct_answer": "B"
            },
        {
            "question": "What will be measured during the typing tasks in Stage 2 of the experiment?",
            "options": ["A. Participants' heart rate", "B. Participants' typing speed and accuracy", "C. Participants' ability to solve puzzles"], 
            "correct_answer": "B"
            }
    ]

    root = tk.Tk()
    root.title("Manipulation Check Test")
    root.geometry("600x600")
    current_question = 0
    countdown_seconds = 5
    countdown_label = tk.Label(root, text="", padx=10, pady=10)
    countdown_label.pack()

    # Countdown function
    def countdown():
        nonlocal countdown_seconds
        if countdown_seconds > 0:
            countdown_label.config(text=f"Countdown: {countdown_seconds} seconds")
            countdown_seconds -= 1
            root.after(1000, countdown)
        else:
            countdown_label.config(text="")
            goto_next_part()

    # Display question function
    def show_question():
        nonlocal current_question
        question_label.config(text=questions[current_question]["question"])
        for i in range(3):
            option_buttons[i].config(text=questions[current_question]["options"][i])
        current_question += 1

    # Check answer function
    def check_answer(selected_option):
        correct_answer = questions[current_question - 1]["correct_answer"]
        if selected_option == correct_answer:
            if current_question == len(questions):
                messagebox.showinfo("Congratulations", "Correct! Starting the formal experiment in 5 seconds...")
                countdown()
            else:
                show_question()
        else:
            messagebox.showerror("Incorrect", "The answer is incorrect. Please answer this question again.")
    question_label = tk.Label(root, text="", padx=10, pady=10)
    question_label.pack()
    option_buttons = []
    for i in range(3):
        button = tk.Button(root, text="", padx=10, pady=5, command=lambda i=i: check_answer(chr(65 + i)))
        button.pack()
        option_buttons.append(button)

    # Go to next part function
    def goto_next_part():
        root.destroy()
        typing_interface()
    show_question()
    check_answer()
    root.mainloop()


# Formal experiment first part typing interface
def typing_interface():
    global current_typing, typing_start_time, typing_reference_text, typing_timer, current_time_3
    current_time_3 = get_current_time()
    root = tk.Tk()
    root.title("Formal Experiment Part 1")
    root.geometry("800x600")
    typing_reference_text = "A platform before the Castle. Enter two Sentinels-first, Francisco, who paces up and down at his post; then Bernardo, who approaches him. Ber. Who's there? Fran. Nay, answer me. Stand and unfold yourself. Ber. Long live the King! Fran. Bernardo? Ber. He. Fran. You come most carefully upon your hour. Ber. 'Tis now struck twelve. Get thee to bed, Francisco. Fran. For this relief much thanks. 'Tis bitter cold, And I am sick at heart. Ber. Have you had quiet guard? Fran. Not a mouse stirring. Ber. Well, good night. If you do meet Horatio and Marcellus, The rivals of my watch, bid them make haste. Enter Horatio and Marcellus. Fran. I think I hear them. Stand, ho! Who is there? Hor. Friends to this ground. Mar. And liegemen to the Dane. Fran. Give you good night. Mar. farewell, honest soldier. Who hath reliev'd you? Fran. Bernardo hath my place. Give you good night. Exit. Mar. Holla, Bernardo! Ber. Say What, is Horatio there ? Hor. A piece of him. Ber. Welcome, Horatio. Welcome, good Marcellus. Mar. What, has this thing appear'd again tonight? Ber. I have seen nothing. Mar. Horatio says 'tis but our fantasy, And will not let belief take hold of him Touching this dreaded sight, twice seen of us. Therefore I have entreated him along, With us to watch the minutes of this night, That, if again this apparition come, He may approve our eyes and speak to it. Hor. Tush, tush, 'twill not appear. Ber. Sit down awhile, And let us once again assail your ears, That are so fortified against our story, What we two nights have seen. Hor. Well, sit we down, And let us hear Bernardo speak of this. Ber. Last night of all, When yond same star that's westward from the pole Had made his course t' illume that part of heaven Where now it burns, Marcellus and myself, The bell then beating one- Enter Ghost. Mar. Peace! break thee off! Look where it comes again! Ber. In the same figure, like the King that's dead. Mar. Thou art a scholar; speak to it, Horatio. Ber. Looks it not like the King? Mark it, Horatio. Hor. Most like. It harrows me with fear and wonder. Ber. It would be spoke to. Mar. Question it, Horatio. Hor. What art thou that usurp'st this time of night. Together with that fair and warlike form In which the majesty of buried Denmark Did sometimes march? By heaven I charge thee speak! Mar. It is offended. Ber. See, it stalks away! Hor. Stay! Speak, speak! I charge thee speak!Exit Ghost. Mar. 'Tis gone and will not answer. Ber. How now, Horatio? You tremble and look pale. Is not this something more than fantasy? What think you on't? Hor. Before my God, I might not this believe Without the sensible and true avouch Of mine own eyes. Mar. Is it not like the King? Hor. As thou art to thyself. Such was the very armour he had on When he th' ambitious Norway combated. So frown'd he once when, in an angry parle, He smote the sledded Polacks on the ice. 'Tis strange. Mar. Thus twice before, and jump at this dead hour, With martial stalk hath he gone by our watch. Hor. In what particular thought to work I know not; But, in the gross and scope of my opinion, This bodes some strange eruption to our state. Mar. Good now, sit down, and tell me he that knows, Why this same strict and most observant watch So nightly toils the subject of the land, And why such daily cast of brazen cannon And foreign mart for implements of war; Why such impress of shipwrights, whose sore task Does not divide the Sunday from the week. What might be toward, that this sweaty haste Doth make the night joint-labourer with the day? Who is't that can inform me? Hor. That can I. At least, the whisper goes so. Our last king, Whose image even but now appear'd to us, Was, as you know, by Fortinbras of Norway, Thereto prick'd on by a most emulate pride, Dar'd to the combat; in which our valiant Hamlet (For so this side of our known world esteem'd him) Did slay this Fortinbras; who, by a seal'd compact, Well ratified by law and heraldry, Did forfeit, with his life, all those his lands Which he stood seiz'd of, to the conqueror; Against the which a moiety competent Was gaged by our king; which had return'd To the inheritance of Fortinbras, Had he been vanquisher, as, by the same cov'nant And carriage of the article design'd, His fell to Hamlet. Now, sir, young Fortinbras, Of unimproved mettle hot and full, Hath in the skirts ofNorway, here and there, Shark'd up a list of lawless resolutes, For food and diet, to some enterprise That hath a stomach in't; which is no other, As it doth well appear unto our state, But to recover of us, by strong hand And terms compulsatory, those foresaid lands So by his father lost; and this, I take it, Is the main motive of our preparations, The source of this our watch, and the chief head Of this post-haste and romage in the land. Ber. I think it be no other but e'en so. Well may it sort that this portentous figure Comes armed through our watch, so like the King That was and is the question of these wars. Hor. A mote it is to trouble the mind's eye. In the most high and palmy state of Rome, A little ere the mightiest Julius fell, The graves stood tenantless, and the sheeted dead Did squeak and gibber in the Roman streets; As stars with trains of fire, and dews of blood, Disasters in the sun; and the moist star Upon whose influence Neptune's empire stands Was sick almost to doomsday with eclipse. And even the like precurse of fierce events, As harbingers preceding still the fates And prologue to the omen coming on, Have heaven and earth together demonstrated Unto our climature and countrymen. Enter Ghost again. But soft! behold! Lo, where it comes again! I'll cross it, though it blast me.- Stay illusion!Spreads his arms. If thou hast any sound, or use of voice, Speak to me. If there be any good thing to be done, That may to thee do ease, and, race to me, Speak to me. If thou art privy to thy country's fate, Which happily foreknowing may avoid, O, speak! Or if thou hast uphoarded in thy life Extorted treasure in the womb of earth (For which, they say, you spirits oft walk in death),The cock crows. Speak of it! Stay, and speak!- Stop it, Marcellus! Mar. Shall I strike at it with my partisan? Hor. Do, if it will not stand. Ber. 'Tis here! Hor. 'Tis here! Mar. 'Tis gone!Exit Ghost. We do it wrong, being so majestical, To offer it the show of violence; For it is as the air, invulnerable, And our vain blows malicious mockery. Ber. It was about to speak, when the cock crew. Hor. And then it started, like a guilty thing Upon a fearful summons. I have heard The cock, that is the trumpet to the morn, Doth with his lofty and shrill-sounding throat Awake the god of day; and at his warning, Whether in sea or fire, in earth or air, Th' extravagant and erring spirit hies To his confine; and of the truth herein This present object made probation. Mar. It faded on the crowing of the cock. Some say that ever, 'gainst that season comes Wherein our Saviour's birth is celebrated, The bird of dawning singeth all night long; And then, they say, no spirit dare stir abroad, The nights are wholesome, then no planets strike, No fairy takes, nor witch hath power to charm, So hallow'd and so gracious is the time. Hor. So have I heard and do in part believe it. But look, the morn, in russet mantle clad, Walks o'er the dew of yon high eastward hill. Break we our watch up; and by my advice Let us impart what we have seen to-night Unto young Hamlet; for, upon my life, This spirit, dumb to us, will speak to him. Do you consent we shall acquaint him with it, As needful in our loves, fitting our duty? Let's do't, I pray; and I this morning know Where we shall find him most conveniently. Exeunt. A room of state in the Castle. Flourish. Enter Claudius, King of Denmark, Gertrude the Queen, Hamlet, Polonius, Laertes and his sister Ophelia, Voltemand, Cornelius, Lords Attendant. King. Though yet of Hamlet our dear brother's death The memory be green, and that it us befitted To bear our hearts in grief, and our whole kingdom To be contracted in one brow of woe, Yet so far hath discretion fought with nature That we with wisest sorrow think on him Together with remembrance of ourselves. Therefore our sometime sister, now our queen, Th' imperial jointress to this warlike state, Have we, as 'twere with a defeated joy, With an auspicious, and a dropping eye, With mirth in funeral, and with dirge in marriage, In equal scale weighing delight and dole, Taken to wife; nor have we herein barr'd Your better wisdoms, which have freely gone With this affair along. For all, our thanks. Now follows, that you know, young Fortinbras, Holding a weak supposal of our worth, Or thinking by our late dear brother's death Our state to be disjoint and out of frame, Colleagued with this dream of his advantage, He hath not fail'd to pester us with message Importing the surrender of those lands Lost by his father, with all bands of law, To our most valiant brother. So much for him. Now for ourself and for this time of meeting. Thus much the business is: we have here writ To Norway, uncle of young Fortinbras, Who, impotent and bedrid, scarcely hears Of this his nephew's purpose, to suppress His further gait herein, in that the levies, The lists, and full proportions are all made Out of his subject; and we here dispatch You, good Cornelius, and you, Voltemand, For bearers of this greeting to old Norway, Giving to you no further personal power To business with the King, more than the scope Of these dilated articles allow.Gives a paper. Farewell, and let your haste commend your duty. Cor., Volt. In that, and all things, will we show our duty. King. We doubt it nothing. Heartily farewell.Exeunt Voltemand and Cornelius. And now, Laertes, what's the news with you? You told us of some suit. What is't, Laertes? You cannot speak of reason to the Dane And lose your voice. What wouldst thou beg, Laertes, That shall not be my offer, not thy asking? The head is not more native to the heart, The hand more instrumental to the mouth, Than is the throne of Denmark to thy father. What wouldst thou have, Laertes? Laer. My dread lord, Your leave and favour to return to France; From whence though willingly I came to Denmark To show my duty in your coronation, Yet now I must confess, that duty done, My thoughts and wishes bend again toward France And bow them to your gracious leave and pardon. King. Have you your father's leave? What says Polonius? Pol. He hath, my lord, wrung from me my slow leave By laboursome petition, and at last Upon his will I seal'd my hard consent. I do beseech you give him leave to go. King. Take thy fair hour, Laertes. Time be thine, And thy best graces spend it at thy will! But now, my cousin Hamlet, and my son- Ham. [aside] A little more than kin, and less than kind! King. How is it that the clouds still hang on you? Ham. Not so, my lord. I am too much i' th' sun. Queen. Good Hamlet, cast thy nighted colour off, And let thine eye look like a friend on Denmark. Do not for ever with thy vailed lids Seek for thy noble father in the dust. Thou know'st 'tis common. All that lives must die, Passing through nature to eternity. Ham. Ay, madam, it is common. Queen. If it be, Why seems it so particular with thee? Ham. Seems, madam, Nay, it is. I know not 'seems.' 'Tis not alone my inky cloak, good mother, Nor customary suits of solemn black, Nor windy suspiration of forc'd breath, No, nor the fruitful river in the eye, Nor the dejected havior of the visage, Together with all forms, moods, shapes of grief, 'That can denote me truly. "
    scrollbar = tk.Scrollbar(root)
    scrollbar.pack(side=tk.RIGHT, fill=tk.Y)

    data_textbox = tk.Text(root, height=30, width=50, yscrollcommand=scrollbar.set)
    data_textbox.pack(side=tk.RIGHT, padx=20)

    scrollbar.config(command=data_textbox.yview)

    data_textbox.insert(tk.END, typing_reference_text)

    typing_label = tk.Label(root, text="Please press the start button and type the words:")
    typing_label.pack()

    # Create a disabled typing textbox initially
    typing_textbox = tk.Text(root, height=30, width=50, state=tk.DISABLED)
    typing_textbox.pack()

    #change of showing text
    countdown_label = tk.Label(root, text="You have 15min to type")
    countdown_label.pack()

    typing_start_time = None
    typing_timer = None
    typing_speed = None
    typing_accuracy = None

    # Start typing button click event handler
    def start_typing():
        global typing_timer, typing_start_time
        start_time = time.time()
        typing_start_time = start_time
        countdown()
        start_button.config(state=tk.DISABLED)
        end_button.config(state=tk.NORMAL)

        # Enable the typing textbox
        typing_textbox.config(state=tk.NORMAL)
    start_button = tk.Button(root, text="Start Typing", command=start_typing)
    start_button.pack()

    # End typing button click event handler
    def end_typing():
        typing_textbox.config(state=tk.DISABLED)
        update_typing_text()
        end_button.config(state=tk.DISABLED)
        goto_button.config(state=tk.NORMAL)
    end_button = tk.Button(root, text="End Typing", command=end_typing, state=tk.DISABLED)
    end_button.pack()

    # Update typing data function
    def update_typing_text():
        global typing_speed, typing_accuracy, typing_timer, test2_speed, test2_accuracy
        typed_text = typing_textbox.get("1.0", tk.END).strip()
        typed_words = typed_text.split()
        reference_words = typing_reference_text.split()
        correct_words = [w1 for w1, w2 in zip(typed_words, reference_words) if w1 == w2]
        accuracy = len(correct_words) / len(typed_words) * 100
        typing_speed = len(correct_words) / (time.time() - typing_start_time) * 60
        typing_accuracy = accuracy
        test2_speed = typing_speed
        test2_accuracy = accuracy

    # Countdown function
    def countdown():
        remaining_time = 15 * 60 - int(time.time() - typing_start_time)
        if remaining_time <= 0:
            end_typing()
        else:
            minutes = remaining_time // 60
            seconds = remaining_time % 60
            #countdown_label.config(text=f"Countdown: {minutes:02}:{seconds:02}")
            root.after(1000, countdown)

    # Go to next part function
    def goto_next_part():
        root.destroy()
        countdown_page()

    goto_button = tk.Button(root, text="Goto Next Part", command=goto_next_part, state=tk.DISABLED)
    goto_button.pack()

    # Disable copy-paste function
    def disable_copy_paste(event):
        if (event.state & 4) or (event.state & 1):  # Check for Control key (Ctrl or Command)
            if event.keysym == 'c' or event.keysym == 'v':
                return "break"  # Prevents copy and paste

    typing_textbox.bind("<Control-c>", disable_copy_paste)  # Disable Ctrl+C (copy)
    typing_textbox.bind("<Control-v>", disable_copy_paste)  # Disable Ctrl+V (paste)

    root.mainloop()

# 10-minute countdown page
def countdown_page():
    def countdown(minutes):
        seconds = minutes * 60

        def update_time():
            nonlocal seconds
            if seconds > 0:
                minutes = seconds // 60
                seconds_remaining = seconds % 60
                time_label.config(text=f"{minutes:02d}:{seconds_remaining:02d}")
                seconds -= 1
                time_label.after(1000, update_time)
            else:
                root.destroy()
                typing_interface_part2()

        root = tk.Tk()
        root.title("Rest for 10 Minutes")
        root.geometry("600x600")

        time_label = tk.Label(root, font=("Arial", 24))
        time_label.pack(pady=20)

        skip_button = tk.Button(root, text="Skip Rest Period", command=lambda: skip_countdown(root))
        skip_button.pack()

        update_time()
        root.mainloop()

    def skip_countdown(root):
        root.destroy()
        typing_interface_part2()

    countdown(10)

# Formal experiment second part typing interface
def typing_interface_part2():
    global current_typing, typing_start_time, typing_reference_text, typing_timer, current_time_4
    current_time_4 = get_current_time()
    root = tk.Tk()
    root.title("Formal Experiment Part 2")
    root.geometry("800x600")
    typing_reference_text = "Did slay this Fortinbras; who, by a seal'd compact, Well ratified by law and heraldry, Did forfeit, with his life, all those his lands Which he stood seiz'd of, to the conqueror; Against the which a moiety competent Was gaged by our king; which had return'd To the inheritance of Fortinbras, Had he been vanquisher, as, by the same cov'nant And carriage of the article design'd, His fell to Hamlet. Now, sir, young Fortinbras, Of unimproved mettle hot and full, Hath in the skirts ofNorway, here and there, Shark'd up a list of lawless resolutes, For food and diet, to some enterprise That hath a stomach in't; which is no other, As it doth well appear unto our state, But to recover of us, by strong hand And terms compulsatory, those foresaid lands So by his father lost; and this, I take it, Is the main motive of our preparations, The source of this our watch, and the chief head Of this post-haste and romage in the land. Ber. I think it be no other but e'en so. Well may it sort that this portentous figure Comes armed through our watch, so like the King That was and is the question of these wars. Hor. A mote it is to trouble the mind's eye. In the most high and palmy state of Rome, A little ere the mightiest Julius fell, The graves stood tenantless, and the sheeted dead Did squeak and gibber in the Roman streets; As stars with trains of fire, and dews of blood, Disasters in the sun; and the moist star Upon whose influence Neptune's empire stands Was sick almost to doomsday with eclipse. And even the like precurse of fierce events, As harbingers preceding still the fates And prologue to the omen coming on, Have heaven and earth together demonstrated Unto our climature and countrymen. Enter Ghost again. But soft! behold! Lo, where it comes again! I'll cross it, though it blast me.- Stay illusion!Spreads his arms. If thou hast any sound, or use of voice, Speak to me. If there be any good thing to be done, That may to thee do ease, and, race to me, Speak to me. If thou art privy to thy country's fate, Which happily foreknowing may avoid, O, speak! Or if thou hast uphoarded in thy life Extorted treasure in the womb of earth (For which, they say, you spirits oft walk in death),The cock crows. Speak of it! Stay, and speak!- Stop it, Marcellus! Mar. Shall I strike at it with my partisan? Hor. Do, if it will not stand. Ber. 'Tis here! Hor. 'Tis here! Mar. 'Tis gone!Exit Ghost. We do it wrong, being so majestical, To offer it the show of violence; For it is as the air, invulnerable, And our vain blows malicious mockery. Ber. It was about to speak, when the cock crew. Hor. And then it started, like a guilty thing Upon a fearful summons. I have heard The cock, that is the trumpet to the morn, Doth with his lofty and shrill-sounding throat Awake the god of day; and at his warning, Whether in sea or fire, in earth or air, Th' extravagant and erring spirit hies To his confine; and of the truth herein This present object made probation. Mar. It faded on the crowing of the cock. Some say that ever, 'gainst that season comes Wherein our Saviour's birth is celebrated, The bird of dawning singeth all night long; And then, they say, no spirit dare stir abroad, The nights are wholesome, then no planets strike, No fairy takes, nor witch hath power to charm, So hallow'd and so gracious is the time. Hor. So have I heard and do in part believe it. But look, the morn, in russet mantle clad, Walks o'er the dew of yon high eastward hill. Break we our watch up; and by my advice Let us impart what we have seen to-night Unto young Hamlet; for, upon my life, This spirit, dumb to us, will speak to him. Do you consent we shall acquaint him with it, As needful in our loves, fitting our duty? Let's do't, I pray; and I this morning know Where we shall find him most conveniently. Exeunt. A room of state in the Castle. Flourish. Enter Claudius, King of Denmark, Gertrude the Queen, Hamlet, Polonius, Laertes and his sister Ophelia, Voltemand, Cornelius, Lords Attendant. King. Though yet of Hamlet our dear brother's death The memory be green, and that it us befitted To bear our hearts in grief, and our whole kingdom To be contracted in one brow of woe, Yet so far hath discretion fought with nature That we with wisest sorrow think on him Together with remembrance of ourselves. Therefore our sometime sister, now our queen, Th' imperial jointress to this warlike state, Have we, as 'twere with a defeated joy, With an auspicious, and a dropping eye, With mirth in funeral, and with dirge in marriage, In equal scale weighing delight and dole, Taken to wife; nor have we herein barr'd Your better wisdoms, which have freely gone With this affair along. For all, our thanks. Now follows, that you know, young Fortinbras, Holding a weak supposal of our worth, Or thinking by our late dear brother's death Our state to be disjoint and out of frame, Colleagued with this dream of his advantage, He hath not fail'd to pester us with message Importing the surrender of those lands Lost by his father, with all bands of law, To our most valiant brother. So much for him. Now for ourself and for this time of meeting. Thus much the business is: we have here writ To Norway, uncle of young Fortinbras, Who, impotent and bedrid, scarcely hears Of this his nephew's purpose, to suppress His further gait herein, in that the levies, The lists, and full proportions are all made Out of his subject; and we here dispatch You, good Cornelius, and you, Voltemand, For bearers of this greeting to old Norway, Giving to you no further personal power To business with the King, more than the scope Of these dilated articles allow.Gives a paper. Farewell, and let your haste commend your duty. Cor., Volt. In that, and all things, will we show our duty. King. We doubt it nothing. Heartily farewell.Exeunt Voltemand and Cornelius. And now, Laertes, what's the news with you? You told us of some suit. What is't, Laertes? You cannot speak of reason to the Dane And lose your voice. What wouldst thou beg, Laertes, That shall not be my offer, not thy asking? The head is not more native to the heart, The hand more instrumental to the mouth, Than is the throne of Denmark to thy father. What wouldst thou have, Laertes? Laer. My dread lord, Your leave and favour to return to France; From whence though willingly I came to Denmark To show my duty in your coronation, Yet now I must confess, that duty done, My thoughts and wishes bend again toward France And bow them to your gracious leave and pardon. King. Have you your father's leave? What says Polonius? Pol. He hath, my lord, wrung from me my slow leave By laboursome petition, and at last Upon his will I seal'd my hard consent. I do beseech you give him leave to go. King. Take thy fair hour, Laertes. Time be thine, And thy best graces spend it at thy will! But now, my cousin Hamlet, and my son- Ham. [aside] A little more than kin, and less than kind! King. How is it that the clouds still hang on you? Ham. Not so, my lord. I am too much i' th' sun. Queen. Good Hamlet, cast thy nighted colour off, And let thine eye look like a friend on Denmark. Do not for ever with thy vailed lids Seek for thy noble father in the dust. Thou know'st 'tis common. All that lives must die, Passing through nature to eternity. Ham. Ay, madam, it is common. Queen. If it be, Why seems it so particular with thee? Ham. Seems, madam, Nay, it is. I know not 'seems.' 'Tis not alone my inky cloak, good mother, Nor customary suits of solemn black, Nor windy suspiration of forc'd breath, No, nor the fruitful river in the eye, Nor the dejected havior of the visage, Together with all forms, moods, shapes of grief, 'That can denote me truly. These indeed seem, For they are actions that a man might play; But I have that within which passeth show- These but the trappings and the suits of woe. King. 'Tis sweet and commendable in your nature, Hamlet, To give these mourning duties to your father; But you must know, your father lost a father; That father lost, lost his, and the survivor bound In filial obligation for some term To do obsequious sorrow. But to persever In obstinate condolement is a course Of impious stubbornness. 'Tis unmanly grief; It shows a will most incorrect to heaven, A heart unfortified, a mind impatient, An understanding simple and unschool'd; For what we know must be, and is as common As any the most vulgar thing to sense, Why should we in our peevish opposition Take it to heart? Fie! 'tis a fault to heaven, A fault against the dead, a fault to nature, To reason most absurd, whose common theme Is death of fathers, and who still hath cried, From the first corse till he that died to-day, 'This must be so.' We pray you throw to earth This unprevailing woe, and think of us As of a father; for let the world take note You are the most immediate to our throne, And with no less nobility of love Than that which dearest father bears his son Do I impart toward you. For your intent In going back to school in Wittenberg, It is most retrograde to our desire; And we beseech you, bend you to remain Here in the cheer and comfort of our eye, Our chiefest courtier, cousin, and our son. Queen. Let not thy mother lose her prayers, Hamlet. I pray thee stay with us, go not to Wittenberg. Ham. I shall in all my best obey you, madam. King. Why, 'tis a loving and a fair reply. Be as ourself in Denmark. Madam, come. This gentle and unforc'd accord of Hamlet Sits smiling to my heart; in grace whereof, No jocund health that Denmark drinks to-day But the great cannon to the clouds shall tell, And the King's rouse the heaven shall bruit again, Respeaking earthly thunder. Come away. Flourish. Exeunt all but Hamlet. Ham. O that this too too solid flesh would melt, Thaw, and resolve itself into a dew! Or that the Everlasting had not fix'd His canon 'gainst self-slaughter! O God! God! How weary, stale, flat, and unprofitable Seem to me all the uses of this world! Fie on't! ah, fie! 'Tis an unweeded garden That grows to seed; things rank and gross in nature Possess it merely. That it should come to this! But two months dead! Nay, not so much, not two. So excellent a king, that was to this Hyperion to a satyr; so loving to my mother That he might not beteem the winds of heaven Visit her face too roughly. Heaven and earth! Must I remember? Why, she would hang on him As if increase of appetite had grown By what it fed on; and yet, within a month- Let me not think on't! Frailty, thy name is woman!- A little month, or ere those shoes were old With which she followed my poor father's body Like Niobe, all tears- why she, even she (O God! a beast that wants discourse of reason Would have mourn'd longer) married with my uncle; My father's brother, but no more like my father Than I to Hercules. Within a month, Ere yet the salt of most unrighteous tears Had left the flushing in her galled eyes, She married. O, most wicked speed, to post With such dexterity to incestuous sheets! It is not, nor it cannot come to good. But break my heart, for I must hold my tongue! Enter Horatio, Marcellus, and Bernardo. Hor. Hail to your lordship! Ham. I am glad to see you well. Horatio!- or I do forget myself. Hor. The same, my lord, and your poor servant ever. Ham. Sir, my good friend- I'll change that name with you. And what make you from Wittenberg, Horatio? Marcellus? Mar. My good lord! Ham. I am very glad to see you.- [To Bernardo] Good even, sir.- But what, in faith, make you from Wittenberg? Hor. A truant disposition, good my lord. Ham. I would not hear your enemy say so, Nor shall you do my ear that violence To make it truster of your own report Against yourself. I know you are no truant. But what is your affair in Elsinore? We'll teach you to drink deep ere you depart. Hor. My lord, I came to see your father's funeral. Ham. I prithee do not mock me, fellow student. I think it was to see my mother's wedding. Hor. Indeed, my lord, it followed hard upon. Ham. Thrift, thrift, Horatio! The funeral bak'd meats Did coldly furnish forth the marriage tables. Would I had met my dearest foe in heaven Or ever I had seen that day, Horatio! My father- methinks I see my father. Hor. O, where, my lord? Ham. In my mind's eye, Horatio. Hor. I saw him once. He was a goodly king. Ham. He was a man, take him for all in all. I shall not look upon his like again. Hor. My lord, I think I saw him yesternight. Ham. Saw? who? Hor. My lord, the King your father. Ham. The King my father? Hor. Season your admiration for a while With an attent ear, till I may deliver Upon the witness of these gentlemen, This marvel to you. Ham. For God's love let me hear! Hor. Two nights together had these gentlemen (Marcellus and Bernardo) on their watch In the dead vast and middle of the night Been thus encount'red. A figure like your father, Armed at point exactly, cap-a-pe, Appears before them and with solemn march Goes slow and stately by them. Thrice he walk'd By their oppress'd and fear-surprised eyes, Within his truncheon's length; whilst they distill'd Almost to jelly with the act of fear, Stand dumb and speak not to him. This to me In dreadful secrecy impart they did, And I with them the third night kept the watch; Where, as they had deliver'd, both in time, Form of the thing, each word made true and good, The apparition comes. I knew your father. These hands are not more like. Ham. But where was this? Mar. My lord, upon the platform where we watch'd. Ham. Did you not speak to it? Hor. My lord, I did; But answer made it none. Yet once methought It lifted up it head and did address Itself to motion, like as it would speak; But even then the morning cock crew loud, And at the sound it shrunk in haste away And vanish'd from our sight. Ham. 'Tis very strange. Hor. As I do live, my honour'd lord, 'tis true; And we did think it writ down in our duty To let you know of it. Ham. Indeed, indeed, sirs. But this troubles me. Hold you the watch to-night? Both [Mar. and Ber. We do, my lord. Ham. Arm'd, say you? Both. Arm'd, my lord. Ham. From top to toe? Both. My lord, from head to foot. Ham. Then saw you not his face? Hor. O, yes, my lord! He wore his beaver up. Ham. What, look'd he frowningly. Hor. A countenance more in sorrow than in anger. Ham. Pale or red? Hor. Nay, very pale. Ham. And fix'd his eyes upon you? Hor. Most constantly. Ham. I would I had been there. Hor. It would have much amaz'd you. Ham. Very like, very like. Stay'd it long? Hor. While one with moderate haste might tell a hundred. Both. Longer, longer. Hor. Not when I saw't. Ham. His beard was grizzled- no? Hor. It was, as I have seen it in his life, A sable silver'd. Ham. I will watch to-night. Perchance 'twill walk again. Hor. I warr'nt it will. Ham. If it assume my noble father's person, I'll speak to it, though hell itself should gape And bid me hold my peace. I pray you all, If you have hitherto conceal'd this sight, Let it be tenable in your silence still; And whatsoever else shall hap to-night, Give it an understanding but no tongue. I will requite your loves. So, fare you well. Upon the platform, 'twixt eleven and twelve, I'll visit you. All. Our duty to your honour. Ham. Your loves, as mine to you. Farewell. Exeunt. My father's spirit- in arms? All is not well. I doubt some foul play. Would the night were come! Till then sit still, my soul. Foul deeds will rise, Though all the earth o'erwhelm them, to men's eyes. Exit."

    scrollbar = tk.Scrollbar(root)
    scrollbar.pack(side=tk.RIGHT, fill=tk.Y)

    data_textbox = tk.Text(root, height=30, width=50, yscrollcommand=scrollbar.set)
    data_textbox.pack(side=tk.RIGHT, padx=20)

    scrollbar.config(command=data_textbox.yview)
    data_textbox.insert(tk.END, typing_reference_text)

    typing_label = tk.Label(root, text="Please press the start button and type the words:")
    typing_label.pack()
    typing_textbox = tk.Text(root, height=30, width=50, state=tk.DISABLED)
    typing_textbox.pack()

    countdown_label = tk.Label(root, text="You have 15min to type")
    countdown_label.pack()

    typing_start_time = None
    typing_timer = None
    typing_speed = None
    typing_accuracy = None

    # Start typing button click event handler
    def start_typing():
        global typing_timer, typing_start_time
        start_time = time.time()
        typing_start_time = start_time
        countdown()
        start_button.config(state=tk.DISABLED)
        end_button.config(state=tk.NORMAL)
        typing_textbox.config(state=tk.NORMAL)
    start_button = tk.Button(root, text="Start Typing", command=start_typing)
    start_button.pack()

    # End typing button click event handler
    def end_typing():
        typing_textbox.config(state=tk.DISABLED)
        update_typing_text()
        end_button.config(state=tk.DISABLED)
        goto_button.config(state=tk.NORMAL)
    end_button = tk.Button(root, text="End Typing", command=end_typing, state=tk.DISABLED)
    end_button.pack()

    # Update typing data function
    def update_typing_text():
        global typing_speed, typing_accuracy, typing_timer, test3_speed, test3_accuracy
        typed_text = typing_textbox.get("1.0", tk.END).strip()
        typed_words = typed_text.split()
        reference_words = typing_reference_text.split()
        correct_words = [w1 for w1, w2 in zip(typed_words, reference_words) if w1 == w2]
        accuracy = len(correct_words) / len(typed_words) * 100
        typing_speed = len(correct_words) / (time.time() - typing_start_time) * 60
        typing_accuracy = accuracy
        test3_speed = typing_speed
        test3_accuracy = accuracy

    # Countdown function
    def countdown():
        remaining_time = 15 * 60 - int(time.time() - typing_start_time)
        if remaining_time <= 0:
            end_typing()
        else:
            minutes = remaining_time // 60
            seconds = remaining_time % 60
            #countdown_label.config(text=f"Countdown: {minutes:02}:{seconds:02}")
            root.after(1000, countdown)

    # Go to next part function
    def goto_next_part():
        root.destroy()
        save_data()
        thank_you_interface()

    goto_button = tk.Button(root, text="Goto Next Part", command=goto_next_part, state=tk.DISABLED)
    goto_button.pack()

    # Disable copy-paste function
    def disable_copy_paste(event):
        if (event.state & 4) or (event.state & 1):  # Check for Control key (Ctrl or Command)
            if event.keysym == 'c' or event.keysym == 'v':
                return "break"  # Prevents copy and paste

    typing_textbox.bind("<Control-c>", disable_copy_paste)  # Disable Ctrl+C (copy)
    typing_textbox.bind("<Control-v>", disable_copy_paste)  # Disable Ctrl+V (paste)

    root.mainloop()

# Thank you interface
def thank_you_interface():
    root = tk.Tk()
    root.title("Thank You!")
    root.geometry("600x600")
    label = tk.Label(root, text="Thank you for participating in the experiment!")
    label.pack()

    def finish_experiment():
        root.destroy()
        save_data()
        exit()

    finish_button = tk.Button(root, text="Finish Experiment", command=finish_experiment)
    finish_button.pack()

    root.mainloop()

# Save data to a CSV file
def save_data():
    global participant_id, test1_score, test2_speed, test2_accuracy, test3_speed, test3_accuracy, typing_data
    global current_time_1, current_time_2, current_time_3, current_time_4
    
    # Specify the directory where you want to save the CSV file
    directory = r"C:\Users\S1mple\Desktop\SW"  # Replace with the actual directory path

    # Create the directory if it doesn't exist
    if not os.path.exists(directory):
        os.makedirs(directory)
    
    # Save data to a CSV file
    filename = os.path.join(directory,f"typing_data_{participant_id}.csv")
    with open(filename, mode="w", newline="") as file:
        writer = csv.writer(file)
        writer.writerow(["Participant ID", "Part 1 Typng Speed", "Part 1 Typing Accuracy", "Part 2 Typng Speed", "Part 2 Typng Accuracy", "Start time", "Part 1 Start Time", "Part 2 Start Time"])
        writer.writerow([participant_id, test2_speed, test2_accuracy, test3_speed, test3_accuracy, current_time_1, current_time_3, current_time_4])
        writer.writerow(["","WPM(word per minute)","","WPM","","","",""])
    
# Main function
def main():
    prepare_interface()

if __name__ == "__main__":
    main()


