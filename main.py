from flask import Flask, render_template
import pandas as pd
import matplotlib.pyplot as plt
import io
import base64

app = Flask(__name__)

@app.route('/')
def index():
    data = pd.read_csv('../data/road_data.csv')

    # Generate a simple matplotlib plot
    plt.figure(figsize=(10, 6))
    plt.bar(data['Road'], data['Assessment'])
    plt.xlabel('Road')
    plt.ylabel('Assessment')
    plt.title('Road Assessment Data')
    plt.tight_layout()

    # Convert plot to base64 for displaying in HTML
    buffer = io.BytesIO()
    plt.savefig(buffer, format='png')
    buffer.seek(0)
    image_base64 = base64.b64encode(buffer.read()).decode('utf-8')
    buffer.close()

    return render_template('index.html', image_base64=image_base64)

if __name__ == '__main__':
    app.run(debug=True)
