# Dhanesh kumar 
# 2045141

def get_age():

    age = int(input())

    if (age >= 18 and age <= 75):
        return age

    else:
        raise ValueError("Invalid age.")

def fat_burning_heart_rate(age):
    return (0.7 * (220 - age))

if __name__ == '__main__':
    try:
        age = get_age()

        print("Fat burning heart rate for a", age, "year-old:", fat_burning_heart_rate(age), "bpm")
    except ValueError as ve:
        print(f"{ve.args[0]}\nCould not calculate heart rate info.\n")