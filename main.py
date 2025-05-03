import csv

def calculate_score(profile1, profile2):
    score = 0

    # Sleep Time Compatibility
    if profile1['sleep_time'] == profile2['sleep_time']:
        score += 25
    elif 'Moderate' in (profile1['sleep_time'], profile2['sleep_time']):
        score += 10

    # Cleanliness Tolerance
    levels = {'Low': 0, 'Medium': 1, 'High': 2}
    cleanliness_gap = abs(levels[profile1['cleanliness']] - levels[profile2['cleanliness']])
    if cleanliness_gap == 0:
        score += 25
    elif cleanliness_gap == 1:
        score += 15

    # Work Schedule Synergy
    if profile1['work_schedule'] == profile2['work_schedule']:
        score += 25
    elif {'Remote', '9-5'} <= {profile1['work_schedule'], profile2['work_schedule']}:
        score += 10
    elif {'Shift', '9-5'} <= {profile1['work_schedule'], profile2['work_schedule']}:
        score += 5

    # Food Habit Harmony
    if profile1['food_habits'] == profile2['food_habits']:
        score += 25
    elif {'Vegetarian', 'Non-Vegetarian'} <= {profile1['food_habits'], profile2['food_habits']}:
        score += 5

    return score

def load_profiles(file_path):
    profiles = []
    with open(file_path, newline='') as csvfile:
        reader = csv.DictReader(csvfile)
        for row in reader:
            profiles.append(row)
    return profiles

def rank_matches(new_profile, profiles):
    scored = []
    for profile in profiles:
        score = calculate_score(new_profile, profile)
        scored.append((profile['name'], score))
    return sorted(scored, key=lambda x: x[1], reverse=True)

if __name__ == '__main__':
    new_user = {
        'sleep_time': 'Early',
        'cleanliness': 'High',
        'work_schedule': '9-5',
        'food_habits': 'Vegetarian'
    }

    profiles = load_profiles('profiles.csv')
    ranked = rank_matches(new_user, profiles)

    print("Top Compatible Roommates:")
    for name, score in ranked:
        print(f"{name}: {score}/100")