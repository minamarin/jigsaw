
from flask import Flask, render_template, Response, request, jsonify
from flask import Flask, render_template, request, redirect, url_for


app = Flask(__name__)

#data

steps = {
    "1": {
        "step_id": "1",
        "title": "Step #1: Choosing Difficulty", 
        "media":"https://i.ibb.co/d287rY6/step1.png", 
        "text": "For those new to jigsaw puzzles, starting with a 250-500-piece puzzle is recommended. If you have some familiarity or are seeking a greater challenge, consider trying a 1000-piece puzzle.",
        "next": "2"
    },
    "2": {
        "step_id": "2",
        "title": "Step #2: Choosing Workspace", 
        "media":"https://i.ibb.co/5TqBNPp/step2.png", 
        "text": "Simulator Setup: If you are using digital workspace e.g. jigsawpuzzles.io, choose a background color that contrasts well with your puzzle pieces for better visibility. I chose gray background, because my puzzle image as seen on the right is colorful and does not include darker colors. Physical Space Setup: Ensure your workspace, such as a dining table, is large enough for the puzzle size. We recommend using a puzzle mat for its portability and to safeguard your progress.",
        "next": "3",
    }, 
    "3": {
        "step_id": "3",
        "title": "Step #3: Flip all the pieces upwards", 
        "media":"https://i.ibb.co/wh0yFFX/step3.png", 
        "text": "Jigsaw puzzle pieces come in varying shapes with “ins” and “outs.” Sometimes, it might seem like a perfect match, but they don't belong together. With practice, you'll improve at spotting these differences. Begin by flipping all pieces upwards to easily identify their shapes and colors.",
        "next": "4",
    }, 
    
    "4": {
        "step_id": "4",
        "title": "Step #4: Finding Corner Pieces", 
        "media":"https://i.ibb.co/RDhxMXH/step4.gif", 
        "text": "Corner pieces have two unique features: two “ins” and “outs”, and two straight edges. These pieces are your puzzle's foundation; start by finding all four corners. Position them according to the puzzle's final image for guidance.",
        "next": "5",
    }, 

    "5": {
        "step_id": "5",
        "title": "Step #5: Finding Edge Pieces", 
        "media":"https://i.ibb.co/jGpQntH/step5-edges.gif", 
        "text": "After corner pieces, the next goal is to find all the edge pieces. Edge pieces have one “out” side and are crucial for framing your puzzle. Assembling the border gives a clear boundary and structure to work within. Use the puzzle's final image as a reference to align these pieces accurately.",
        "next": "6",
    }, 

    "6": {
        "step_id": "6",
        "title": "Step #6: Sort by Colors & Special Pieces", 
        "media":"https://i.ibb.co/YkfKHPz/Screen-Recording-2024-04-09-at-20-49-53.gif", 
        "text": "Begin sorting pieces by color to group similar sections together. Identify and separate special pieces that stand out due to unique colors, patterns, or text. These are often key to solving specific parts of the puzzle. Also, look out for 'whimsies' - pieces shaped unusually, like animals or objects, which can be placed more easily once their general location is determined.",
        "next": "7",
    }, 
    
    "7": {
        "step_id": "7",
        "title": "Step #7: Completing the Puzzle", 
        "media":"https://i.ibb.co/MRHDqqB/Screen-Recording-2024-04-09-at-20-49-53-1.gif", 
        "text": "Focus on completing small sections or specific images within the puzzle first, using your sorted groups. If you encounter difficulty with a particular area, switch to another section. This can prevent frustration and keep the process enjoyable. Some puzzles allow for sorting by shape—this can be particularly helpful for areas with uniform color. Remember: patience is key. Take breaks if needed, and don’t rush. Puzzling is a marathon, not a sprint.",
        "next": "",
    } 
}

video_tutorial = {
        "title": "Video Tutorial for All Steps", 
        "media":"", 
        "next": "",
}

practice = {
        "title": "Practice!", 
        "media":"https://im-a-puzzle.com/share/55794569b3b9be3?embed=true&showAds=false&showNav=false&showSolve=false", 
        "next": "",
}

quiz = {
    "1": {
        "quiz_id": "1",
        "question": "Q1. What did you do first upon starting the puzzle?",
        "media": "",
        "choices": [
            {"id": "choice_1", "text": "A) Sorted pieces by color"},
            {"id": "choice_2", "text": "B) Looked for corner pieces"},
            {"id": "choice_3", "text": "C) Assembled edge pieces"}
        ],
        "answer": "choice_2",
        "next": "2"
    },

    "2": {
        "quiz_id": "2",
        "question": "Q2. Which color group did not exist in the puzzle?",
        "media": "",
        "choices": [
            {"id": "choice_1", "text": "A) Red"},
            {"id": "choice_2", "text": "B) Green"},
            {"id": "choice_3", "text": "C) Brown"},
            {"id": "choice_4", "text": "D) Blue"}
        ],
        "answer": "choice_1",
        "next": "3"
    },

    "3": {
        "quiz_id": "3",
        "question": "Q3. How many edges does a corner piece have?",
        "media": "",
        "choices": [
            {"id": "choice_1", "text": "A) None"},
            {"id": "choice_2", "text": "B) 1"},
            {"id": "choice_3", "text": "C) 2"},
            {"id": "choice_4", "text": "D) 3"}
        ],
        "answer": "choice_3",
        "next": "4"
    },

    "4": {
        "quiz_id": "4",
        "question": "Q4. Where do the pieces shown in the image belong? (in order)",
        "media": "",
        "choices": [
            {"id": "choice_1", "text": "A) The left edge, the bottom edge"},
            {"id": "choice_2", "text": "B) The bottom right corner, the top edge"},
            {"id": "choice_3", "text": "C) The top left corner, the bottom edge"}
        ],
        "answer": "choice_3",
        "next": ""
    }
}

#routes 
@app.route('/')
def default():
    return render_template('home.html')

@app.route('/home')
def home():
    return render_template('home.html')

@app.route('/puzzletips/<step_id>')
def puzzletips(step_id):
    step = steps.get(step_id)
    if not step:
        return "Step not found", 404
    return render_template('puzzletips.html', step=step)

@app.route('/videotutorial')
def video_tutorial_page():
    return render_template('videotutorial.html')

@app.route('/quiz/<quiz_id>')
def quiz_page(quiz_id):
    quiz_question = quiz.get(quiz_id)
    if not quiz_question:
        return "Quiz not found", 404
    return render_template('quiz.html', quiz=quiz_question)

@app.route('/submit_quiz/<quiz_id>', methods=['POST'])
def submit_quiz(quiz_id):
    quiz_question = quiz.get(quiz_id)
    if not quiz_question:
        return "Quiz not found", 404

    selected_choice = request.form.get('answer')
    if not selected_choice:
        return "No answer selected", 400

    if selected_choice == quiz_question['answer']:
        # Redirect to next quiz if answer is correct
        next_quiz_id = quiz_question['next']
        if next_quiz_id:
            return redirect(url_for('quiz_page', quiz_id=next_quiz_id))
        else:
            # No more quizzes, redirect to a completion page or something similar
            return redirect(url_for('quiz_completion'))
    else:
        # Reload the current quiz if answer is incorrect
        return redirect(url_for('quiz_page', quiz_id=quiz_id))


if __name__ == '__main__':
    app.run(debug=True)