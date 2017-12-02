from flask import Flask, render_template, request, flash, url_for
import feeder_control
from multiprocessing import Process


app = Flask(__name__)

p=0

def getFeedInfo():
	try:
		with open("/home/pi/fish_feeder/env/fishFeeder/logs/last_feed.txt", "r") as f:
			lastFeed = f.read()

		with open("/home/pi/fish_feeder/env/fishFeeder/logs/next_feed.txt", "r") as f:
			nextFeed = f.read()

		return (lastFeed, nextFeed)

	except:
		return ("Error: Something went wrong!", "Error: Something went Wrong!")


@app.before_first_request
def setupFeeder():
	global p   
        p = Process(target=feeder_control.runFeeder)
	p.daemon=True
	p.start()


# Home page
@app.route('/')
def index():
    global p	
    temp = p.is_alive()
    feedInfo = getFeedInfo()
    return render_template('index.html', lastFeedTime = feedInfo[0], nextFeedTime = feedInfo[1], status = temp)


# Handles sending the schedule params to the text file for the feeder
@app.route('/change_schedule', methods=['GET', 'POST'])
def change_schedule():
    feedInfo = getFeedInfo()

    if request.method == 'POST':
        start = request.form['feedStart']
        interval = request.form['feedInterval']
        feedParams = (int(start), int(interval))

        if feedParams[0] > 0 & feedParams[0] < 23 & feedParams[1] > 0:
            with open('/home/pi/fish_feeder/env/fishFeeder/logs/feed_time.txt', 'w') as f:
            	f.write(str(feedParams[0]) + ' ' + str(feedParams[1]))

	    return render_template('index.html', lastFeedTime = feedInfo[0], nextFeedTime = feedInfo[1])

        else:
            return render_template('change_schedule.html', lastFeedTime = feedInfo[0], nextFeedTime = feedInfo[1])

    else:
        return render_template('change_schedule.html', lastFeedTime = feedInfo[0], nextFeedTime = feedInfo[1])


@app.route('/about')
def about():
    feedInfo = getFeedInfo()
    return render_template('about.html', lastFeedTime = feedInfo[0], nextFeedTime = feedInfo[1])


@app.route('/live_view')
def live_view():
    feedInfo = getFeedInfo()
    global p
    p.terminate()
    p = Process(target=feeder_control.runFeeder)
    p.daemon = True
    p.start()
    return render_template('live_view.html', lastFeedTime = feedInfo[0], nextFeedTime = feedInfo[1])


@app.errorhandler(404)
def page_not_found(e):
    return render_template('404.html')


if __name__ == "__main__":   
	app.run(debug=True)
