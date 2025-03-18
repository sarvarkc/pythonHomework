from bs4 import BeautifulSoup

html_doc = """
<!DOCTYPE html>
<html>
<head>
    <title>Weather Forecast</title>
</head>
<body>
    <h4>5-Day Weather Forecast</h4>
    <table>
        <thead>
            <tr>
                <th>Day</th>
                <th>Temperature</th>
                <th>Condition</th>
            </tr>
        </thead>
        <tbody>
            <tr>
                <td>Monday</td>
                <td>25°C</td>
                <td>Sunny</td>
            </tr>
            <tr>
                <td>Tuesday</td>
                <td>22°C</td>
                <td>Cloudy</td>
            </tr>
            <tr>
                <td>Wednesday</td>
                <td>18°C</td>
                <td>Rainy</td>
            </tr>
            <tr>
                <td>Thursday</td>
                <td>20°C</td>
                <td>Partly Cloudy</td>
            </tr>
            <tr>
                <td>Friday</td>
                <td>30°C</td>
                <td>Sunny</td>
            </tr>
        </tbody>
    </table>

</body>
</html>"""

soup = BeautifulSoup(html_doc, 'html.parser')
#print(soup.prettify())
def display_data():
    for x in soup.tbody.find_all('tr'):
        just = []
        for y in x.find_all('td'):
            just.append(y.text)
        print(",".join(just))

def specific_data():
    #max temperature
    nums = []
    for x in soup.tbody.find_all('tr'):
        just = []
        for y in x.find_all('td')[1].string:
            if y.isdigit():
                just.append(y)
        nums.append("".join(just))
    print("Max tempereture is:",max(nums))

    #The Sunny Conditions
    for x in soup.tbody.find_all('tr'):
        if x.find_all('td')[2].string == "Sunny":
            print(x.find_all('td')[0].string,x.find_all('td')[1].string,x.find_all('td')[2].string)

def average_temp():
    nums = []
    for x in soup.tbody.find_all('tr'):
        just = []
        for y in x.find_all('td')[1].string:
            if y.isdigit():
                just.append(y)
        nums.append(int("".join(just)))
    print("The average tempereture is:",sum(nums)/len(nums))

#display_data()
#specific_data()
#average_temp()



