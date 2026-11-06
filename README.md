## Student Exam Performance Prediction

Flask app that predicts a student's math score from demographic details and reading/writing scores.

### Deploy on Render

1. Push this repository to GitHub, including `artifacts/model.pkl` and `artifacts/preprocessor.pkl`.
2. In Render, choose **New +** → **Blueprint** and connect the GitHub repository.
3. Render reads `render.yaml` and creates the Python web service. Review the proposed service, then apply it.
4. Wait for the build and deploy to finish. Open the `onrender.com` URL Render provides.
5. The home page is `/`; submit the form at `/prediction` to check a prediction.

The service uses `requirements.txt` to install dependencies and Gunicorn to serve `application:app`. The Python version is set by `.python-version`.

### Deploy without a Blueprint

Create a **Web Service** from the same repository and set:

- Runtime: **Python 3**
- Build command: `pip install -r requirements.txt`
- Start command: `gunicorn application:app --bind 0.0.0.0:$PORT`
- Root directory: leave blank (the project files are at the repository root)

Keep the two `.pkl` model artifacts in `artifacts/`; prediction fails if either file is missing.
