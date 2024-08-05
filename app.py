from flask import Flask, render_template, request

app = Flask(__name__)

def estimate_finger_lengths(palm_length, palm_width):
    thumb_ratio = 0.5
    index_finger_ratio = 0.75
    middle_finger_ratio = 0.85
    ring_finger_ratio = 0.8
    little_finger_ratio = 0.65

    thumb_length = palm_length * thumb_ratio
    index_finger_length = palm_length * index_finger_ratio
    middle_finger_length = palm_length * middle_finger_ratio
    ring_finger_length = palm_length * ring_finger_ratio
    little_finger_length = palm_length * little_finger_ratio

    return {
        "Thumb": round(thumb_length, 2),
        "Index Finger": round(index_finger_length, 2),
        "Middle Finger": round(middle_finger_length, 2),
        "Ring Finger": round(ring_finger_length, 2),
        "Little Finger": round(little_finger_length, 2)
    }

@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        palm_length = float(request.form['palm_length'])
        palm_width = float(request.form['palm_width'])
        finger_lengths = estimate_finger_lengths(palm_length, palm_width)
        return render_template('index.html', finger_lengths=finger_lengths)
    return render_template('index.html', finger_lengths=None)
if __name__ == '__main__':
    app.run(debug=True)



