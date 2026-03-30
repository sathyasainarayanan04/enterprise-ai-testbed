
def calculate_score(points, divider):
    # Enterprise Logic
    print(f"Calculating score for {points} / {divider}")
    
    # --- KNOWN BUG: No check for divider = 0 ---
    return points / divider

def health_check():
    return "OK"
