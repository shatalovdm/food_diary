# -*- coding: utf-8 -*-
# this file is released under public domain and you can use without limitations

# -------------------------------------------------------------------------
# This is a sample controller
# - index is the default action of any application
# - user is required for authentication and authorization
# - download is for downloading files uploaded in the db (does streaming)
# -------------------------------------------------------------------------


def index():
    return dict()


def user():
    if request.args(0) == 'register':
        form = auth.register(next=URL('default', 'personalData'))
    else:
        form = auth()
    return dict(form=form)


@cache.action()
def download():
    return response.download(request, db)


def call():
    return service()

#This page allows user to fill in the form with personal information which will effect calculated nutrician goals
@auth.requires_login()
def personalData():

    #Checking if the user has already filled in the form
    row = db(db.details.created_by == auth.user_id).select().first()

    # if not, creating a new record for the user
    if not row:
        form = SQLFORM(db.details, submit_button=T('Submit'))
        form.element('input[name=height]')['_style']='width:60px;height:30px;'
        form.element('input[name=current_weight]')['_style']='width:60px;height:30px;'
        form.element('input[name=date_of_birth]')['_style']='width:106px;height:30px;'
        form.element('input[name=goal_weight]')['_style']='width:60px;height:30px;'
        form.element('input[value=Submit]')['_style']='background-color: #DA2128; color:#ffffff'

        if form.process().accepted:
            session.flash = 'form accepted'
            row = db(db.details.created_by == auth.user_id).select().first()
            protformula = round(((row.current_weight)/(2.2))*1.0)
            if row.gender == 'Female':
                if row.your_activity_level == 'Sedentary':
                    if row.diet_goal == 'Maintain current weight':
                        formula = (((4.7 * float(row.height)) + (4.35 * float(row.current_weight)) - (4.7 * float(row.age)))+655)*1.2
                        db.projected.insert(projected_calories = round(formula),protein = protformula)
                        db.commit()
                    if row.diet_goal == 'Loose weight':
                        formula = ((((4.7 * float(row.height)) + (4.35 * float(row.current_weight)) - (4.7 * float(row.age)))+655)*1.2)-500
                        db.projected.insert(projected_calories = round(formula),protein = protformula)
                        db.commit()
                    if row.diet_goal == 'Gain weight':
                        formula = ((((4.7 * float(row.height)) + (4.35 * float(row.current_weight)) - (4.7 * float(row.age)))+655)*1.2)+500
                        db.projected.insert(projected_calories = round(formula),protein = protformula)
                        db.commit()


                if row.your_activity_level == 'Low active':
                    if row.diet_goal == 'Maintain current weight':
                        formula = (((4.7 * float(row.height)) + (4.35 * float(row.current_weight)) - (4.7 * float(row.age)))+655)*1.375
                        db.projected.insert(projected_calories = round(formula),protein = protformula)
                        db.commit()
                    if row.diet_goal == 'Loose weight':
                        formula = ((((4.7 * float(row.height)) + (4.35 * float(row.current_weight)) - (4.7 * float(row.age)))+655)*1.375)-500
                        db.projected.insert(projected_calories = round(formula),protein = protformula)
                        db.commit()
                    if row.diet_goal == 'Gain weight':
                        formula = ((((4.7 * float(row.height)) + (4.35 * float(row.current_weight)) - (4.7 * float(row.age)))+655)*1.375)+400
                        db.projected.insert(projected_calories = round(formula),protein = protformula)
                        db.commit() 

                if row.your_activity_level == 'Active':
                    if row.diet_goal == 'Maintain current weight':
                        formula = (((4.7 * float(row.height)) + (4.35 * float(row.current_weight)) - (4.7 * float(row.age)))+655)*1.55
                        db.projected.insert(projected_calories = round(formula),protein = protformula)
                        db.commit()
                    if row.diet_goal == 'Loose weight':
                        formula = ((((4.7 * float(row.height)) + (4.35 * float(row.current_weight)) - (4.7 * float(row.age)))+655)*1.55)-500
                        db.projected.insert(projected_calories = round(formula),protein = protformula)
                        db.commit()
                    if row.diet_goal == 'Gain weight':
                        formula = ((((4.7 * float(row.height)) + (4.35 * float(row.current_weight)) - (4.7 * float(row.age)))+655)*1.55)+500
                        db.projected.insert(projected_calories = round(formula),protein = protformula)
                        db.commit()

                if row.your_activity_level == 'Very active':
                    if row.diet_goal == 'Maintain current weight':
                        formula = (((4.7 * float(row.height)) + (4.35 * float(row.current_weight)) - (4.7 * float(row.age)))+655)*1.725
                        db.projected.insert(projected_calories = round(formula),protein = protformula)
                        db.commit()
                    if row.diet_goal == 'Loose weight':
                        formula = ((((4.7 * float(row.height)) + (4.35 * float(row.current_weight)) - (4.7 * float(row.age)))+655)*1.725)-500
                        db.projected.insert(projected_calories = round(formula),protein = protformula)
                        db.commit()
                    if row.diet_goal == 'Gain weight':
                        formula = ((((4.7 * float(row.height)) + (4.35 * float(row.current_weight)) - (4.7 * float(row.age)))+655)*1.725)+600
                        db.projected.insert(projected_calories = round(formula),protein = protformula)
                        db.commit()


            if row.gender == 'Male':
                if row.your_activity_level == 'Sedentary':
                    if row.diet_goal == 'Maintain current weight':
                        formula = (((12.7 * float(row.height)) + (6.23 * float(row.current_weight)) - (6.8 * float(row.age)))+66)*1.2
                        db.projected.insert(projected_calories = round(formula),protein = protformula)
                        db.commit()

                    if row.diet_goal == 'Loose weight':
                        formula = ((((12.7 * float(row.height)) + (6.23 * float(row.current_weight)) - (6.8 * float(row.age)))+66)*1.2)-500
                        db.projected.insert(projected_calories = round(formula),protein = protformula)
                        db.commit()
                    if row.diet_goal == 'Gain weight':
                        formula = ((((12.7 * float(row.height)) + (6.23 * float(row.current_weight)) - (6.8 * float(row.age)))+66)*1.2)+500
                        db.projected.insert(projected_calories = round(formula),protein = protformula)
                        db.commit()


                if row.your_activity_level == 'Low active':
                    if row.diet_goal == 'Maintain current weight':
                        formula = (((12.7 * float(row.height)) + (6.23 * float(row.current_weight)) - (6.8 * float(row.age)))+66)*1.375
                        db.projected.insert(projected_calories = round(formula),protein = protformula)
                        db.commit()
                    if row.diet_goal == 'Loose weight':
                        formula = ((((12.7 * float(row.height)) + (6.23 * float(row.current_weight)) - (6.8 * float(row.age)))+66)*1.375)-500
                        db.projected.insert(projected_calories = round(formula),protein = protformula)
                        db.commit()
                    if row.diet_goal == 'Gain weight':
                        formula = ((((12.7 * float(row.height)) + (6.23 * float(row.current_weight)) - (6.8 * float(row.age)))+66)*1.375)+400
                        db.projected.insert(projected_calories = round(formula),protein = protformula)
                        db.commit() 

                if row.your_activity_level == 'Active':
                    if row.diet_goal == 'Maintain current weight':
                        formula = (((12.7 * float(row.height)) + (6.23 * float(row.current_weight)) - (6.8 * float(row.age)))+66)*1.55
                        db.projected.insert(projected_calories = round(formula),protein = protformula)
                        db.commit()
                    if row.diet_goal == 'Loose weight':
                        formula = ((((12.7 * float(row.height)) + (6.23 * float(row.current_weight)) - (6.8 * float(row.age)))+66)*1.55)-500
                        db.projected.insert(projected_calories = round(formula),protein = protformula)
                        db.commit()
                    if row.diet_goal == 'Gain weight':
                        formula = ((((12.7 * float(row.height)) + (6.23 * float(row.current_weight)) - (6.8 * float(row.age)))+66)*1.55)+500
                        db.projected.insert(projected_calories = round(formula),protein = protformula)
                        db.commit()

                if row.your_activity_level == 'Very active':
                    if row.diet_goal == 'Maintain current weight':
                        formula = (((12.7 * float(row.height)) + (6.23 * float(row.current_weight)) - (6.8 * float(row.age)))+66)*1.725
                        db.projected.insert(projected_calories = round(formula),protein = protformula)
                        db.commit()
                    if row.diet_goal == 'Loose weight':
                        formula = ((((12.7 * float(row.height)) + (6.23 * float(row.current_weight)) - (6.8 * float(row.age)))+66)*1.725)-500
                        db.projected.insert(projected_calories = round(formula),protein = protformula)
                        db.commit()
                    if row.diet_goal == 'Gain weight':
                        formula = ((((12.7 * float(row.height)) + (6.23 * float(row.current_weight)) - (6.8 * float(row.age)))+66)*1.725)+600
                        db.projected.insert(projected_calories = round(formula),protein = protformula)
                        db.commit()

            redirect(URL('suggested_goals'))
        elif form.errors:
            response.flash = 'form has errors'
        else:
            response.flash = 'please fill in the form'
            
    # if yes, updating information about the user
    if row:
        form = SQLFORM(db.details, row.id, submit_button=T('Submit'))
        form.element('input[name=height]')['_style']='width:80px;height:30px;'
        form.element('input[name=current_weight]')['_style']='width:80px;height:30px;'
        form.element('input[name=date_of_birth]')['_style']='width:106px;height:30px;'
        form.element('input[name=goal_weight]')['_style']='width:80px;height:30px;'
        form.element('input[value=Submit]')['_style']='background-color: #DA2128; color:#ffffff'
        if form.process().accepted:
            session.flash = 'form accepted'
            proj = db(db.projected.id == row.id).select().first()
            protformula = round(((row.current_weight)/(2.2))*1.0)
            if row.gender == 'Female':
                if row.your_activity_level == 'Sedentary':
                    if row.diet_goal == 'Maintain current weight':
                        formula = (((4.7 * float(row.height)) + (4.35 * float(row.current_weight)) - (4.7 * float(row.age)))+655)*1.2
                        proj.update_record(projected_calories = round(formula),protein = protformula)
                    if row.diet_goal == 'Loose weight':
                        formula = ((((4.7 * float(row.height)) + (4.35 * float(row.current_weight)) - (4.7 * float(row.age)))+655)*1.2)-500
                        proj.update_record(projected_calories = round(formula),protein = protformula)
                        
                    if row.diet_goal == 'Gain weight':
                        formula = ((((4.7 * float(row.height)) + (4.35 * float(row.current_weight)) - (4.7 * float(row.age)))+655)*1.2)+500
                        proj.update_record(projected_calories = round(formula),protein = protformula)
       


                if row.your_activity_level == 'Low active':
                    if row.diet_goal == 'Maintain current weight':
                        formula = (((4.7 * float(row.height)) + (4.35 * float(row.current_weight)) - (4.7 * float(row.age)))+655)*1.375
                        proj.update_record(projected_calories = round(formula),protein = protformula)
                
                    if row.diet_goal == 'Loose weight':
                        formula = ((((4.7 * float(row.height)) + (4.35 * float(row.current_weight)) - (4.7 * float(row.age)))+655)*1.375)-500
                        proj.update_record(projected_calories = round(formula),protein = protformula)
                  
                    if row.diet_goal == 'Gain weight':
                        formula = ((((4.7 * float(row.height)) + (4.35 * float(row.current_weight)) - (4.7 * float(row.age)))+655)*1.375)+400
                        proj.update_record(projected_calories = round(formula),protein = protformula)


                if row.your_activity_level == 'Active':
                    if row.diet_goal == 'Maintain current weight':
                        formula = (((4.7 * float(row.height)) + (4.35 * float(row.current_weight)) - (4.7 * float(row.age)))+655)*1.55
                        proj.update_record(projected_calories = round(formula),protein = protformula)

                    if row.diet_goal == 'Loose weight':
                        formula = ((((4.7 * float(row.height)) + (4.35 * float(row.current_weight)) - (4.7 * float(row.age)))+655)*1.55)-500
                        proj.update_record(projected_calories = round(formula),protein = protformula)

                    if row.diet_goal == 'Gain weight':
                        formula = ((((4.7 * float(row.height)) + (4.35 * float(row.current_weight)) - (4.7 * float(row.age)))+655)*1.55)+500
                        proj.update_record(projected_calories = round(formula),protein = protformula)


                if row.your_activity_level == 'Very active':
                    if row.diet_goal == 'Maintain current weight':
                        formula = (((4.7 * float(row.height)) + (4.35 * float(row.current_weight)) - (4.7 * float(row.age)))+655)*1.725
                        proj.update_record(projected_calories = round(formula),protein = protformula)

                    if row.diet_goal == 'Loose weight':
                        formula = ((((4.7 * float(row.height)) + (4.35 * float(row.current_weight)) - (4.7 * float(row.age)))+655)*1.725)-500
                        proj.update_record(projected_calories = round(formula),protein = protformula)

                    if row.diet_goal == 'Gain weight':
                        formula = ((((4.7 * float(row.height)) + (4.35 * float(row.current_weight)) - (4.7 * float(row.age)))+655)*1.725)+600
                        proj.update_record(projected_calories = round(formula),protein = protformula)



            if row.gender == 'Male':
                if row.your_activity_level == 'Sedentary':
                    if row.diet_goal == 'Maintain current weight':
                        formula = (((12.7 * float(row.height)) + (6.23 * float(row.current_weight)) - (6.8 * float(row.age)))+66)*1.2
                        proj.update_record(projected_calories = round(formula),protein = protformula)


                    if row.diet_goal == 'Loose weight':
                        formula = ((((12.7 * float(row.height)) + (6.23 * float(row.current_weight)) - (6.8 * float(row.age)))+66)*1.2)-500
                        proj.update_record(projected_calories = round(formula),protein = protformula)

                    if row.diet_goal == 'Gain weight':
                        formula = ((((12.7 * float(row.height)) + (6.23 * float(row.current_weight)) - (6.8 * float(row.age)))+66)*1.2)+500
                        proj.update_record(projected_calories = round(formula),protein = protformula)



                if row.your_activity_level == 'Low active':
                    if row.diet_goal == 'Maintain current weight':
                        formula = (((12.7 * float(row.height)) + (6.23 * float(row.current_weight)) - (6.8 * float(row.age)))+66)*1.375
                        proj.update_record(projected_calories = round(formula),protein = protformula)

                    if row.diet_goal == 'Loose weight':
                        formula = ((((12.7 * float(row.height)) + (6.23 * float(row.current_weight)) - (6.8 * float(row.age)))+66)*1.375)-500
                        proj.update_record(projected_calories = round(formula),protein = protformula)

                    if row.diet_goal == 'Gain weight':
                        formula = ((((12.7 * float(row.height)) + (6.23 * float(row.current_weight)) - (6.8 * float(row.age)))+66)*1.375)+400
                        proj.update_record(projected_calories = round(formula),protein = protformula)


                if row.your_activity_level == 'Active':
                    if row.diet_goal == 'Maintain current weight':
                        formula = (((12.7 * float(row.height)) + (6.23 * float(row.current_weight)) - (6.8 * float(row.age)))+66)*1.55
                        proj.update_record(projected_calories = round(formula),protein = protformula)

                    if row.diet_goal == 'Loose weight':
                        formula = ((((12.7 * float(row.height)) + (6.23 * float(row.current_weight)) - (6.8 * float(row.age)))+66)*1.55)-500
                        proj.update_record(projected_calories = round(formula),protein = protformula)

                    if row.diet_goal == 'Gain weight':
                        formula = ((((12.7 * float(row.height)) + (6.23 * float(row.current_weight)) - (6.8 * float(row.age)))+66)*1.55)+500
                        proj.update_record(projected_calories = round(formula),protein = protformula)


                if row.your_activity_level == 'Very active':
                    if row.diet_goal == 'Maintain current weight':
                        formula = (((12.7 * float(row.height)) + (6.23 * float(row.current_weight)) - (6.8 * float(row.age)))+66)*1.725
                        proj.update_record(projected_calories = round(formula),protein = protformula)

                    if row.diet_goal == 'Loose weight':
                        formula = ((((12.7 * float(row.height)) + (6.23 * float(row.current_weight)) - (6.8 * float(row.age)))+66)*1.725)-500
                        proj.update_record(projected_calories = round(formula),protein = protformula)

                    if row.diet_goal == 'Gain weight':
                        formula = ((((12.7 * float(row.height)) + (6.23 * float(row.current_weight)) - (6.8 * float(row.age)))+66)*1.725)+600
                        proj.update_record(projected_calories = round(formula),protein = protformula)


            redirect(URL('suggested_goals'))
        elif form.errors:
            response.flash = 'form has errors'
        else:
            response.flash = 'please fill in the form'
    return dict(form=form)

