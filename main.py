from decouple import config
import requests

def get_api_key():
    return config('APEX_API_KEY')

def get_apex_legends_stats(player_name, platform):
    # Replace 'YOUR_API_KEY' with your actual API key
    api_key = get_api_key()
    # Define the API endpoint
    base_url = 'https://public-api.tracker.gg/v2/apex/standard/profile'
    
    # Construct the request URL
    url = f'{base_url}/{platform}/{player_name}'
    
    # Define headers with your API key
    headers = {
        'TRN-Api-Key': api_key
    }
    
    try:
        # Send GET request to the API
        response = requests.get(url, headers=headers)
        response.raise_for_status()

        # Parse JSON response
        player_data = response.json()
        
        # Extract and display stats
        stats = player_data['data']['segments'][0]['stats']
        
        print(f"Player: {player_data['data']['platformInfo']['platformUserId']}")
        print(f"Level: {stats['level']['value']}")
        print(f"Kills: {stats['kills']['value']}")
        print(f"Wins: {stats['wins']['value']}")
        print(f"Matches Played: {stats['matches']['value']}")

    except requests.exceptions.HTTPError as http_err:
        print(f"HTTP error occurred: {http_err}")
    except Exception as err:
        print(f"An error occurred: {err}")

if __name__ == "__main__":
    player_name = input("Enter Apex Legends player name: ")
    platform = input("Enter platform (pc/psn/xbl): ").lower()
    
    get_apex_legends_stats(player_name, platform)
