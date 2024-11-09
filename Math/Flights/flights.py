import pandas as pd
from collections import deque
import os

def find_path(df, start, end):
    graph = {}
    for _, row in df.iterrows():
        if row['Departure Country'] not in graph:
            graph[row['Departure Country']] = set()
        graph[row['Departure Country']].add(row['Arrival Country'])
    
    queue = deque([(start, [start])])
    visited = set()

    while queue:
        (country, path) = queue.popleft()
        if country not in visited:
            visited.add(country)
            
            if country == end:
                return path
            
            for next_country in graph.get(country, []):
                if next_country not in visited:
                    queue.append((next_country, path + [next_country]))
    
    return None

def recommend_flight(file_path, departure_country, arrival_country):
    try:
        if not os.path.exists(file_path):
            print(f"Error: The file '{file_path}' does not exist.")
            return

        df = pd.read_csv(file_path)
        
        required_columns = ['Flight Number', 'Airline', 'Departure Country', 'Arrival Country']
        if not all(col in df.columns for col in required_columns):
            print(f"Error: The CSV file is missing one or more required columns: {', '.join(required_columns)}")
            return
        
        path = find_path(df, departure_country, arrival_country)
        
        if not path:
            print(f"No path found from {departure_country} to {arrival_country}.")
            return
        
        print(f"\nPath found from {departure_country} to {arrival_country}:")
        print(f"Number of stops: {len(path) - 2}")
        print("\nFlight route:")
        
        for i in range(len(path) - 1):
            from_country = path[i]
            to_country = path[i+1]
            flight = df[(df['Departure Country'] == from_country) & (df['Arrival Country'] == to_country)].iloc[0]
            print(f"{i+1}. {flight['Airline']} {flight['Flight Number']}: {from_country} -> {to_country}")
    
    except Exception as e:
        print(f"An error occurred: {str(e)}")
        print("Please check that your CSV file is properly formatted and contains the required columns.")

# Usage example:
file_path = 'C:/Users/ASUS/gen-ai/expanded_flight_dataset.csv'

# Get user input for departure and arrival countries
departure_country = input("Enter the departure country: ")
arrival_country = input("Enter the arrival country: ")

# Call the function
recommend_flight(file_path, departure_country, arrival_country)

