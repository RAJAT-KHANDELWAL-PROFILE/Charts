from flask import Flask, render_template, request
import plotly.graph_objs as go
import plotly.io as pio

app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def index():
    plot_div = None
    if request.method == 'POST':
        title = request.form['title']
        x_label = request.form['x_label']
        y_label = request.form['y_label']
        x_data = request.form['x_data'].split(',')
        y_data = list(map(float, request.form['y_data'].split(',')))
        plot_type = request.form['plot_type']
        
        if plot_type == 'bar':
            fig = go.Figure(data=[go.Bar(x=x_data, y=y_data)])
        elif plot_type == 'line':
            fig = go.Figure(data=[go.Scatter(x=x_data, y=y_data, mode='lines')])
        elif plot_type == 'scatter':
            fig = go.Figure(data=[go.Scatter(x=x_data, y=y_data, mode='markers')])

        fig.update_layout(
            title=title,
            xaxis_title=x_label,
            yaxis_title=y_label,
            paper_bgcolor='rgba(0,0,0,0)',
            plot_bgcolor='rgba(0,0,0,0)',
            font=dict(color='#333')
        )

        plot_div = pio.to_html(fig, full_html=False)
    
    return render_template('index.html', plot_div=plot_div)

if __name__ == '__main__':
    app.run(debug=True)
