# Variables for visited branches for each hero
define gavin_seen_today = False
define lance_seen_today = False
define morgan_seen_today = False

define gavin_duty_seen = False
define gavin_happiness_seen = False
define gavin_family_seen = False

define lance_morality_seen = False
define lance_knowlege_seen = False
define lance_relationships_seen = False

define morgan_value_seen = False
define morgan_preservation_seen = False
define morgan_flaws_seen = False

label hero_paths_choice:
    $ gavin_seen_today = False
    $ lance_seen_today = False
    $ morgan_seen_today = False

    menu hero_paths_choice_menu:
        'Gavin' if not gavin_seen_today:
            call hero_paths_gavin
            $ gavin_seen_today = True
        'Gavin (disabled)' if gavin_seen_today:
            pass
        'Lance' if not lance_seen_today:
            call hero_paths_lance
            $ lance_seen_today = True
        'Lance (disabled)' if lance_seen_today:
            pass
        'Morgan' if not morgan_seen_today:
            call hero_paths_morgan
            $ morgan_seen_today = True
        'Morgan (disabled)' if morgan_seen_today:
            pass
    
    if not all([gavin_seen_today, lance_seen_today, morgan_seen_today]):
        jump hero_paths_choice_menu
    
    return

label hero_paths_gavin:
    menu:
        "Duty" if not gavin_duty_seen:
            call gavin_duty
            $ gavin_duty_seen = True
        "Duty (disabled)" if gavin_duty_seen:
            pass
        "Happiness" if not gavin_happiness_seen:
            call gavin_happiness
            $ gavin_happiness_seen = True
        "Happiness (disabled)" if gavin_happiness_seen:
            pass
        "Family" if not gavin_family_seen:
            call gavin_family
            $ gavin_family_seen = True
        "Family (disabled)" if gavin_family_seen:
            pass
    return

    label gavin_duty:
        menu:
            'It\'s a calling, not a certainty':
                call gavin_duty_calling
            'This is a sacred mission, indeed':
                call gavin_duty_sacred_mission
            'Do you really believe you\'re special?':
                call gavin_duty_special
        return

        label gavin_duty_calling:
            guide 'It\'s a calling, not a certainty'
            gavin 'Yeah, I guess so. But it\'s a prophecy, isn\'t it?'
            $ gavin_score = gavin_score + 1
            return

        label gavin_duty_sacred_mission:
            guide 'This is a sacred mission, indeed'
            gavin 'I think so, too'
            $ gavin_score = gavin_score + 0
            return

        label gavin_duty_special:
            guide 'Do you really believe you\'re special?'
            gavin 'I was chosen to save the world!'
            $ gavin_score = gavin_score - 1
            return

    label gavin_happiness:
        menu:
            'Happiness involves others':
                call gavin_happiness_others
            'Happiness is very personal':
                call gavin_happiness_personal
            'Happiness is fleeting':
                call gavin_happiness_fleeting
        return

        label gavin_happiness_others:
            guide '"Happiness involves others"'
            gavin '"Ultimate happiness is when everyone is happy"'
            $ gavin_score = gavin_score + 1
            return

        label gavin_happiness_personal:
            guide '"Happiness is very personal"'
            gavin '"Not everyone will like the same things"'
            $ gavin_score = gavin_score + 0
            return

        label gavin_happiness_fleeting:
            guide '"Happiness is fleeting"'
            gavin '"Well, I was happy before you said that..."'
            $ gavin_score = gavin_score - 1
            return

    label gavin_family:
        menu:
            'Family is a choice':
                call gavin_family_choice
            'Family is blood':
                call gavin_family_blood
            'Family is a hindrance':
                call gavin_family_hindrance
        return

        label gavin_family_others:
            guide '"Family is a choice"'
            gavin '"Like my friends"'
            $ gavin_score = gavin_score + 1
            return

        label gavin_family_blood:
            guide '"Family is blood"'
            gavin '"I guess that makes sense."'
            $ gavin_score = gavin_score + 0
            return

        label gavin_family_hindrance:
            guide '"Family is a hindrance"'
            gavin '"My family is why I\'m here."'
            $ gavin_score = gavin_score - 1
            return

