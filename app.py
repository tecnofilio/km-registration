from pathlib import Path
from uuid import uuid4

from flask import Flask, flash, redirect, render_template, request, url_for
from werkzeug.utils import secure_filename


BASE_DIR = Path(__file__).resolve().parent
UPLOAD_FOLDER = BASE_DIR / "static" / "uploads"
ALLOWED_EXTENSIONS = {"png", "jpg", "jpeg", "gif", "webp"}
CATEGORY_OPTIONS = ("Office", "Private", "Office + private", "BT")


app = Flask(__name__)
app.config["SECRET_KEY"] = "change-this-secret-key"
app.config["UPLOAD_FOLDER"] = UPLOAD_FOLDER
app.config["MAX_CONTENT_LENGTH"] = 8 * 1024 * 1024

UPLOAD_FOLDER.mkdir(parents=True, exist_ok=True)


def allowed_file(filename):
    return "." in filename and filename.rsplit(".", 1)[1].lower() in ALLOWED_EXTENSIONS


@app.route("/", methods=["GET", "POST"])
def index():
    image_url = None
    selected_category = None
    comments = None

    if request.method == "POST":
        file = request.files.get("photo")
        selected_category = request.form.get("category", "")
        comments = request.form.get("comments", "").strip()

        if not file or file.filename == "":
            flash("Selecciona una foto antes de subirla.")
            return redirect(url_for("index"))

        if selected_category not in CATEGORY_OPTIONS:
            flash("Selecciona una opcion valida del menu.")
            return redirect(url_for("index"))

        if not allowed_file(file.filename):
            flash("Formato no permitido. Usa PNG, JPG, JPEG, GIF o WEBP.")
            return redirect(url_for("index"))

        original_name = secure_filename(file.filename)
        extension = original_name.rsplit(".", 1)[1].lower()
        filename = f"{uuid4().hex}.{extension}"
        save_path = app.config["UPLOAD_FOLDER"] / filename
        file.save(save_path)

        image_url = url_for("static", filename=f"uploads/{filename}")
        flash("Foto subida correctamente.")

    return render_template(
        "index.html",
        category_options=CATEGORY_OPTIONS,
        comments=comments,
        image_url=image_url,
        selected_category=selected_category,
    )


@app.errorhandler(413)
def file_too_large(_error):
    flash("La foto es demasiado grande. El limite es 8 MB.")
    return redirect(url_for("index"))


if __name__ == "__main__":
    app.run(debug=True)
