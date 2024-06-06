import subprocess
import sys

def main():
    while True:
        print("Welcome to Tic-Tac-Toe!")
        print("Choose your mode:")
        print("1. GUI")
        print("2. CLI")
        choice = input("Enter your choice (1 or 2): ")
        
        if choice == '1':
            print("Launching GUI version...")
            subprocess.run([sys.executable, 'gui.py'])
            break
        elif choice == '2':
            print("Launching CLI version...")
            subprocess.run([sys.executable, 'cli.py'])
            break
        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()
