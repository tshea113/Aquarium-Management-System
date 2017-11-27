from flask import Flask, render_template, request, flash, url_for

app = Flask(__name__)


#Home page
@app.route('/')
def index():
    return render_template('index.html')


#Handles sending the schedule params to the text file for the feeder
@app.route('/change_schedule', methods=['GET', 'POST'])
def change_schedule():

    if request.method == 'POST':
        start = request.form['feedStart']
        interval = request.form['feedInterval']
        feedParams = (int(start), int(interval))

        if feedParams[0] > 0 & feedParams[0] < 23 & feedParams[1] > 0:
            with open('test.txt', 'w') as f:
                f.write(str(feedParams[0]) + ' ' + str(feedParams[1]))

        else:
            return render_template('change_schedule.html')

        return render_template('index.html')
    else:
        return render_template('change_schedule.html')


@app.route('/about')
def about():
    return render_template('about.html')

@app.route('/live_view')
def live_view():
    return render_template('live_view.html')

@app.errorhandler(404)
def page_not_found(e):
    return render_template('404.html')


if __name__ == "__main__":
    app.run(debug=True)
