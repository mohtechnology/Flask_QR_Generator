import qrcode as qr
from flask import Flask , render_template, request, send_file

app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def gfg():
    if request.method == "POST":
        link = request.form.get("link")
        qr_name = request.form.get("qr_name")
        global qr_n
        qr_n = qr_name + ".png"
        img = qr.make(link)
        saved_image = img.save(qr_n)
        return render_template("index.html", activated=True)
    return render_template("index.html")

@app.route('/image')
def hello():
    return send_file(qr_n, mimetype='image/png')

if __name__ == "__main__":
    app.run(debug=True)
