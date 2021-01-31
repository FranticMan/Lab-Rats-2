## This file is used to house all of the functions and lables used to debug LR2.##
# CURRENT CONCLUSIONS: #
# 1) Time to create people is independent of the number of people involved.
#
#
#
#
#
#

## LEADS:##
# 1) Outfits that deep copy other outfits (and other improper uses of deepcopy) will end up duplicating the image set library for each clothing item (which should be a singleton). That makes character objects huge and the game slow.
# 2) Moving characters at the end of the day takes seconds for a large number of people.
# 3) Running hte move code involves a deep copy. Likely the issue.
#
#
#

## RESOLUTIONS: ##
# 1) Add a create_copy function to the outfit and clothign class that properly copy it without the use of deep copy.
# 2) Review all uses of deep copy and remove them if at all possible. Purge them, they are almost certainly not being used correctly.
#
#
#
#
#



init -15 python:
    from datetime import datetime
    import traceback

    # def log_image(the_image_stream):
    #     file_path = os.path.abspath(os.path.join(config.basedir, "game"))
    #     file_name = os.path.join(file_path,"DEBUG_IMAGE_LOG.txt")
    #     opened_file = os.open(file_name,os.O_WRONLY|os.O_APPEND|os.O_CREAT) #Open the log, create it if it doesn't exist already.
    #
    #     string_to_write = "TIME: " + datetime.now().strftime('%Y-%m-%d %H:%M:%S') + ":\n" + the_image_stream.getbuffer() + "\n"
    #     os.write(opened_file, string_to_write)
    #     os.close(opened_file) #Close everything

    def log_message(the_message):
        if not config.developer:
            return #Don't log anything if we're on a production platform.
        file_path = os.path.abspath(os.path.join(config.basedir, "game"))
        file_name = os.path.join(file_path,"DEBUG_LOG.txt")
        opened_file = os.open(file_name,os.O_WRONLY|os.O_APPEND|os.O_CREAT) #Open the log, create it if it doesn't exist already.

        string_to_write = "TIME: " + datetime.now().strftime('%Y-%m-%d %H:%M:%S') + " | " + the_message + "\n"
        os.write(opened_file, string_to_write)
        os.close(opened_file) #Close everything

    def log_missing_personality_labels():
        for personality in list_of_personalities:
            for ending in personality.response_label_ending:
                if not renpy.has_label(personality.personality_type_prefix + "_" + ending):
                    if not renpy.has_label(personality.default_prefix + "_" + ending):
                        log_message("CRITICAL ERROR: Personality \"" + personality.personality_type_prefix + "\" Lacks any label for dialogue type \"" + ending + "\"")
                    else:
                        log_message("Warning: Personality \"" + personality.personality_type_prefix + "\" is using it's default entry for dialogue type \"" + ending + "\"")

    class VrenZipImage(renpy.display.im.ImageBase): #TODO: Move this to a more obvious file. Probably something to do along with a bunch of other refactoring.
        def __init__(self, position, filename, mtime=0, **properties):
            super(VrenZipImage, self).__init__(position, filename, mtime, **properties)
            self.position = position
            self.filename = filename

        def load(self):
            tries = 0
            max_tries = 5
            while tries < max_tries:
                global mobile_zip_dict
                try:
                    data = mobile_zip_dict[self.position].read(self.filename)
                    sio = io.BytesIO(data)
                    the_image = renpy.display.pgrender.load_image(sio, self.filename)
                    return the_image

                except (zipfile.BadZipfile, RuntimeError): #Not my fault! See: https://github.com/pfnet/pfio/issues/104
                    e = sys.exc_info()[1]
                    log_message("ERR " + str(tries) + ": "  + str(e))
                    tries += 1
                    if tries >= max_tries:
                        renpy.notify("Unsuccessful Recovery: " + self.position + ", Item: " + self.filename)
                        return renpy.display.pgrender.surface((2, 2), True)

                    else:
                        file_name = mobile_zip_dict[self.position].filename
                        mobile_zip_dict[self.position].close()
                        mobile_zip_dict[self.position] = zipfile.ZipFile(self.filename, "r") #May have to convert to a renpy_file first, but I dthink Zipfile will have alreayd done that



label person_select_debug:
    "Calling screen now!"
    call screen employee_overview(person_select = True)
    "Done! The returned person was: [_return.name]!"
    return

