init -2:
    python:

        def get_random_from_list(list):
            if len(list) > 0:
                return list[renpy.random.randint(0,len(list)-1)]
            else:
                return None

        def get_random_from_weighted_list(list): #Passed a list of parameters which are ["Thing", weighted value]
            if len(list) == 0:
                return None

            total_value = 0
            for item in list:
                total_value += item[1] #Get the total weighting value that we use to determine what thing we've picked.

            random_value = renpy.random.randint(0,total_value) #Gets us a value somewhere inside of our probability space.
            running_total = 0
            for item in list:
                if random_value <= (item[1]+running_total):
                    return item[0]
                else:
                    running_total += item[1]

        list_of_names = []

        list_of_names.append("Jessica")
        list_of_names.append("Jenny")
        list_of_names.append("Victoria")
        list_of_names.append("Lily")
        list_of_names.append("Jennifer")
        list_of_names.append("Nora")
        list_of_names.append("Stephanie")
        list_of_names.append("Alexia")
        list_of_names.append("Danielle")
        list_of_names.append("Ashley")
        list_of_names.append("Brittany")
        list_of_names.append("Sally")
        list_of_names.append("Helen")
        list_of_names.append("Sarah")
        list_of_names.append("Erika")
        list_of_names.append("Sandra")
        list_of_names.append("Maya")
        list_of_names.append("Emma")
        list_of_names.append("Katya")
        list_of_names.append("Saphirette")
        list_of_names.append("Charisma")
        list_of_names.append("Mayumi")
        list_of_names.append("Brendan")
        list_of_names.append("Jose")
        list_of_names.append("Saya")
        list_of_names.append("Yamiko")
        list_of_names.append("Rowena")
        list_of_names.append("Katie")
        list_of_names.append("Dawn")
        list_of_names.append("Sasha")
        list_of_names.append("Melanie")
        list_of_names.append("Tina")
        list_of_names.append("Raven")
        list_of_names.append("Sarah")
        list_of_names.append("Antonia")
        list_of_names.append("Mina")
        list_of_names.append("Marisha")
        list_of_names.append("Misty")
        list_of_names.append("Krya")
        list_of_names.append("Kida")
        list_of_names.append("Miyu")
        list_of_names.append("Rayne")
        list_of_names.append("Joana")
        list_of_names.append("Bobbi")
        list_of_names.append("Moira")
        list_of_names.append("Penelope")
        list_of_names.append("Julie")
        list_of_names.append("Geneviève")
        list_of_names.append("Persephone")
        list_of_names.append("Kyle")
        list_of_names.append("Alice")
        list_of_names.append("Ginger")
        list_of_names.append("Shirley")
        list_of_names.append("Alicia")
        list_of_names.append("Arianne")
        list_of_names.append("Roxy")
        list_of_names.append("Sheyla")
        list_of_names.append("Candice")
        list_of_names.append("Becky")
        list_of_names.append("Susan")
        list_of_names.append("Kirsten")
        list_of_names.append("Sylvia")
        list_of_names.append("Niamh")
        list_of_names.append("Teagan")
        list_of_names.append("Robin")
        list_of_names.append("Mara")
        list_of_names.append("Veronica")
        list_of_names.append("Misa")
        list_of_names.append("Kerri")
        list_of_names.append("Marianne")
        list_of_names.append("Marry-Ann")
        list_of_names.append("Angela")
        list_of_names.append("June")
        list_of_names.append("Angie")
        list_of_names.append("Gillian")
        list_of_names.append("Faith")
        list_of_names.append("Julia")


        def get_random_name():
            return get_random_from_list(list_of_names)

        list_of_last_names = []
        list_of_last_names.append("Hitchcock")
        list_of_last_names.append("Peters")
        list_of_last_names.append("Fallbrooke")
        list_of_last_names.append("Williams")
        list_of_last_names.append("Orion")
        list_of_last_names.append("Marie")
        list_of_last_names.append("Millstein")
        list_of_last_names.append("Sky")
        list_of_last_names.append("Spherica")
        list_of_last_names.append("Fields")
        list_of_last_names.append("Moran")
        list_of_last_names.append("Kurokami")
        list_of_last_names.append("Bergstrom")
        list_of_last_names.append("Fernandez")
        list_of_last_names.append("Bergstrom")
        list_of_last_names.append("Sasamiya")
        list_of_last_names.append("Onihime")
        list_of_last_names.append("Lancie")
        list_of_last_names.append("Simmons")
        list_of_last_names.append("Parsons")
        list_of_last_names.append("Lockheart")
        list_of_last_names.append("Summers")
        list_of_last_names.append("Seras")
        list_of_last_names.append("Proud")
        list_of_last_names.append("Blanes")
        list_of_last_names.append("Shaw")
        list_of_last_names.append("Bailey")
        list_of_last_names.append("Daniels")
        list_of_last_names.append("Castillo")
        list_of_last_names.append("Kimiko")
        list_of_last_names.append("Farrowsdotter")
        list_of_last_names.append("Prashad")
        list_of_last_names.append("Pharys")
        list_of_last_names.append("Pires")
        list_of_last_names.append("Brock")
        list_of_last_names.append("Kingsley")
        list_of_last_names.append("Navarias")
        list_of_last_names.append("LaPorte")
        list_of_last_names.append("Isabella")
        list_of_last_names.append("Hamilton")
        list_of_last_names.append("Hellene")
        list_of_last_names.append("Belladonna")
        list_of_last_names.append("Vedeer")
        list_of_last_names.append("Currance")
        list_of_last_names.append("Murray")
        list_of_last_names.append("Silvers")
        list_of_last_names.append("Vermelen")
        list_of_last_names.append("Blair")
        list_of_last_names.append("Rojas")
        list_of_last_names.append("Reichart")
        list_of_last_names.append("Swift")
        list_of_last_names.append("Carroll")
        list_of_last_names.append("Maugher")
        list_of_last_names.append("Moonstone")
        list_of_last_names.append("Kirk")
        list_of_last_names.append("Deal")
        list_of_last_names.append("Quinn")
        list_of_last_names.append("Jade")
        list_of_last_names.append("Smythe")
        list_of_last_names.append("Rose")
        list_of_last_names.append("Chanen")
        list_of_last_names.append("Pesche")
        list_of_last_names.append("Lighton")
        list_of_last_names.append("Michaelson")
        list_of_last_names.append("Anderson")
        list_of_last_names.append("Connors")
        list_of_last_names.append("Song")


        def get_random_last_name():
            return get_random_from_list(list_of_last_names)


        list_of_male_names = []
        list_of_male_names.append("Aaron")
        list_of_male_names.append("Andre")
        list_of_male_names.append("Bradley")
        list_of_male_names.append("Colin")
        list_of_male_names.append("Dustin")
        list_of_male_names.append("Erwin")
        list_of_male_names.append("Felix")
        list_of_male_names.append("Glenn")
        list_of_male_names.append("Harold")
        list_of_male_names.append("Ivan")
        list_of_male_names.append("Jake")
        list_of_male_names.append("Jon")
        list_of_male_names.append("Julian")
        list_of_male_names.append("Kurt")
        list_of_male_names.append("Kim")
        list_of_male_names.append("Lowell")
        list_of_male_names.append("Maxwell")
        list_of_male_names.append("Morton")
        list_of_male_names.append("Neil")
        list_of_male_names.append("Omar")
        list_of_male_names.append("Peter")
        list_of_male_names.append("Raul")
        list_of_male_names.append("Rudy")
        list_of_male_names.append("Steve")
        list_of_male_names.append("Stuart")
        list_of_male_names.append("Terrence")
        list_of_male_names.append("Tyrone")
        list_of_male_names.append("Vincent")
        list_of_male_names.append("Wilbur")
        list_of_male_names.append("William")
        list_of_male_names.append("Zachary")

        def get_random_male_name():
            return get_random_from_list(list_of_male_names)

        list_of_hairs = []
        list_of_hairs.append("blond")
        list_of_hairs.append("brown")
        list_of_hairs.append("black")
        list_of_hairs.append("red")

        def get_random_hair_colour():
            return get_random_from_list(list_of_hairs)

        list_of_skins = []
        list_of_skins.append(["white",5])
        list_of_skins.append(["black",1])
        list_of_skins.append(["tan",2])

        def get_random_skin():
            return get_random_from_weighted_list(list_of_skins)

        list_of_faces = []
        list_of_faces.append("Face_1")
        list_of_faces.append("Face_2")
        list_of_faces.append("Face_3")
        list_of_faces.append("Face_4")
        list_of_faces.append("Face_5")
        list_of_faces.append("Face_6")

        def get_random_face():
            return get_random_from_list(list_of_faces)

        list_of_eyes = []
        list_of_eyes.append("blue")
        list_of_eyes.append("green")
        list_of_eyes.append("brown")
        list_of_eyes.append("grey")

        def get_random_eye():
            return get_random_from_list(list_of_eyes)

        list_of_tits = []
        list_of_tits.append(["AA",5])
        list_of_tits.append(["A",15])
        list_of_tits.append(["B",30])
        list_of_tits.append(["C",30])
        list_of_tits.append(["D",15])
        list_of_tits.append(["DD",10])
        list_of_tits.append(["DDD",5])
        list_of_tits.append(["E",2])
        list_of_tits.append(["F",1])
        list_of_tits.append(["FF",1])

        def get_random_tit():
            return get_random_from_weighted_list(list_of_tits)

        def get_smaller_tits(current_tits):
            for tits in list_of_tits:
                if current_tits == tits[0]:
                    current_index = list_of_tits.index(tits)
            if current_index > 0: #If they are not min size.
                return list_of_tits[current_index-1][0]
            else:
                return current_tits

        def get_larger_tits(current_tits):
            for tits in list_of_tits:
                if current_tits == tits[0]: #Needed to account for the fact that this is now a 3d array.
                    current_index = list_of_tits.index(tits)
            if current_index < len(list_of_tits)-1: #If they are not max size, get the next index up.
                return list_of_tits[current_index+1][0]
            else:
                return current_tits #This is as large as they can get on our current chart.

        list_of_jobs = []
        list_of_jobs.append("scientist")
        list_of_jobs.append("secretary")
        list_of_jobs.append("PR representative")
        list_of_jobs.append("sales person")

        def get_random_job():
            return get_random_from_list(list_of_jobs)

        list_of_body_types = []
        list_of_body_types.append("thin_body")
        list_of_body_types.append("standard_body")
        list_of_body_types.append("curvy_body")

        def get_random_body_type():
            return get_random_from_list(list_of_body_types)

        technobabble_list = []
        technobabble_list.append("optimize the electromagnetic pathways")
        technobabble_list.append("correct for the nanowave signature")
        technobabble_list.append("de-scramble the thermal injector")
        technobabble_list.append("crosslink the long chain polycarbons")
        technobabble_list.append("carbonate the ethyl groups")
        technobabble_list.append("oxdize the functional group")
        technobabble_list.append("resynchronize the autosequencers")
        technobabble_list.append("invert the final power spike")
        technobabble_list.append("kickstart the process a half second early")
        technobabble_list.append("stall the process by a half second")
        technobabble_list.append("apply a small machine learning algorithm")
        technobabble_list.append("hit the thing in just the right spot")
        technobabble_list.append("wait patiently for it to finish")



        coffee_list = []
        coffee_list.append("just black")
        coffee_list.append("one milk")
        coffee_list.append("two milk")
        coffee_list.append("cream and sugar")
        coffee_list.append("just a splash of cream")
        coffee_list.append("lots of sugar")
        coffee_list.append("just a little sugar")

        def get_random_coffee_style():
            return get_random_from_list(coffee_list)

        # Regular opinions _usually_ add a bit of bonus happiness, but some may influence some options or effects.
        opinions_list = [] #A master list of things a character might like or dislike. Should always be named so it fits the framework "Likes X" or "Dislikes X". Personalities have a unique list that they always draw from as well
        opinions_list.append("skirts")
        opinions_list.append("pants")
        opinions_list.append("small talk") #Has gameplay effect.
        opinions_list.append("Mondays") #Has gameplay effect
        opinions_list.append("Fridays") #Has gameplay effect
        opinions_list.append("the weekend") #Has gameplay effect
        opinions_list.append("working") #Has gameplay effect
        opinions_list.append("the colour blue")
        opinions_list.append("the colour yellow")
        opinions_list.append("the colour red")
        opinions_list.append("the colour pink")
        opinions_list.append("conservative outfits") #Has gameplay effect
        opinions_list.append("work uniforms") #Has gameplay effect
        opinions_list.append("research work") #Has gameplay effect
        opinions_list.append("marketing work") #Has gameplay effect
        opinions_list.append("HR work") #Has gameplay effect
        opinions_list.append("supply work") #Has gameplay effect
        opinions_list.append("production work") #Has gameplay effect
        opinions_list.append("makeup")
        opinions_list.append("flirting") #Has gameplay effect
        opinions_list.append("sports") #Has gameplay effect
        opinions_list.append("hiking") #Hsa gameplay effect

        def get_random_opinion():
            return get_random_from_list(opinions_list)

        # Sexy opinions _usually_ add a bit of bonus sluttiness, but some may influence some sex scenes, make some approaches more likely, or have other effects.
        sexy_opinions_list = [] #Another list of opinions, but these ones are sex/kink related and probably shoudn't be brought up in polite conversation.
        sexy_opinions_list.append("doggy style sex") #Has gameplay effect
        sexy_opinions_list.append("missionary style sex") #Has gameplay effect
        sexy_opinions_list.append("sex standing up") #Has gameplay effect
        sexy_opinions_list.append("giving blowjobs") #Has gameplay effect
        sexy_opinions_list.append("getting head")
        sexy_opinions_list.append("anal sex")
        sexy_opinions_list.append("vaginal sex") #Has gameplay effect
        sexy_opinions_list.append("public sex") #Has gameplay effect
        sexy_opinions_list.append("kissing") #Has gameplay effect
        sexy_opinions_list.append("lingerie") #Has gameplay effect
        sexy_opinions_list.append("masturbating") #Has gameplaye effect
        sexy_opinions_list.append("giving handjobs")
        sexy_opinions_list.append("being fingered")
        sexy_opinions_list.append("skimpy uniforms") #Has gameplay effect
        sexy_opinions_list.append("skimpy outfits") #Has gameplay effect
        sexy_opinions_list.append("not wearing underwear") #Has gameplay effect
        sexy_opinions_list.append("not wearing anything") #Has gameplay effect
        sexy_opinions_list.append("showing her tits") #Has gameplay effect
        sexy_opinions_list.append("showing her ass") #Has gameplay effect
        sexy_opinions_list.append("being submissive") #Has gameplay effect
        sexy_opinions_list.append("taking control") #Has gameplay effect
        sexy_opinions_list.append("drinking cum") #Has gameplay effect
        sexy_opinions_list.append("creampies") #Has gameplay effect
        sexy_opinions_list.append("cum facials") #Has gameplay effect
        sexy_opinions_list.append("being covered in cum") #Has gameplay effect
        sexy_opinions_list.append("risking getting pregnant") #Has TEMPORARY gameplay effect
        sexy_opinions_list.append("big dicks")

        def get_random_sexy_opinion():
            return get_random_from_list(sexy_opinions_list)

        font_list = []
        font_list.append("Avara.ttf")
        font_list.append("GlacialIndifference-Regular.otf")
        font_list.append("FantasqueSansMono-Regular.ttf")

        def get_random_font():
            return get_random_from_list(font_list)


        #https://snook.ca/technical/colour_contrast/colour.html A good site to generate colour contrast examples to make sure thigns are readable. Our text background is roughly #3459d2
        readable_color_list = [] #Colors that are easily readable on our blue background.
        readable_color_list.append("#ffffff") #White
        readable_color_list.append("#dddddd") #Grey
        readable_color_list.append("#ffff6e") #Yellow
        readable_color_list.append("#8fff66") #Green
        readable_color_list.append("#ff2c2c") #Red
        readable_color_list.append("#ffd4d4") #Pink
        readable_color_list.append("#FFB1F8") #Hotpink
        readable_color_list.append("#73ffdf") #Teal
        readable_color_list.append("#d62cff") #Purple
        readable_color_list.append("#696eff") #Blue


        def get_random_readable_color():
            return get_random_from_list(readable_color_list)

        def get_titles(the_person): #Returns a list of character titles this person can have. A title is what you call a person, often but not always their name or based on their name.
            list_of_titles = []

            personality_titles = the_person.personality.get_personality_titles(the_person)
            if isinstance(personality_titles, list):
                list_of_titles.extend(personality_titles)
            else:
                list_of_titles.append(personality_titles)


            if the_person.sluttiness > 60:
                list_of_titles.append("Slut")
                if the_person.obedience > 140:
                    list_of_titles.append("Cocksleeve")
                    list_of_titles.appnd("Cock Slave")

            if the_person.sluttiness > (70 - (the_person.get_opinion_score("drinking cum")*5 + the_person.get_opinion_score("creampies")*5 + the_person.get_opinion_score("cum facials")*5 + the_person.get_opinion_score("being covered in cum")*5)):
                list_of_titles.append("Cumslut")

            return list_of_titles #We return the list so that it can be presented to the player. In general the girl will always want to pick the first one on the list.

        def get_random_title(the_person):
            return get_random_from_list(get_titles(the_person))

        def get_possessive_titles(the_person):
            list_of_possessive_titles = []
            #Your mother and sister both have specific personality types, so they get their family titles there.

            personality_possessive_titles = the_person.personality.get_personality_possessive_titles(the_person)
            if isinstance(personality_possessive_titles, list):
                list_of_possessive_titles.extend(personality_possessive_titles)
            else:
                list_of_possessive_titles.append(personality_possessive_titles)

            if employee_role in the_person.special_role:
                list_of_possessive_titles.append("Your employee")
                if the_person.sluttiness > 60:
                    list_of_possessive_titles.append("Your office slut")

            if the_person.obedience > 150 and the_person.sluttiness > 60:
                list_of_possessive_titles.append("Your dedicated cocksleeve")

            if the_person.sluttiness > 60:

                if the_person.love > 50:
                    list_of_possessive_titles.append("Your personal slut")
                elif the_person.love < 0:
                    list_of_possessive_titles.append("Your hatefuck slut")
                else:
                    list_of_possessive_titles.append("Your slut")

            if the_person.sluttiness > (70 - (the_person.get_opinion_score("drinking cum")*5 + the_person.get_opinion_score("creampies")*5 + the_person.get_opinion_score("cum facials")*5 + the_person.get_opinion_score("being covered in cum")*5)):
                list_of_possessive_titles.append("Your cumslut")
                list_of_possessive_titles.append("Your cumdump")

            return list_of_possessive_titles

        def get_random_possessive_title(the_person):
            return get_random_from_list(get_possessive_titles(the_person))

        def get_player_titles(the_person):
            list_of_player_titles = []
            personality_player_titles = the_person.personality.get_personality_player_titles(the_person)
            if isinstance(personality_player_titles, list):
                list_of_player_titles.extend(personality_player_titles)
            else:
                list_of_player_titles.append(personality_player_titles)

            if employee_role in the_person.special_role:
                list_of_player_titles.append("Mr." + mc.last_name)
                if the_person.obedience > 120:
                    list_of_player_titles.append("Sir")
                elif the_person.obedience < 80:
                    list_of_player_titles.append("Boss")

            if the_person.obedience > 140 and the_person.sluttiness > 50:
                list_of_player_titles.append("Master")

            if the_person.sluttiness > 50:
                if the_person.love > 50:
                    list_of_player_titles.append("Daddy")
                elif the_person.love < 0:
                    list_of_player_titles.append("Fuck Meat")
                    list_of_player_titles.append("Cunt Slave")
                else:
                    list_of_player_titles.append("Boy Toy")

            return list_of_player_titles

        def get_random_player_title(the_person):
            return get_random_from_list(get_player_titles(the_person))

