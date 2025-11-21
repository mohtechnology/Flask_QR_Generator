from flask import Flask , render_template, request, send_file
import qrcode as qr

# Defining the app
app = Flask(__name__)

# Home page how are you
@app.route('/', methods=['GET', 'POST'])
def gfg():
    if request.method == "POST":
        # Defining variables 
        link = request.form.get("link")
        global qr_n
        qr_n = ".png"
        path = "QR-Codes"
        img = qr.make(link)
        saved_image = path + "/" + qr_n
        img.save(saved_image)
        return render_template("index.html", activated=True)
    return render_template("index.html")

# Image page 
@app.route('/image')
def hello():
    return send_file("QR-Codes/" + qr_n, mimetype='image/png')

if __name__ == "__main__":
    app.run(debug=True)
