from flask import Flask, render_template,redirect,url_for
import pandas as pd
import matplotlib.pyplot as plt
import os

app = Flask(__name__)

data_df = pd.DataFrame()

@app.route("/page1")
def page1():
    # Step 1: Read CSV file into Pandas DataFrame
    #df = pd.read_csv("academicStress.csv")
    #df.head()

    # Step 2: Convert DataFrame to HTML table
    #table_html = df.head().to_html( index=False)

    # Step 3: Send table to HTML template
    #return render_template("page1.html", table=table_html, title=" Table 1")

#@app.route('/page2')
#def page2():
    #df = pd.read_csv("multilingual_mobile_app_reviews_2025.csv")
    #df.head()
    #table_html = df.head().to_html(index = False)

    #return render_template("page2.html", table = table_html, title = "Table 2")

#@app.route('/page3')
#def page3():
    #df = pd.read_csv("ai_personality_selfie_dataset.csv")
    #df.head()
    #table_html = df.head().to_html(index = False)

    #return render_template("page3.html", table = table_html, title = "Table 3")

#@app.route('/page4')
#def page4():
    #df = pd.read_csv("blood_donor_dataset.csv")
    #df.head()
    #table_html = df.head().to_html(index = False)

    #return render_template("page4.html", table = table_html, title = "Table 4")

@app.route('/')
def Home_page():
    global data_df
    data_df = pd.read_csv("65k_anime_data.csv").head()
    return render_template("Home_page.html",title = "PANDAS",table = data_df.to_html(index = False, classes="table"))

@app.route('/bar')
def bar():
    if data_df.empty:
        return redirect('/Home')
    plt.bar(data_df["rank"], data_df["synopsis"])
    plt.xlabel("Rank")
    plt.ylabel("Synopsis")
    plt.grid(False)
    char_path = os.path.join('static','chart.png')
    plt.savefig(char_path)
    plt.close()

    return render_template('bar.html',chart_url = url_for('static',filename='chart.png'))

if (__name__) == "__main__":
    app.run(port = 3000, host = "0.0.0.0", debug = False)


