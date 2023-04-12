from flask import Flask, request, render_template

app = Flask(__name__)



@app.route('/', methods=['GET', 'POST'])
def upload_file():
    if request.method == 'POST':
        file = request.files['file']

        file.save('videos/' + file.filename)
        return 'File' + file.filename + 'imported succesfully'
    return render_template('upload.html')


def identify_characters():
    """
    Identify the characters in the movie
    """
    pass


def style_transfer():
    """
    Take the video and apply a style to it.
    """
    pass


def generate_subtitels():
    pass


if __name__ == '__main__':
    app.run(debug=True)
