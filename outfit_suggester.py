import itertools
import random

def get_clothes():
    print("Enter your clothes for each category (comma-separated). Leave blank if none.")
    tops = input("Tops (e.g., t-shirt, blouse): ").strip().split(",") if input("Include tops? (y/n): ").lower() == 'y' else []
    bottoms = input("Bottoms (e.g., jeans, skirt): ").strip().split(",") if input("Include bottoms? (y/n): ").lower() == 'y' else []
    outers = input("Outerwear (e.g., jacket, cardigan): ").strip().split(",") if input("Include outerwear? (y/n): ").lower() == 'y' else []
    shoes = input("Shoes (e.g., sneakers, boots): ").strip().split(",") if input("Include shoes? (y/n): ").lower() == 'y' else []
    
    clothes = {
        "tops": [item.strip() for item in tops if item.strip()],
        "bottoms": [item.strip() for item in bottoms if item.strip()],
        "outers": [item.strip() for item in outers if item.strip()],
        "shoes": [item.strip() for item in shoes if item.strip()]
    }
    return clothes

def suggest_outfits(clothes, n=5):
    categories = [cat for cat, items in clothes.items() if items]
    all_items = [clothes[cat] for cat in categories]
    all_combinations = list(itertools.product(*all_items))
    if not all_combinations:
        print("Not enough clothes to suggest outfits.")
        return
    
    print(f"\nHere are {min(n, len(all_combinations))} ways to wear your clothes:")
    sampled = random.sample(all_combinations, min(n, len(all_combinations)))
    for idx, combo in enumerate(sampled, 1):
        outfit = ', '.join(combo)
        print(f"{idx}. {outfit}")

def main():
    print("Welcome to Outfit Suggester!")
    clothes = get_clothes()
    suggest_outfits(clothes)

if __name__ == "__main__":
    main()