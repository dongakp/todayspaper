from apscheduler.schedulers.background import BackgroundScheduler
from scrapingPapers import scrap
from flask import Flask, render_template, request
from keyWordSearch import paperIncluding

schedule = BackgroundScheduler(daemon=True, timezone='Asia/Seoul')
schedule.add_job(scrap, 'cron', hour=11, minute=0, second=0)
schedule.start()

app = Flask(__name__)

@app.route('/todayspaper/')
def main_page():
    return render_template('main.html')

@app.route('/todayspaper/search')
def search():
    keyword = request.args.get('keyword')
    selected = paperIncluding(keyword)
    if len(selected)==0:
        contents='<p style="font-size:32px; text-align:center;">No paper is found</p>'
    else:
        contents=''
        for paper in selected:
            contents += (f'<a href="https://arxiv.org/pdf/{paper['ID']}" target="_blank">'+paper['title'] + '</a><br>')
            authors = 'Authors: '
            for author in paper['authors'][:3]:
                authors += (author + ', ')
            if len(paper['authors'])>3:
                authors += ' ...<br><br>'
            else:
                authors = authors[:-2]
                authors += '<br><br>'
            contents += authors
    return render_template('search.html').format(keyword,contents)

app.run(port=5001, debug=True)