# This page summarizes user's daily nutrition goals
@auth.requires_login()
def suggested_goals():
    row = db(db.projected.created_by == auth.user.id).select().first()
    return dict(row = row)

# This is user's personal food diary
@auth.requires_login()
def diary():
    
    diary_date = None
    result_breakfast = []
    result_lunch = []
    result_dinner = []
    result_snack = []
    calories_sum = 0
    protein_sum = 0
    fat_sum = 0
    carbs_sum = 0
    
    #Deleting a specific row
    if request.vars.delete:
        row = db(db.diary.id==request.vars.delete).delete()
        db.commit()
        redirect(URL('default', 'diary', vars=dict(current_date=session.date)))
    
    #Working with a diary date
    from datetime import date
    if request.vars.current_date == None:
        diary_date = date.today()
    else:
        diary_date = request.vars.current_date
    session.date = diary_date
    
    #Getting goal values for current user
    goals = db(db.projected.created_by == auth.user_id).select().first()
    
    #Getting diary for current user
    rows = db(db.diary.created_by == auth.user_id)
    results = rows(db.diary.today == diary_date).select()
    for row in results:
        calories_sum += row.calories
        protein_sum += row.protein
        fat_sum += row.fat
        carbs_sum += row.carbs
        if row.meal == 'breakfast':
            result_breakfast.append(row)
        if row.meal == 'lunch':
            result_lunch.append(row)
        if row.meal == 'dinner':
            result_dinner.append(row)
        if row.meal == 'snack':
            result_snack.append(row)
            
    return dict(diary_date=diary_date, result_breakfast=result_breakfast, result_lunch=result_lunch, result_dinner=result_dinner, result_snack=result_snack, calories_sum=calories_sum, protein_sum=protein_sum, fat_sum=fat_sum, carbs_sum=carbs_sum, goals=goals)

