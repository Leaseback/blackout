from website import create_app

app = create_app()

if __name__ == '__main__': # If we run this file directly we will run the app, not if we import main.py
    app.run(debug=True)