from flask import Flask, render_template, request, redirect, url_for, send_from_directory
import os
import shutil

app = Flask(__name__)

UPLOAD_FOLDER = 'uploads'
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER

images = []

@app.route('/')
def index():
    return render_template('index.html', images=images)

@app.route('/upload_folder', methods=['POST'])
def upload_folder():
    global images
    folder_path = request.form.get('folder_path')
    if folder_path:
        if os.path.exists(UPLOAD_FOLDER):
            shutil.rmtree(UPLOAD_FOLDER)
        os.makedirs(UPLOAD_FOLDER)

        images = [img for img in os.listdir(folder_path) if img.endswith(('.png', '.jpeg'))]
        for img in images:
            shutil.copy(os.path.join(folder_path, img), UPLOAD_FOLDER)
    return redirect(url_for('index'))

@app.route('/get_image/<filename>')
def get_image(filename):
    return send_from_directory(UPLOAD_FOLDER, filename)


@app.route('/update_filename', methods=['POST'])
def update_filename():
    global images
    new_name = request.form.get('new_name')
    if not new_name.endswith('.png'):
        new_name += '.png'

    current_image = request.form.get('current_image')
    new_path = os.path.join(UPLOAD_FOLDER, new_name)

    # Eğer dosya zaten varsa, onu sil
    if os.path.exists(new_path):
        os.remove(new_path)

    os.rename(os.path.join(UPLOAD_FOLDER, current_image), new_path)
    images.pop(0)
    return redirect(url_for('index'))


@app.route('/reset', methods=['POST'])
def reset():
    global images
    images = []
    if os.path.exists(UPLOAD_FOLDER):
        shutil.rmtree(UPLOAD_FOLDER)
    return redirect(url_for('index'))

if __name__ == '__main__':
    app.run(debug=True)
