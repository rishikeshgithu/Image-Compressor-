import tinify
from flask import Flask, render_template, request, redirect, url_for

app = Flask(__name__)

# Set your API key here
tinify.key = "wS3BplSqHJCxXgHhsfm9Zq5k0bbFpq7C"

@app.route("/", methods=["GET", "POST"])
def index():
    if request.method == "POST":
        input_image = request.files["input_image"]
        if input_image:
            input_image_path = "input_image.jpg"  # Temporary path
            input_image.save(input_image_path)

            output_image_path = "output_image.jpg"  # Replace with the desired output image path
            compress_image(input_image_path, output_image_path)

            return render_template("result.html", input_image_path=input_image_path, output_image_path=output_image_path)

    return render_template("index.html")

def compress_image(input_path, output_path):
    try:
        # Compress the image using Tinify
        source = tinify.from_file(input_path)
        source.to_file(output_path)

        print(f"Image compressed and saved to {output_path}")
    except tinify.errors.AccountError as e:
        print(f"Tinify API Error: {e}")
    except Exception as e:
        print(f"An error occurred: {e}")

if __name__ == "__main__":
    app.run(debug=True)
