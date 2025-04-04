import tkinter as tk

def check_life_stage():
    age_text = entry.get()
    
    if age_text.isdigit():
        age = int(age_text)
        if age < 0:
            result.set("You haven't been born yet! 👻")
        elif age <= 12:
            result.set("You're a Kid 👶")
        elif age <= 19:
            result.set("You're a Teenager 🧑‍🎓")
        elif age <= 35:
            result.set("Young Adult life! 💼")
        elif age <= 59:
            result.set("You're in your Prime! 🏆")
        elif age <= 99:
            result.set("You're a Wise Senior 👴")
        else:
            result.set("Legendary Status Achieved! 🦸‍♂")
    else:
        result.set("Please enter a valid positive number!")

# GUI setup
root = tk.Tk()
root.title("Life Stage Checker")
root.geometry("350x220")
root.configure(bg="#e3f2fd")

tk.Label(root, text="Enter your age:", font=("Arial", 12), bg="#e3f2fd").pack(pady=10)

entry = tk.Entry(root, font=("Arial", 13))
entry.pack(pady=5)

tk.Button(root, text="Check Life Stage", command=check_life_stage,
          font=("Arial", 12), bg="#42a5f5", fg="white").pack(pady=10)

result = tk.StringVar()
tk.Label(root, textvariable=result, font=("Arial", 12), bg="#e3f2fd", fg="#0d47a1").pack(pady=10)

root.mainloop()
