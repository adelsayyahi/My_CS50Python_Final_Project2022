import sys
from PyQt5.QtWidgets import (
    QApplication, QWidget, QVBoxLayout, QLabel, QLineEdit, QPushButton, QMessageBox
)
from PyQt5.QtGui import QFont, QPalette, QColor
import pyqtgraph as pg


class BMICalculator(QWidget):
    def __init__(self):  # 🛠 Constructor for initializing the UI
        super().__init__()
        self.initUI()

    def initUI(self):
        self.setWindowTitle("BMI Calculator & Fatty Liver Probability")  # 🏷️ Set window title
        self.resize(800, 800)  # 📏 Set window size

        palette = QPalette()
        palette.setColor(QPalette.Window, QColor("#f0f0f0"))  # 🎨 Set background color
        self.setPalette(palette)

        layout = QVBoxLayout()
        font = QFont("Arial", 12)  # 🔤 Set font style and size

        self.height_label = QLabel("Height (cm):")
        self.height_label.setFont(font)
        self.height_input = QLineEdit()
        self.height_input.setFont(font)
        layout.addWidget(self.height_label)
        layout.addWidget(self.height_input)

        self.weight_label = QLabel("Weight (kg):")
        self.weight_label.setFont(font)
        self.weight_input = QLineEdit()
        self.weight_input.setFont(font)
        layout.addWidget(self.weight_label)
        layout.addWidget(self.weight_input)

        self.calculate_button = QPushButton("Calculate")  # 🔘 Button for calculation
        self.calculate_button.setFont(font)
        self.calculate_button.setStyleSheet("background-color: #4CAF50; color: white; padding: 8px; border-radius: 5px;")
        self.calculate_button.clicked.connect(self.calculate)
        layout.addWidget(self.calculate_button)

        self.result_label = QLabel("")  # 📊 Label to display results
        self.result_label.setFont(font)
        layout.addWidget(self.result_label)

        self.graph_widget = pg.PlotWidget()  # 📈 Widget for plotting data
        layout.addWidget(self.graph_widget)

        self.setLayout(layout)

    def calculate(self):
        try:
            height = float(self.height_input.text()) / 100  # 📏 Convert height to meters
            weight = float(self.weight_input.text())  # ⚖️ Get weight
            if height <= 0 or weight <= 0:
                raise ValueError("Height and weight must be positive numbers.")
            
            bmi = weight / (height ** 2)  # 🔢 Calculate BMI
            fatty_liver_prob = determine_fatty_liver_prob(bmi)  # 🔍 Determine probability
            fatty_liver_deg = determine_fatty_liver_degree(bmi)  # 📌 Determine fatty liver grade

            self.result_label.setText(
                f"BMI: {bmi:.2f}, Fatty Liver Probability: {fatty_liver_prob}, Liver Grade: {fatty_liver_deg}"
            )
            self.plot_data(bmi)  # 📊 Plot the BMI value
        except ValueError:
            QMessageBox.warning(self, "Invalid Input", "Please enter valid numeric values for height and weight.")  # ⚠️ Error handling

    def plot_data(self, bmi):
        x = [0, 1]
        y = [bmi, bmi]
        self.graph_widget.clear()
        self.graph_widget.plot(x, y, pen="r", symbol='o', symbolBrush='r')  # 📉 Plot BMI on graph


def determine_fatty_liver_prob(bmi):  # 📊 Categorize fatty liver probability
    if bmi < 25:
        return "Low probability"
    elif bmi < 30:
        return "Moderate probability"
    else:
        return "High probability"


def determine_fatty_liver_degree(bmi):  # 📌 Categorize fatty liver grade
    if bmi < 25:
        return "Normal"
    elif bmi < 30:
        return "Grade 1"
    else:
        return "Grade 2 or higher"


def main():  # 🚀 Entry point of the application
    app = QApplication(sys.argv)
    window = BMICalculator()
    window.show()
    sys.exit(app.exec_())


if __name__ == "__main__":  # ✅ Run the application
    main()