def search_food():
    found = None
    if request.vars.name:
        found = db(db.food_data.name==request.vars.name).select().first()
    return found

# This page allows user to search for the food item in the database
@auth.requires_login()
def search():
    found = search_food()
    scale = None
    form = FORM(INPUT(_name='name', _id="name", _style="width: 400px; height:50px", _autocomplete="off", _placeholder="Start typing...", requires=IS_NOT_EMPTY()), INPUT(_type='submit', _style="height:50px; background-color: #DA2128; color:#ffffff" ))
    if found != None:
        session.found = found
    if request.args[0]:
        if request.args[0] == "s":
            session.submit = None
    if request.vars.submit:
        session.submit = request.vars.submit
    if request.vars.new_item:
        redirect(URL('default', 'create'))
    
    # Calculating the weight of the food item depending on user's input
    if request.vars.weight:
        if request.vars.weight == str(session.found.weight1):
            scale = int(request.vars.quantity) * session.found.weight1
        if request.vars.weight == str(session.found.weight2):
            scale = int(request.vars.quantity) * float(session.found.weight2)
        if request.vars.weight == "1":
            scale = int(request.vars.quantity) * 100
    
    #Adding the found food item into the diary
    if request.vars.add:
        if session.submit == 'breakfast':
            db.diary.insert(meal = 'breakfast',
                        today = session.date,
                        food_item = session.found.name.replace('.', ' '),
                        calories= round((scale * session.found.calories)/100),
                        carbs = round((scale * session.found.carbs)/100),
                        fat = round((scale * session.found.total_fat)/100),
                        protein = round((scale * session.found.protein)/100))
            db.commit()
        if session.submit == 'lunch':
            db.diary.insert(meal = 'lunch',
                        today = session.date,
                        food_item = session.found.name.replace('.', ' '),
                        calories= round((scale * session.found.calories)/100),
                        carbs = round((scale * session.found.carbs)/100),
                        fat = round((scale * session.found.total_fat)/100),
                        protein = round((scale * session.found.protein)/100))
            db.commit()
        if session.submit == 'dinner':
            db.diary.insert(meal = 'dinner',
                        today = session.date,
                        food_item = session.found.name.replace('.', ' '),
                        calories= round((scale * session.found.calories)/100),
                        carbs = round((scale * session.found.carbs)/100),
                        fat = round((scale * session.found.total_fat)/100),
                        protein = round((scale * session.found.protein)/100))
            db.commit()
        if session.submit == 'snack':
            db.diary.insert(meal = 'snack',
                        today = session.date,
                        food_item = session.found.name.replace('.', ' '),
                        calories= round((scale * session.found.calories)/100),
                        carbs = round((scale * session.found.carbs)/100),
                        fat = round((scale * session.found.total_fat)/100),
                        protein = round((scale * session.found.protein)/100))
            db.commit()
        session.submit = None
    return dict(found=found, form=form)

# This page allows user to create a new food item and add it into the database
@auth.requires_login()
def create():
    form = SQLFORM(db.food_data,submit_button=T('Submit'))
    form.element('input[value=Submit]')['_style']='background-color: #DA2128; color:#ffffff'
    if form.process().accepted:
         response.flash="form accepted"
         redirect(URL('default', 'search'))
    return dict(form=form)

def search_selector():
    if not request.vars.name:
        return 'Not found'
    selected = []
    for row in db(db.food_data.name.contains(request.vars.name)).select():
        if len(selected) <50:
            selected.append(row.name)
        else:
            break
    return ''.join([DIV(k,
                 _onclick="jQuery('#name').val('%s')" % k,
                 _onmouseover="this.style.backgroundColor='lightblue'",
                 _onmouseout="this.style.backgroundColor='white'"
                 ).xml() for k in selected])
