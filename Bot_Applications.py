from tkinter import *
from tkinter import simpledialog
from tkinter import messagebox
import numpy as np


def cal_bmi():
    global res
    application_window = Tk()
    application_window.title("calculate bmi")
    application_window.geometry("0x0")
    confirm = messagebox.askokcancel("Confirm", "Calculate BMI?")
    if confirm:
        weight = float(simpledialog.askfloat("weight", "Enter your weight in kg:", parent=application_window))
        height = float(simpledialog.askfloat("height", "Enter your height in meter:", parent=application_window))
        application_window.destroy()
        bmi = np.divide(weight, np.square(height))
        below = ",you're in the underweight range."
        good = ",you're in the healthy weight range."
        over = ",you're in the overweight range."
        obese = ",you're in the obese range."
        if bmi < 18.5:
            res = "Your BMI is: " + str(bmi) + below + "\n\n" + "Bot: Hi! What can I do for you?(type 'quit' to stop)"
        elif 18.5 <= bmi <= 24.9:
            res = "Your BMI is: " + str(bmi) + good + "\n\n" + "Bot: Hi! What can I do for you?(type 'quit' to stop)"
        elif 25 <= bmi <= 29.9:
            res = "Your BMI is: " + str(bmi) + over + "\n\n" + "Bot: Hi! What can I do for you?(type 'quit' to stop)"
        else:
            res = "Your BMI is: " + str(bmi) + obese + "\n\n" + "Bot: Hi! What can I do for you?(type 'quit' to stop)"
    else:
        res = "Bot: Hi! What can I do for you?(type 'quit' to stop)"
    return res


def cal_bodyfat():
    global formula
    global res
    global fat_rate
    application_window = Tk()
    application_window.title("calculate body fat")
    application_window.geometry("0x0")
    confirm = messagebox.askokcancel("Confirm", "Calculate Body Fat?")
    if confirm:
        gender = simpledialog.askstring("gender", "Enter your gender: a) male b)female", parent=application_window)
        if gender.lower() == "a" or gender.lower() == "male":
            formula = "a"
        elif gender.lower() == "b" or gender.lower() == "female":
            formula = "b"
        else:
            messagebox.showinfo("Invalid Input", "Please enter a valid value")
            return None
        age = float(simpledialog.askfloat("age", "Enter your age:", parent=application_window))
        weight = float(simpledialog.askfloat("weight", "Enter your weight in kg:", parent=application_window))
        height = float(simpledialog.askfloat("height", "Enter your height in meter:", parent=application_window))
        application_window.destroy()
        bmi = np.divide(weight, np.square(height))
        if formula == "b":
            fat_rate = 1.2 * bmi + 0.23 * age - 5.4 - 10.8 * 0
            if fat_rate < 14:
                res = "body fat: " + str(
                    fat_rate) + "%" + ", dangerously low." + "\n\n" + "Bot: Hi! What can I do for you?(type 'quit' to stop)"
            elif 14 <= fat_rate <= 16.5:
                res = "body fat: " + str(
                    fat_rate) + "%" + ", excellent." + "\n\n" + "Bot: Hi! What can I do for you?(type 'quit' to stop)"
            elif 16.5 < fat_rate <= 19.4:
                res = "body fat: " + str(
                    fat_rate) + "%" + ", good." + "\n\n" + "Bot: Hi! What can I do for you?(type 'quit' to stop)"
            elif 19.4 < fat_rate <= 22.7:
                res = "body fat: " + str(
                    fat_rate) + "%" + ", fair." + "\n\n" + "Bot: Hi! What can I do for you?(type 'quit' to stop)"
            elif 22.7 < fat_rate <= 27.1:
                res = "body fat: " + str(
                    fat_rate) + "%" + ", poor." + "\n\n" + "Bot: Hi! What can I do for you?(type 'quit' to stop)"
            elif 27.1 < fat_rate:
                res = "body fat: " + str(
                    fat_rate) + "%" + ", dangerously high." + "\n\n" + "Bot: Hi! What can I do for you?(type 'quit' to stop)"
        else:
            fat_rate = 1.2 * bmi + 0.23 * age - 5.4 - 10.8 * 1
            if fat_rate < 8:
                res = "body fat: " + str(
                    fat_rate) + "%" + ", dangerously low." + "\n\n" + "Bot: Hi! What can I do for you?(type 'quit' to stop)"
            elif 8 <= fat_rate <= 10.5:
                res = "body fat: " + str(
                    fat_rate) + "%" + ", excellent." + "\n\n" + "Bot: Hi! What can I do for you?(type 'quit' to stop)"
            elif 10.5 < fat_rate <= 14.8:
                res = "body fat: " + str(
                    fat_rate) + "%" + ", good." + "\n\n" + "Bot: Hi! What can I do for you?(type 'quit' to stop)"
            elif 14.8 < fat_rate <= 18.6:
                res = "body fat: " + str(
                    fat_rate) + "%" + ", fair." + "\n\n" + "Bot: Hi! What can I do for you?(type 'quit' to stop)"
            elif 18.6 < fat_rate <= 23.1:
                res = "body fat: " + str(
                    fat_rate) + "%" + ", poor." + "\n\n" + "Bot: Hi! What can I do for you?(type 'quit' to stop)"
            elif 23.1 < fat_rate:
                res = "body fat: " + str(
                    fat_rate) + "%" + ", dangerously high." + "\n\n" + "Bot: Hi! What can I do for you?(type 'quit' to stop)"
    else:
        res = "Bot: Hi! What can I do for you?(type 'quit' to stop)"
    return res


