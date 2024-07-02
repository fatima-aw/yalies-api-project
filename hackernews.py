import requests

def get_latest_story():
    # Fetch the IDs of the most recent stories
    top_stories_url = "https://hacker-news.firebaseio.com/v0/newstories.json"
    response = requests.get(top_stories_url)
    story_ids = response.json()

    # Iterate through the story IDs to find the most recent story that is of type 'story'
    for story_id in story_ids:
        story_url = f"https://hacker-news.firebaseio.com/v0/item/{story_id}.json"
        story_response = requests.get(story_url)
        story = story_response.json()
        
        # Check if the item is of type 'story'
        if story.get('type') == 'story':
            return story

    return None

def print_story_details(story):
    if story:
        title = story.get('title', 'No title')
        author = story.get('by', 'No author')
        link = story.get('url', 'No link')
        
        print(f"Title: {title}")
        print(f"Author: {author}")
        print(f"Link: {link}")
    else:
        print("No recent story found.")

if __name__ == "__main__":
    latest_story = get_latest_story()
    print_story_details(latest_story)
