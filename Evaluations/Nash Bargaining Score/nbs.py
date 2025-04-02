# Nash Bargaining Score

# Map the preferences: High, Medium and Low as numeric values 1,2,3 respectively.
def map_participant_preferences(preferences):
    mapping = {"High": 3, "Medium": 2, "Low": 1}
    return {resource: mapping[level] for level, resource in preferences.items()}


# Utility of a player - calculated as the sum of the resources 
# provided and summed over their preferences represented as weights
# U_i = w_{firewood} * x_{firewood} + w_{water} * x_{water} + w_{food} * x_{food}
def utility(resources, preferences):
    return sum(resources[resource]*preferences[resource] for resource in resources)


# Compute the NBS score between 2 participants
# F = (U_1 - U_1^{min}) * (U_2 - U_2^{min}) / (U_1^{max} - U_1^{min}) * (U_2^{max} - U_2^{min})
def compute_NBS(resources_p1, p1_prefs, resources_p2, p2_prefs):
    preferences_p1 = map_participant_preferences(p1_prefs)
    preferences_p2 = map_participant_preferences(p2_prefs)

    U1 = utility(resources_p1, preferences_p1)
    U2 = utility(resources_p2, preferences_p2)

    min_p1, max_p1 = 0, utility({'Firewood': 3, 'Water': 3, 'Food': 3}, preferences_p1)
    min_p2, max_p2 = 0, utility({'Firewood': 3, 'Water': 3, 'Food': 3}, preferences_p2)

    num = (U1-min_p1) * (U2-min_p2)
    denom = (max_p1 - min_p1) * (max_p2 - min_p2)

    if denom == 0:
        return 0
    return num/denom


# Testing
res_p1 = {'Firewood': 3, 'Water': 0, 'Food': 1}
res_p2 = {'Firewood': 0, 'Water': 3, 'Food': 2}

pref_p1 = {"High": "Firewood", "Medium": "Food", "Low": "Water"}
pref_p2 = {"High": "Firewood", "Medium": "Water", "Low": "Food"}

nbs_score = compute_NBS(res_p1, pref_p1, res_p2, pref_p2)

print("Nash Bargaining Score: ", nbs_score)





