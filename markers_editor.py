import tkinter as tk
from tkinter import ttk, messagebox
import csv
import json
import os
import configparser
from datetime import datetime, time


def extract_unique_strings(obj, seen=None):
    if seen is None:
        seen = set()

    if isinstance(obj, str):
        seen.add(obj)
    elif isinstance(obj, dict):
        for value in obj.values():
            extract_unique_strings(value, seen)
    elif isinstance(obj, list):
        for item in obj:
            extract_unique_strings(item, seen)

    return list(seen)


options = configparser.ConfigParser()
options.read('options.ini')

NAMES = None
PLACES = None
t = None
with (open(f"locales/groups_{options["MAIN"]["language"]}.json", "r", encoding="utf-8") as groups_file,
      open(f"locales/locations_{options["MAIN"]["language"]}.json", "r", encoding="utf-8") as locations_file,
      open(f"locales/markers_editor_{options["MAIN"]["language"]}.json", "r", encoding="utf-8") as t_file):
    groups_json = json.load(groups_file)[options["MAIN"]["mode"]]
    NAMES = extract_unique_strings(groups_json) + list(groups_json.keys())
    PLACES = list(json.load(locations_file).keys())
    t = json.load(t_file)

START_TIME = time(7, 0)
END_TIME = time(18, 0)


def validate_and_format_time(hour_str, minute_str, period):
    try:
        hour = int(hour_str)
        minute = int(minute_str)
        if hour < 1 or hour > 12 or minute < 0 or minute > 59:
            return None
        if period == "PM" and hour != 12:
            hour += 12
        elif period == "AM" and hour == 12:
            hour = 0
        formatted = f"{hour:02d}:{minute:02d}"
        parsed_time = datetime.strptime(formatted, "%H:%M").time()
        if START_TIME <= parsed_time <= END_TIME:
            return f"{hour_str}:{minute_str} {period}"
    except ValueError:
        return None
    return None


def submit_data():
    hour = hour_entry.get()
    minute = minute_entry.get()
    period = period_combobox.get()
    name_input = name_combobox.get()
    place_input = place_combobox.get()

    formatted_time = validate_and_format_time(hour, minute, period)
    if not formatted_time:
        messagebox.showerror(t["error"], t["enter_correct_timestamp"])
        return

    if name_input not in NAMES:
        messagebox.showerror(t["error"], t['name_not_found'])
        return

    if place_input not in PLACES:
        messagebox.showerror(t["error"], t["place_not_found"])
        return

    with open("cartographer_in&out\markers.csv", "a", encoding='utf-8') as file:
        writer = csv.writer(file)
        writer.writerow([formatted_time, name_input, place_input])

    log_entry(t["recorded"].format(formatted_time=formatted_time, name_input=name_input, place_input=place_input))
    hour_entry.delete(0, tk.END)
    minute_entry.delete(0, tk.END)
    period_combobox.set('')
    name_combobox.set('')
    place_combobox.set('')

    hour_entry.focus_set()


def undo_last_entry():
    if not os.path.exists("cartographer_in&out\markers.csv"):
        messagebox.showwarning(t["error"], t["no_data_to_undo"])
        return

    with open("cartographer_in&out\markers.csv", "r", encoding='utf-8') as file:
        lines = file.readlines()

    if not lines:
        messagebox.showwarning(t["error"], t["no_data_to_undo"])
        return

    with open("cartographer_in&out\markers.csv", "w", encoding='utf-8') as file:
        file.writelines(lines[:-1])
    
    if len(lines) == 1:
        log_entry(t["undone_csv_empty"])
    else:
        log_entry(t["undone_last_entry"].format(lines=lines[-1]))


def log_entry(message):
    log_text.configure(state='normal')
    log_text.insert(tk.END, f"{datetime.now().strftime('%H:%M:%S')} — {message}\n")
    log_text.configure(state='disabled')
    log_text.see(tk.END)


class AutocompleteCombobox(ttk.Combobox):
    def __init__(self, master=None, completevalues=None, **kwargs):
        super().__init__(master, width=40, **kwargs)
        self._completion_list = completevalues or []
        self._hits = []
        self._typed = ''
        self.bind('<KeyRelease>', self._on_keyrelease)
        self['values'] = self._completion_list

    def set_completion_list(self, completion_list):
        self._completion_list = sorted(completion_list)
        self['values'] = self._completion_list

    def _on_keyrelease(self, event):
        value = self.get()
        if value == '':
            self['values'] = self._completion_list
        else:
            self['values'] = [item for item in self._completion_list if item.lower().startswith(value.lower())]


# Создание окна
root = tk.Tk()
root.title(t["markers_editor"])

# Метка "Время:"
ttk.Label(root, text=t["timestamp"]).grid(row=0, column=0, padx=5, pady=5, sticky='e')

# Часы
hour_entry = ttk.Entry(root, width=5)
hour_entry.grid(row=0, column=1, pady=5, sticky='w')

# Двоеточие
ttk.Label(root, text=":").grid(row=0, column=2, pady=5, sticky='w')

# Минуты
minute_entry = ttk.Entry(root, width=5)
minute_entry.grid(row=0, column=3, pady=5, sticky='w')

# AM/PM
period_combobox = ttk.Combobox(root, values=["AM", "PM"], width=5, state='readonly')
period_combobox.grid(row=0, column=4, pady=5, sticky='w')

# Имя с автодополнением
ttk.Label(root, text=t["name"]).grid(row=1, column=0, padx=5, pady=5, sticky='e')
name_combobox = AutocompleteCombobox(root, completevalues=NAMES)
name_combobox.grid(row=1, column=1, columnspan=4, padx=5, pady=5)

# Место с автодополнением
ttk.Label(root, text=t["place"]).grid(row=2, column=0, padx=5, pady=5, sticky='e')
place_combobox = AutocompleteCombobox(root, completevalues=PLACES)
place_combobox.grid(row=2, column=1, columnspan=4, padx=5, pady=5)

# Кнопки
submit_button = ttk.Button(root, text=t["submit"], command=submit_data)
submit_button.grid(row=2, column=5, pady=5)

undo_button = ttk.Button(root, text=t["undo"], command=undo_last_entry)
undo_button.grid(row=0, column=5, pady=5)

# Лог
ttk.Label(root, text=t["logs"]).grid(row=4, column=0, pady=(10, 0))
log_text = tk.Text(root, height=10, width=50, state='disabled', bg="#f7f7f7")
log_text.grid(row=5, column=1, columnspan=19, padx=5, pady=5)

root.bind('<Return>', lambda event: submit_data())
root.bind('<Control-z>', lambda event: undo_last_entry())

root.mainloop()
