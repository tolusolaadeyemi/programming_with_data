from flask import Flask, request
app = Flask(__name__)

html_form_with_message = '''
<!DOCTYPE html>
<html>
<head>
<title>Text Echo App</title>
</head>
<body>
    <h2 style="color:pink">sums</h2>
    <form method="post" action="/">
        <label for="text">first number:</label><br>
        <input type="number" name="my_first_value"><br><br>
        <label for="text">second number:</label><br>
        <input type="number" name="my_second_value"><br><br>
        <input type="submit" value="My Button">
    </form>
    <p>put_data_here</p>
</body>
</html>
'''

def my_calculation(x,y):
    return x + y

@app.route('/', methods=['GET', 'POST'])
def home():
    first_input = ''
    second_input = ''
    calculated_value = 0
    if request.method == 'POST':
        first_input = request.form['my_first_value']
        second_input = request.form['my_second_value']
        calculated_value = my_calculation( int(first_input),int(second_input))

    display_text = f"the sum of {first_input} +  {second_input} is: {str(calculated_value)}"
    return html_form_with_message.replace("put_data_here", display_text)

app.run()