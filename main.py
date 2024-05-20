import sys
import argparse

def main(param1, param2):
    print(f"Received parameters: param1={param1}, param2={param2}")
    # Add your business logic here

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="A script that processes two parameters.")
    parser.add_argument("--param1", required=True, help="First parameter")
    parser.add_argument("--param2", required=True, help="Second parameter")
    
    args = parser.parse_args()
    
    main(args.param1, args.param2)

