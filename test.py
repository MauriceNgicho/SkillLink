from models.base_model import BaseModel
import models

# Step 1: Create an object
obj = BaseModel()
print("Created Object:", obj)

# Step 2: Save to FileStorage
obj.save()
print("\nObject Saved! Check 'file.json'.")

# Step 3: Reload saved objects
models.storage.reload()
print("\nReloading objects from 'file.json'...\n")

# Step 4: Print all objects
all_objects = models.storage.all()
print("All Stored Objects:\n", all_objects)


#<!DOCTYPE html>
#<html lang="en">
#<head>
 #   <meta charset="UTF-8">
  #  <meta name="viewport" content="width=device-width, initial-scale=1.0">
   # <title>SkillLink - Home</title>
#    <link rel="stylesheet" href="{{ url_for('static', filename='styles.css') }}">
#</head>
#<body>
 #   <header>
  #      <h1>Welcome to SkillLink</h1>
   #     <nav>
    #        <ul>
     #           <li><a href="{{ url_for('main.courses') }}">Courses</a></li>
      #          <li><a href="{{ url_for('auth.login') }}">Login</a></li>
       #     </ul>
#        </nav>
 #   </header>
  #  <section>
   #     <h2>Learn and Grow with SkillLink</h2>
    #    <p>Access a variety of courses designed to boost you skills.</p>
     #   <a href="{{ url_for('main.courses') }}" class="btn">Explore Courses</a>
    #</section>
    
#</body>
#</html>