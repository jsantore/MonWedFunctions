import urllib.request
import json

def get_data():
    downloaded_data = urllib.request.urlopen("https://webhost.bridgew.edu/jsantore/Fall2026/CS1/Data.json")
    data = json.load(downloaded_data)
    return data

def print_menu():
    print("""
    [1] find increase in salary from entry level to after 2 years
    [2] How many jobs of this type are there
    [9] quit
    """)
def find_salary_increase(job):
    entry_salary = job["entry_salary"]
    two_years_salary = job["salary_after2_years"]
    expected_raise = two_years_salary - entry_salary
    return expected_raise

def main():
    salary_data = get_data()
    while True:
        print_menu()
        choice = input("Enter your choice: ")
        if choice == "9":
            break
        elif choice == "1":
            for this_job in salary_data:
                salary_increase=find_salary_increase(this_job)
                print(f"After two years most people woring {this_job['job']} will increase their salary by ${salary_increase}")
        elif choice == "2":
            print("not implemented yet")
        else:
            print("invalid input")
main()