label debug_start:
    #TODO: Debug stuff here.
    $ log_message("Starting our debugging!")
    $ log_message("Creating town with no people.")
    $ town_time = time.time()
    call create_test_variables("DEBUG", "DEBUG INC.","LASTNAME",[0,0,0], [0,0,0,0,0], [0,0,0,0,0],max_num_of_random=0) from _call_create_test_variables_1
    $ log_message("Finished. Took: " + str(time.time()-town_time) + " Seconds")
    $ people_per_location = 20

    $ log_message("Populating town now. Adding " + str(people_per_location) + " people to each location.")
    $ person_time = time.time()
    $ location_count = 0
    python:
        for place in list_of_places:
            if place.public:
                location_count += 1
                for x in range(0,people_per_location):
                    the_person = create_random_person()
                    the_person.generate_home()
                    place.add_person(the_person)
    $ log_message("Finished. Added " + str(location_count*people_per_location) + " people total to " + str(location_count) + " places.")
    $ log_message("Total time: " + str(time.time()-person_time) + " Seconds. Average time per person: " + str((time.time()-person_time)/(people_per_location*location_count)) + " Seconds.")

    $ log_message("Now doubling number of people. Time per person should remain constant.")
    $ person_time = time.time()
    $ location_count = 0
    python:
        for place in list_of_places:
            if place.public:
                location_count += 1
                for x in range(0,people_per_location):
                    place.add_person(create_random_person())
    $ log_message("Finished. Added " + str(location_count*people_per_location) + " people total to " + str(location_count) + " places.")
    $ log_message("Total time: " + str(time.time()-person_time) + " Seconds. Average time per person: " + str((time.time()-person_time)/(people_per_location*location_count)) + " Seconds.")

    $ log_message("Debugging Finished.")
    return

label debug_run_turn:
    $ log_message("Starting our turn debugging!")
    $ log_message("Advancing time now.")
    $ turn_time = time.time()
    call advance_time from _call_advance_time_27
    $ log_message("Finished. Time taken: " + str(time.time()-turn_time))
    return

label debug_create_position_csv():
    python:
        string = ""
        full_list_of_positions = list_of_positions[:]
        for position in list_of_positions + list_of_girl_positions:
            for connection in position.connections:
                full_list_of_positions.append(connection) #Get all of their stuff
        set_of_positions = __builtin__.set(full_list_of_positions) #Trim out repeated objects.

        for position in set_of_positions:
            string += position.name + ", "
            string += position.skill_tag + ", "
            string += str(position.guy_arousal) + ", "
            string += str(position.girl_arousal) + ", "
            string += str(position.guy_energy) + ", "
            string += str(position.girl_energy) + ", "
            string += str(position.slut_requirement) + ", "
            string += str(position.slut_cap) + ", "
            for trans in position.transitions:
                string += position.name + " -> " + trans[0].name + " | "
            string += "\n"

        log_message("Position CSV: " + string)
    return

label edit_default_wardrobe:
    call screen girl_outfit_select_manager(default_wardrobe, show_sets = True)
    $ picked_outfit = _return
    call create_outfit(picked_outfit) from _call_create_outfit_2
    return

label load_select_from_wardrobe(the_wardrobe):
    call screen girl_outfit_select_manager(the_wardrobe, show_sets = True)
    $ picked_outfit = _return
    call create_outfit(picked_outfit) from _call_create_outfit_3
    return

screen display_all_faces():
    add "Paper_Background.png"
    hbox:
        spacing -250
        add "character_images/default_Face_1_stand2_white.png"
        add "character_images/default_Face_2_stand2_white.png"
        add "character_images/default_Face_3_stand2_white.png"
        add "character_images/default_Face_4_stand2_white.png"
        add "character_images/default_Face_5_stand2_white.png"
        add "character_images/default_Face_6_stand2_white.png"

screen display_all_hair():
    add "Paper_Background.png"
    viewport:
        mousewheel True
        scrollbars "vertical"
        xsize 1920
        ysize 1080

        vbox:
            spacing -900
            for hair in hair_styles:
                hbox:
                    text hair.name
                    $ hair_displayable = hair.generate_item_displayable("standard_body", "AA", "stand2")
                    add hair_displayable

label test_malformed_say(the_person):
    the_person "Hello world!"
    the_person "This is a test!"
    return
