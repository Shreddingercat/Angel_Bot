#!/usr/bin/python3.8
# -*- coding: utf8 -*

import gettext
gettext.bindtextdomain("Text_Instructions", "/locale")
gettext.textdomain("Text_Instructions")
t = gettext.translation("Translate", localedir="locale", languages=['ru_RU'])
t.install()
_ = t.gettext

welcome = _('Hello! This is a telegram bot of the Search And Rescue Squad "Angel". Search And ' \
            'Rescue Squad "Angel" is the first voluntary movement in the Republic of Belarus ' \
            'to assist in the search for missing people. How can we help you? Choose from the ' \
            'options provided. If you haven\'t found your option, just write to us. We will ' \
            'definitely answer')

missing = _('If a person is missing, the first step is to call the Accident Registration Bureau. ' \
            'All information flows here every day from the duty units, ' \
            'sobering-up centers, hospitals and morgues, and is entered into a single database. ' \
            'It contains information about persons detained by the internal affairs bodies and ' \
            'persons taken to medical institutions who are unable to provide information about ' \
            'themselves, as well as information about the discovery of unknown corpses. You need ' \
            'to tell the operator in detail about what happened. There you will be given ' \
            'information about all accidents and accidents that have occurred over the past day. ' \
            'The fact of possible hospitalization of the missing person by the ambulance service ' \
            'should be checked.')

found = _('Call any of the numbers listed in the orientation.')

volunteer = _('You can personally help in finding the missing person by:\n- disseminating ' \
            'information on the Internet;\n- pasting orientation and interviewing passers-by;\n' \
            '- departure for urban and forest searches;\n- and others.\nEach person, regardless ' \
            'of which city he is in, can provide significant assistance. Everyone is dear to us!')

donate = _('How can you support the "Angel"?\nWith the help of donations!\n\n☎ USSD request for MTS ' \
            'subscribers, A1 and life:) - *222*13#!\n💳 by transfer from a bank card (there is also ' \
            'a subscription to monthly transfers) https://imenamag.by/projects/26988691 \n📥 ' \
            'Electronic payments (ERIP) service code 4345671\n☎ replenishment of detachment mobile ' \
            'phones +375(33)6666-856, +375(33)6666-033')

missing_key = _('The person is missing')

found_key = _('The person is found')

volunteer_key = _('I want to become a volunteer')

donate_key = _('Donate')

feedback = _('Your message has been accepted. We will contact you as soon as possible')