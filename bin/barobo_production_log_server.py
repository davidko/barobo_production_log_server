#!/usr/bin/env python3

import bottle
from linkbot_diagnostics import Database
import time

cur_time = time.time()
# Find the time 30 days ago
past_time = cur_time - (30 * 24 * 60 * 60)

past_time = time.localtime(past_time)

time_str = time.strftime('%Y-%m-%d 00:00:00', past_time)

@bottle.route('/')
def main_page():

    page_html = """
        <table>
        """

    with Database() as db:
        sql_statement = """
    SELECT DISTINCT Id, Date from linearity_tests WHERE Date >= '{}' ORDER BY Date DESC
        """.format(time_str)
        rows = db.fetch_all(sql_statement)
        for row in rows:
            timestamp = "{} {} {}".format(row[1].year, row[1].month, row[1].day)
            page_html += """
                <tr>
                    <td> {} </td>
                    <td> {} </td>
                </tr>""".format(row[0], timestamp)

    page_html += "</table>"

    return page_html

bottle.run(host="0.0.0.0", port="8082")
