def mainFilter(d,co,cu,t):
    diet=d
    course=co
    cuisine=cu
    time=t
    import pandas as pd
    import urllib.request
    from urllib.parse import urlparse
    from bs4 import BeautifulSoup
    df = pd.read_csv('D:\Programming\Django\FoodAdvicer\IndianFoodDatasetSuperFakeCSV.csv')
    if(diet=="Any"):
        pass
    elif(diet=="Vegetarian"):
        df = df[df.Diet == "Vegetarian"]
    elif(diet=="High Protein Vegetarian"):
        df = df[df.Diet == "High Protein Vegetarian"]
    elif(diet=="Non Vegeterian"):
        df = df[df.Diet == "Non Vegeterian"]
    elif(diet=="Eggetarian"):
        df = df[df.Diet == "Eggetarian"]
    elif(diet=="Diabetic Friendly"):
        df = df[df.Diet == "Diabetic Friendly"]
    elif(diet=="High Protein Non Vegetarian"):
        df = df[df.Diet == "High Protein Non Vegetarian"]
    #elif(diet=="Gluten Free or Sugar Free"):
    #    df = df[(df.Diet == "Gluten Free") or (df.Diet == "Sugar Free Diet" or df.Diet == "Diabetic Friendly")]
    elif(diet=="No Onion No Garlic (Sattvic)"):
        df = df[df.Diet == "No Onion No Garlic (Sattvic)"]
    elif(diet=="Vegan"):
        df = df[df.Diet == "Vegan"]
    elif(diet=="Gluten Free"):
        df = df[df.Diet == "Gluten Free"]
    elif(diet=="Sugar Free Diet"):
        df = df[df.Diet == "Sugar Free Diet"]
    if(course=="Any"):
        pass
    elif(course=="Lunch"):
        df = df[df.Course == "Lunch"]
    elif(course=="Side Dish"):
        df = df[df.Course == "Side Dish"]
    elif(course=="Snack"):
        df = df[df.Course == "Snack"]
    elif(course=="Dinner"):
        df = df[df.Course == "Dinner"]
    elif(course=="Dessert"):
        df = df[df.Course == "Dessert"]
    elif(course=="Appetizer"):
        df = df[df.Course == "Appetizer"]
    elif(course=="Main Course"):
        df = df[df.Course == "Main Course"]
    elif(course=="South Indian Breakfast"):
        df = df[df.Course == "South Indian Breakfast"]
    elif(course=="World Breakfast"):
        df = df[df.Course == "World Breakfast"]
    elif(course=="North Indian Breakfast"):
        df = df[df.Course == "North Indian Breakfast"]
    elif(course=="Indian Breakfast"):
        df = df[df.Course == "Indian Breakfast"]
    if(cuisine=="Any"):
        pass
    elif(cuisine=="Indian"):
        df = df[df.Cuisine == "Indian"]
    elif(cuisine=="Continental"):
        df = df[df.Cuisine == "Continental"]
    elif(cuisine=="North Indian Recipes"):
        df = df[df.Cuisine == "North Indian Recipes"]
    elif(cuisine=="South Indian Recipes"):
        df = df[df.Cuisine == "South Indian Recipes"]
    elif(cuisine=="Italian Recipes"):
        df = df[df.Cuisine == "Italian Recipes"]
    elif(cuisine=="Bengali Recipes"):
        df = df[df.Cuisine == "Bengali Recipes"]
    elif(cuisine=="Maharashtrian Recipes"):
        df = df[df.Cuisine == "Maharashtrian Recipes"]
    elif(cuisine=="Kerala Recipes"):
        df = df[df.Cuisine == "Kerala Recipes"]
    elif(cuisine=="Tamil Nadu"):
        df = df[df.Cuisine == "Tamil Nadu"]
    elif(cuisine=="Karnataka"):
        df = df[df.Cuisine == "Karnataka"]
    elif(cuisine=="Fusion"):
        df = df[df.Cuisine == "Fusion"]
    elif(cuisine=="Rajasthani"):
        df = df[df.Cuisine == "Rajasthani"]
    elif(cuisine=="Mexican"):
        df = df[df.Cuisine == "Mexican"]
    elif(cuisine=="Andhra"):
        df = df[df.Cuisine == "Andhra"]
    elif(cuisine=="Gujarati Recipes"):
        df = df[df.Cuisine == "Gujarati Recipes"]
    elif(cuisine=="Goan Recipes"):
        df = df[df.Cuisine == "Goan Recipes"]
    elif(cuisine=="Punjabi"):
        df = df[df.Cuisine == "Punjabi"]
    elif(cuisine=="Chettinad"):
        df = df[df.Cuisine == "Chettinad"]
    elif(cuisine=="Asian"):
        df = df[df.Cuisine == "Asian"]
    elif(cuisine=="Thai"):
        df = df[df.Cuisine == "Thai"]
    elif(cuisine=="Chinese"):
        df = df[df.Cuisine == "Chinese"]
    if(time=="Any"):
        pass
    elif(time=="Under30"):
        df = df[df.TotalTimeInMins <= 30]
    elif(time=="Under60"):
        df = df[df.TotalTimeInMins <= 60]
    elif(time=="Under120"):
        df = df[df.TotalTimeInMins <= 120]
    #df.drop(['Srno','RecipeName', 'Ingredients', 'TranslatedIngredients', 'PrepTimeInMins', 'CookTimeInMins', 'TotalTimeInMins', 'Servings', 'Cuisine','Course','Diet','Instructions','TranslatedInstructions'], axis=1, inplace=True)
    z=df.values.tolist()
    return z

def receipeShower(id):
    foodid=id
    import pandas as pd
    df = pd.read_csv('D:\Programming\Django\FoodAdvicer\IndianFoodDatasetSuperFakeCSV.csv')
    df=df[df.Srno==int(foodid)]
    y=df.values.tolist()
    return y