init 1 python:
    def generate_premade_list():
        global list_of_premade_characters
        global list_of_unique_characters
        list_of_premade_characters = []
        list_of_premade_characters.append(create_random_person(body_type = "curvy_body", height=0.99, skin="tan", tits="DD",hair_colour="red",hair_style=messy_hair))
        list_of_premade_characters.append(create_random_person(body_type = "thin_body", height=1.0, skin="white", tits="B",hair_colour="red",hair_style=messy_hair))
        list_of_premade_characters.append(create_random_person(body_type = "curvy_body", height=0.96, skin="white", tits="DD",hair_colour="brown",hair_style=twintail))
        list_of_premade_characters.append(create_random_person(body_type = "standard_body", height=0.96, skin="white", tits="DD", hair_colour="red",hair_style=messy_hair))
        list_of_premade_characters.append(create_random_person(body_type = "thin_body", height=0.92, skin="tan", tits="B", hair_colour="black", hair_style=ponytail))
        list_of_premade_characters.append(create_random_person(body_type = "standard_body", height=0.90, skin="white", tits="DD", hair_colour="blond", hair_style=messy_hair))
        list_of_premade_characters.append(create_random_person(body_type = "curvy_body", height=1.00, skin="white", tits="DD", hair_colour="red", hair_style=messy_hair))
        list_of_premade_characters.append(create_random_person(body_type = "thin_body", height=0.94, skin="white", tits="FF", hair_colour="blond", hair_style=long_hair))
        list_of_premade_characters.append(create_random_person(body_type = "standard_body", height=0.95, skin="tan", tits="FF", hair_colour="brown", hair_style=ponytail))

        list_of_unique_characters = []

        dinah_wardrobe = wardrobe_from_xml("Dinah_Wardrobe")
        person_dinah = create_random_person(name = "Dinah", last_name = "Midari", body_type = "standard_body", height=0.99, skin="black", tits="D", hair_colour="black", hair_style=short_hair, starting_wardrobe = dinah_wardrobe)
        list_of_unique_characters.append(person_dinah)

        sylvia_wardrobe = wardrobe_from_xml("Sylvia_Wardrobe")
        person_sylvia = create_random_person(name = "Sylvia", last_name = "Weissfeldt", body_type = "curvy_body", height=0.96, skin="white", tits="C", hair_colour="blond", hair_style = long_hair, starting_wardrobe = sylvia_wardrobe,
            personality = reserved_personality)
        list_of_unique_characters.append(person_sylvia)

        paige_wardrobe = wardrobe_from_xml("Paige_Wardrobe")
        #Well educated and raised in a very middle-class family.
        #Paige is a cool-headed young woman who has confidence without exuberance or extraversion.
        #her favourite activities are generally calm and solitary: reading, playing musical instruments, watching TV, etc.
        #She doesn't make friends quickly, but she is pleasant and easy to get along with, and the bonds she does cultivate are likely to last for life.
        #She has no passion for her work, but she is good at it and takes pride in that fact.
        person_paige = create_random_person(name = "Paige", last_name = "Sallow", body_type = "thin_body", height = 0.98, skin = "white", tits="A", hair_colour="brown", hair_style = messy_ponytail, starting_wardrobe = paige_wardrobe,
            personality = reserved_personality, stat_array = [1,4,3], skill_array = [5,1,2,3,2], sex_array = [2,1,4,2])
        list_of_unique_characters.append(person_paige)

        stephanie_wardrobe = wardrobe_from_xml("Stephanie_Wardrobe")

        global stephanie
        stephanie = create_random_person(name = "Stephanie", age = 29, body_type = "standard_body", face_style = "Face_4",  tits="C", height = 0.95, hair_colour="brown", hair_style = messy_hair, skin="white" , \
            eyes = "brown", personality = stephanie_personality, name_color = "#ff2c2c", dial_color = "#ff2c2c" , starting_wardrobe = stephanie_wardrobe, \
            stat_array = [3,4,3], skill_array = [1,1,4,2,1], sex_array = [3,4,2,1], start_sluttiness = 24, start_obedience = 12, start_happiness = 119, start_love = 10, \
            title = "Stephanie", possessive_title = "Your friend", mc_title = mc.name)


        ### LILY ###
        lily_wardrobe = wardrobe_from_xml("Lily_Wardrobe")

        global lily
        lily = create_random_person(name = "Lily", last_name = mc.last_name, age = 19, body_type = "thin_body", face_style = "Face_6", tits = "B", height = 0.90, hair_colour="blond", hair_style = ponytail, skin="white", \
            eyes = "blue", personality = lily_personality, name_color = "#FFB1F8", dial_color = "#FFB1F8", starting_wardrobe = lily_wardrobe, start_home = lily_bedroom, \
            stat_array = [5,2,2], skill_array = [2,2,0,1,1], sex_array = [2,1,0,0], start_sluttiness = 8, start_obedience = -26, start_happiness = 122, start_love = 15, \
            title = "Lily", possessive_title = "Your sister", mc_title = mc.name)

        lily.special_role = [sister_role]
        lily.schedule[3] = lily.home

        sister_intro_crisis = Action("sister_intro_crisis", sister_intro_crisis_requirements, "sister_intro_crisis_label", args=lily, requirement_args = [lily, renpy.random.randint(7,14)]) #Def is in roles.rpy
        sister_strip_intro_crisis = Action("sister_strip_intro_crisis", sister_strip_intro_requirement, "sister_strip_intro_label", args=lily, requirement_args = lily)

        mc.business.mandatory_crises_list.append(sister_intro_crisis) #Introduces Lily one to two weeks into the game. She will test serum for cash.
        mc.business.mandatory_crises_list.append(sister_strip_intro_crisis) #Lily comes asking for more money. She will strip (to varying degrees) for cash)

        lily.home.add_person(lily)

        ### MOM ###
        mom_wardrobe = wardrobe_from_xml("Mom_Wardrobe")

        global mom
        mom = create_random_person(name = "Jennifer", last_name = mc.last_name, age = 49, body_type = "standard_body", face_style = "Face_1", tits = "DD", height = 0.94, hair_colour = "black", hair_style = long_hair, skin="white", \
            eyes = "brown", personality = mom_personality, name_color = "#8fff66", dial_color = "#8fff66", starting_wardrobe = mom_wardrobe, start_home = mom_bedroom, \
            stat_array = [3,2,4], skill_array = [5,2,0,0,2], sex_array = [2,1,3,0], start_sluttiness = 7, start_obedience = 12, start_happiness = 108, start_love = 25, \
            title = "Mom", possessive_title = "Your mother", mc_title = "Sweetheart")

        mom.special_role = [mother_role]
        mom.schedule[3] = kitchen

        mom_weekly_pay_action = Action("mom weekly pay", mom_weekly_pay_requirement, "mom_weekly_pay_label", args=mom, requirement_args =[mom])
        mc.business.mandatory_crises_list.append(mom_weekly_pay_action)

        mom.home.add_person(mom)


    def get_premade_character(): #Get a premade character and return them when the function is called.
        person = get_random_from_list(list_of_unique_characters)
        if person is not None:
            list_of_unique_characters.remove(person)
            return person

        person = get_random_from_list(list_of_premade_characters)
        if person is not None:
            list_of_premade_characters.remove(person)
        return person