label hero_paths_lance:
    menu:
        "Morality" if not lance_morality_seen:
            call lance_morality
            $ lance_morality_seen = True
        "Morality (disabled)" if lance_morality_seen:
            pass
        "Knowledge" if not lance_knowlege_seen:
            call lance_knowledge
            $ lance_knowlege_seen = True
        "Knowledge (disabled)" if lance_knowlege_seen:
            pass
        "Relationships" if not lance_relationships_seen:
            call lance_relationships
            $ lance_relationships_seen = True
        "Family (disabled)" if lance_relationships_seen:
            pass
    return

    label lance_morality:
        menu:
            'How do you want to be remembered?':
                call lance_morality_remembered
            'It really depends on the circumstance':
                call lance_morality_circumstance
            'Morals are false things of a dead society':
                call lance_morality_false
        return

        label lance_morality_remembered:
            guide '"How do you want to be remembered?"'
            lance '"A good point... though that could be what brings about one\'s end."'
            $ lance_score = lance_score + 1
            return

        label lance_morality_circumstance:
            guide '"It really depends on the circumstance"'
            lance '"I suppose so. But is survival always the right choice..?"'
            $ lance_score = lance_score + 0
            return

        label lance_morality_false:
            guide '"Morals are false things of a dead society"'
            lance '"That kind of thinking is why my family is dead."'
            $ lance_score = lance_score - 1
            return

    label lance_knowledge:
        menu:
            'No amount of harm is acceptable, but we can still learn from our mistakes':
                call lance_knowledge_learn_from_mistakes
            'We should try to avoid causing harm in the pursuit of knowledge':
                call lance_knowledge_avoid_harm
            'Everybody suffers whether we learn something or not':
                call lance_knowledge_everybody_suffers
        return

        label lance_knowledge_learn_from_mistakes:
            guide '"No amount of harm is acceptable, but we can still learn from our mistakes"'
            lance '"Ultimate happiness is when everyone is happy"'
            $ lance_score = lance_score + 1
            return

        label lance_knowledge_avoid_harm:
            guide '"We should try to avoid causing harm in the pursuit of knowledge"'
            lance '"Well, that\'s obvious. I was asking if the knowledge learned from suffering still has value, or if it\'s tainted at its core."'
            $ lance_score = lance_score + 0
            return

        label lance_knowledge_everybody_suffers:
            guide '"Everybody suffers whether we learn something or not"'
            lance '"So everything just suffers pointlessly?"'
            $ lance_score = lance_score - 1
            return

    label lance_relationships:
        menu:
            'Maybe, but they\'re not common.':
                call lance_relationships_not_common
            'Of course there is. Love is unconditional.':
                call lance_relationships_love_is_unconditional
            'Everything has a condition.':
                call lance_relationships_everything_is_conditional
        return

        label lance_relationships_not_common:
            guide '"Maybe, but they\'re not common."'
            lance '"... What would one look like..?"'
            $ lance_score = lance_score + 1
            return

        label lance_relationships_love_is_unconditional:
            guide '"Of course there is. Love is unconditional."'
            lance '"All love? I somehow doubt that."'
            $ lance_score = lance_score + 0
            return

        label lance_relationships_everything_is_conditional:
            guide '"Everything has a condition."'
            lance '"Maybe so. But... I would have liked to have thought otherwise."'
            $ lance_score = lance_score - 1
            return

label hero_paths_morgan:
    menu:
        "Value" if not morgan_value_seen:
            call morgan_life_value
            $ morgan_value_seen = True
        "Value (disabled)" if morgan_value_seen:
            pass
        "Preservation" if not morgan_preservation_seen:
            call morgan_preservation
            $ morgan_preservation_seen = True
        "Preservation (disabled)" if morgan_preservation_seen:
            pass
        "Flaws" if not morgan_flaws_seen:
            call morgan_flaws
            $ morgan_flaws_seen = True
        "Flaws (disabled)" if morgan_flaws_seen:
            pass
    return

    label morgan_life_value:
        menu:
            'It\'s what you choose it to be.':
                call morgan_life_value_choice
            'All life is priceless':
                call morgan_life_value_priceless
            'Life is meaningless regardless of its form':
                call morgan_life_value_meaningless
        return

        label morgan_life_value_choice:
            guide '"It\'s what you choose it to be."'
            morgan '"That\'s a lot of power to put in one person\'s hand."'
            $ morgan_score = morgan_score + 1
            return

        label morgan_life_value_priceless:
            guide '"All life is priceless"'
            morgan '"In the cosmic scheme of things, maybe..."'
            $ morgan_score = morgan_score + 0
            return

        label morgan_life_value_meaningless:
            guide '"Life is meaningless regardless of its form"'
            morgan '"... That\'s not promising."'
            $ morgan_score = morgan_score - 1
            return

    label morgan_preservation:
        menu:
            '"To preserve memories of ourselves and the people we cared for"':
                call morgan_preservation_memories
            'To record history, so we can remember our roots and avoid repeating the past':
                call morgan_preservation_history
            '"To remember our accomplishments and triumphs over our foes."':
                call morgan_preservation_triumph
        return

        label morgan_preservation_memories:
            guide '"To preserve memories of ourselves and the people we cared for"'
            morgan '"... That\'s... one way to look at it."'
            $ morgan_score = morgan_score + 1
            return

        label morgan_preservation_history:
            guide '"To record history, so we can remember our roots and avoid repeating the past"'
            morgan '"Have we really learned anything though?"'
            $ morgan_score = morgan_score + 0
            return

        label morgan_preservation_triumph:
            guide '"To remember our accomplishments and triumphs over our foes."'
            morgan '"So it\'s all just one big contest?"'
            $ morgan_score = morgan_score - 1
            return

    label morgan_flaws:
        menu:
            'Our flaws are meant to be overcome, not define us.':
                call morgan_flaws_overcome
            'There are other things that define us aside from flaws':
                call morgan_flaws_other_things
            'Yes. Our flaws are as ingrained as our DNA':
                call morgan_flaws_ingrained
        return

        label morgan_flaws_overcome:
            guide '"Our flaws are meant to be overcome, not define us."'
            morgan '"That\'s a long road to travel."'
            $ morgan_score = morgan_score + 1
            return

        label morgan_flaws_other_things:
            guide '"There are other things that define us aside from flaws."'
            morgan '"It feels like the flaws outweigh whatever might be good."'
            $ morgan_score = morgan_score + 0
            return

        label morgan_flaws_ingrained:
            guide '"Yes. Our flaws are as ingrained as our DNA."'
            morgan '"Even for me, that\'s absurdly pessimistic."'
            $ morgan_score = morgan_score - 1
            return