def set_goal():
    global res
    global goal_path
    global fat_rate
    global formula
    global activity
    global BMR
    global cal
    application_window = Tk()
    application_window.title("set fitness goal")
    application_window.geometry("0x0")
    confirm = messagebox.askokcancel("Confirm", "Calculate Daily Calorie Intake?")
    if confirm:
        goal = simpledialog.askstring("select your goal",
                                      "Select Your Fitness Goal: a)lose weight b)gain muscle c)maintain current weight",
                                      parent=application_window)
        if goal.lower() == "a":
            goal_path = "a"
        elif goal.lower() == "b":
            goal_path = "b"
        elif goal.lower() == "c":
            goal_path = "c"
        else:
            messagebox.showinfo("Invalid Input", "Please enter a valid value")
            return None
        gender = simpledialog.askstring("gender", "Enter your gender: a) male b)female", parent=application_window)
        if gender.lower() == "a" or gender.lower() == "male":
            formula = "m"
        elif gender.lower() == "b" or gender.lower() == "female":
            formula = "f"
        else:
            messagebox.showinfo("Invalid Input", "Please enter a valid value")
            return None
        age = float(simpledialog.askfloat("age", "Enter your age:", parent=application_window))
        weight = float(simpledialog.askfloat("weight", "Enter your weight in kg:", parent=application_window))
        height = float(simpledialog.askfloat("height", "Enter your height in meter:", parent=application_window))
        bmi = np.divide(weight, np.square(height))
        if gender.lower() == "a" or gender.lower() == "male":
            fat_rate = 1.2 * bmi + 0.23 * age - 5.4 - 10.8 * 1
            BMR = 66 + np.multiply(6.3, np.multiply(weight, 2.20462)) + np.multiply(12.9, np.multiply(height,
                                                                                                      39.3701)) - np.multiply(
                6.8, age)
        if gender.lower() == "b" or gender.lower() == "female":
            fat_rate = 1.2 * bmi + 0.23 * age - 5.4 - 10.8 * 0
            BMR = 655 + np.multiply(4.3, np.multiply(weight, 2.20462)) + np.multiply(4.7, np.multiply(height,
                                                                                                      39.3701)) - np.multiply(
                4.7, age)
        activity = simpledialog.askstring("select your daily activity level",
                                          "Select your daily activity level: a)little or no exercise b)light exercise/sports 1-3 days/week c)moderate exercise/sports 3-5 days/week d)hard exercise/sports 6-7 days a week e)very hard exercise/sports & physical job or 2x training",
                                          parent=application_window)
        if activity.lower() == "a":
            cal = np.multiply(BMR, 1.2)
        elif activity.lower() == "b":
            cal = np.multiply(BMR, 1.375)
        elif activity.lower() == "c":
            cal = np.multiply(BMR, 1.55)
        elif activity.lower() == "d":
            cal = np.multiply(BMR, 1.725)
        elif activity.lower() == "e":
            cal = np.multiply(BMR, 1.9)
        if goal_path == "a":
            res = "In order to lose weight, your daily calorie intake should be less than" + str(
                cal - 500) + "cal -" + str(cal - 1000) + "cal."
        elif goal_path == "b":
            res = "In order to gain muscle, consume more than" + str(cal) + "cal a day."
        elif goal_path == "c":
            res = "To maintain your current weight, your daily calorie intake should be" + str(cal) + "cal."
    else:
        res = "Bot: Hi! What can I do for you?(type 'quit' to stop)"
    return res
